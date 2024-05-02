from pydantic import BaseModel

class Pet(BaseModel):
    id: int
    nome: str
    animal: str
    id_dono: int
    raca: str
    rga: str