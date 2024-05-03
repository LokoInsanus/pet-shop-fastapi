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