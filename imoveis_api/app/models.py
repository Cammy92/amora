from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Imovel(Base):
    __tablename__ = "imoveis"
    id = Column(Integer, primary_key=True, index=True)
    endereco = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    tipo = Column(String, nullable=False)

class Negociacao(Base):
    __tablename__ = "negociacoes"
    id = Column(Integer, primary_key=True, index=True)
    comprador = Column(String, nullable=False)
    renda_comprador = Column(Float, nullable=False)
    pontuacao_credito = Column(Integer, nullable=False)
    imovel_id = Column(Integer, ForeignKey("imoveis.id"), nullable=False)
    status = Column(String, nullable=False)

    imovel = relationship("Imovel")
