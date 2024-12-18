from sqlalchemy.orm import Session
from app import models, schemas, risk_evaluation

def criar_negociacao(db: Session, negociacao: schemas.NegociacaoCreate):
    imovel = models.Imovel(
        endereco=negociacao.imovel.endereco,
        valor=negociacao.imovel.valor,
        tipo=negociacao.imovel.tipo
    )
    db.add(imovel)
    db.commit()
    db.refresh(imovel)

    status = risk_evaluation.avaliar_risco(
        imovel.valor, negociacao.pontuacao_credito, negociacao.renda_comprador
    )
    nova_negociacao = models.Negociacao(
        comprador=negociacao.comprador,
        renda_comprador=negociacao.renda_comprador,
        pontuacao_credito=negociacao.pontuacao_credito,
        imovel_id=imovel.id,
        status=status
    )
    db.add(nova_negociacao)
    db.commit()
    db.refresh(nova_negociacao)
    return nova_negociacao

def obter_negociacao_por_id(db: Session, id: int):
    return db.query(models.Negociacao).filter(models.Negociacao.id == id).first()
