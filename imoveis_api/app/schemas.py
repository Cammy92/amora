from pydantic import BaseModel
from typing import Optional

class ImovelCreate(BaseModel):
    endereco: str
    valor: float
    tipo: str

class NegociacaoCreate(BaseModel):
    comprador: str
    renda_comprador: float
    pontuacao_credito: int
    imovel: ImovelCreate

class NegociacaoResponse(BaseModel):
    id: int
    status: str
    comprador: str
    renda_comprador: float
    pontuacao_credito: int
    imovel: ImovelCreate

    class Config:
        orm_mode = True
