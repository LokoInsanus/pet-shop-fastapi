from pydantic import BaseModel
from typing import Optional

class Cliente(BaseModel):
    id: Optional[int]
    nome: str
    email: str
    rua: str
    bairro: str
    numeroCasa: str
    numeroTelefone: str
    cpf: str

class Pet(BaseModel):
    id: Optional[int]
    nome: str
    animal: str
    id_dono: int
    raca: str
    rga: str