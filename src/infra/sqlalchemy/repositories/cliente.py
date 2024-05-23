from sqlalchemy.orm import Session
from schemas import schema
from infra.sqlalchemy.models import models

class RepositorioCliente():

    def __init__(self, db: Session):
        self.db = db
        


    def criar(self, cliente: schema.Cliente):# Covertendo o Schema em um modelo
        db_cliente = models.Cliente(nome=cliente.nome, 
                                    email=cliente.email,
                                    rua=cliente.rua,
                                    bairro=cliente.bairro,
                                    numeroCasa=cliente.numeroCasa,
                                    numeroTelefone=cliente.numeroTelefone,
                                    cpf=cliente.cpf
                                    )
        self.db.add(db_cliente)
        self.db.commit()
        self.db.refresh(db_cliente)
        return db_cliente


    def listar(self):
        clientes = self.db.query(models.Cliente).all()
        return  clientes

    def obter(self):
        pass

    def remover(self):
        pass