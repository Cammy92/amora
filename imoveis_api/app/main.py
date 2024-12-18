from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/imoveis", response_model=schemas.NegociacaoResponse)
def criar_imovel(negociacao: schemas.NegociacaoCreate, db: Session = Depends(get_db)):
    return crud.criar_negociacao(db, negociacao)

@app.get("/imoveis/{id}", response_model=schemas.NegociacaoResponse)
def obter_imovel(id: int, db: Session = Depends(get_db)):
    negociacao = crud.obter_negociacao_por_id(db, id)
    if not negociacao:
        raise HTTPException(status_code=404, detail="Negociação não encontrada")
    return negociacao
