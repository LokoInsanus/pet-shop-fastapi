from fastapi import FastAPI
from typing import List, Optional
from cliente import Cliente
from pet import Pet

app = FastAPI()

cliente_db: List[Cliente] = []
pet_db: List[Pet] = []

@app.get("/")
def api():
    return "Bem vindo a API da PetShop"

# Pets
@app.get("/pet", response_model=List[Pet])
def listar_pet():
    return pet_db

@app.post("/pet", response_model=Pet)
def cadastrar_pet(pet: Pet):
    for i in range(len(pet_db)):
        if pet_db[i] == None:
            pet_db.insert(i, pet)
            return pet
    pet_db.append(pet)
    return pet

@app.get("/pet/{id}", response_model=Pet)
def buscar_pet(id: int):
    for pet in pet_db:
        if pet.id == id:
            return pet
    return None

@app.delete("/pet/{id}")
def deletar_pet(id: int):
    for pet in pet_db:
        if pet.id == id:
            pet_db.remove(pet)
            return "Removido com sucesso"
    return "Pet não encontrado"

# Clientes
@app.get("/cliente", response_model=List[Cliente])
def listar_clientes():
    return cliente_db

@app.post("/cliente", response_model=Cliente)
def cadastrar_cliente(cliente: Cliente):
    cliente_db.append(cliente)
    return cliente

@app.get("/cliente/{id}", response_model=Cliente)
def buscar_cliente(id: int):
    for cliente in cliente_db:
        if cliente.id == id:
            return cliente
    return None

@app.delete("/cliente/{id}")
def deletar_cliente(id: int):
    for cliente in cliente_db:
        if cliente.id == id:
            cliente_db.remove(cliente)
            return "Removido com sucesso"
    return "Pet não encontrado"