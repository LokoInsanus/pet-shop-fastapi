from pydantic import BaseModel

class Cliente(BaseModel):
    id: int
    nome: str
    email: str
    rua: str
    bairro: str
    numeroCasa: str
    numeroTelefone: str
    cpf: str

class Pet(BaseModel):
    id: int
    nome: str
    animal: str
    id_dono: int
    raca: str
    rga: str