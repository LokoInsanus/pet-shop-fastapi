from sqlalchemy.orm import Session
from schemas import schema
from infra.sqlalchemy.models import models

class RepositorioPet():

    def __init__(self, db: Session):
        self.db = db
        


    def criar(self, pet: schema.Pet):# Covertendo o Schema em um modelo
        db_pet = models.Pet(nome=pet.nome, 
                            animal=pet.animal,
                            id_dono=pet.id_dono,
                            raca=pet.raca,
                            rga=pet.rga
                            )
        self.db.add(db_pet)
        self.db.commit()
        self.db.refresh(db_pet)
        return db_pet


    def listar(self):
        pets = self.db.query(models.Pet).all()
        return  pets

    def obter(self):
        pass

    def remover(self):
        pass