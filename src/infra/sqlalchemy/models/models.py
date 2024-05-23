from sqlalchemy import Column, Integer, String, Float, Boolean
from infra.sqlalchemy.config.database import Base

class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    rua = Column(String)
    bairro = Column(String)
    numeroCasa = Column(String)
    numeroTelefone = Column(String)
    cpf = Column(String)

class Pet(Base):
    __tablename__ = "pet"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    animal = Column(String)
    id_dono = Column(Integer)
    raca = Column(String)
    rga = Column(String)