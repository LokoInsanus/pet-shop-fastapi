from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from cliente import Cliente
from pet import Pet

app = FastAPI()

origins = ['http://localhost:5500']

cliente_db: List[Cliente] = []
pet_db: List[Pet] = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/")
def api():
    return "Bem vindo a API da PetShop"

# Pets
@app.get("/pet", response_model=List[Pet])
def listar_pet():
    return pet_db

@app.post("/pet", response_model=Pet)
def cadastrar_pet(pet: Pet):
    try:
        for i in range(len(pet_db)):
            if pet_db[i] == None:
                pet.id = len(pet_db) + 1
                pet_db.insert(i, pet)
                return pet
        pet.id = len(pet_db) + 1
        pet_db.append(pet)
        return pet
    except Exception as e:
        print("Erro ao criar pet:", e)
        raise HTTPException(status_code=500, detail="Erro ao criar pet")

@app.get("/pet/{id}", response_model=Pet)
def buscar_pet(id: int):
    for pet in pet_db:
        if pet.id == id:
            return pet
    return None

@app.delete("/pet/{id}")
def deletar_pet(id: int):
    try:
        for pet in pet_db:
            if pet.id == id:
                pet_db.remove(pet)
                return "Removido com sucesso"
        return "Pet não encontrado"
    except Exception as e:
        print("Erro ao deletar pet:", e)
        raise HTTPException(status_code=500, detail="Erro ao deletar pet")

# Clientes
@app.get("/cliente", response_model=List[Cliente])
def listar_clientes():
    return cliente_db

@app.post("/cliente", response_model=Cliente)
def cadastrar_cliente(cliente: Cliente):
    try:
        for i in range(len(cliente_db)):
            if cliente_db[i] == None:
                cliente.id = len(cliente_db) + 1
                cliente_db.insert(i, cliente)
                return cliente
        cliente.id = len(cliente_db) + 1
        cliente_db.append(cliente)
        return cliente
    except Exception as e:
        print("Erro ao criar cliente:", e)
        raise HTTPException(status_code=500, detail="Erro ao criar cliente")

@app.get("/cliente/{id}", response_model=Cliente)
def buscar_cliente(id: int):
    for cliente in cliente_db:
        if cliente.id == id:
            return cliente
    return None

@app.delete("/cliente/{id}")
def deletar_cliente(id: int):
    try:
        for cliente in cliente_db:
            if cliente.id == id:
                cliente_db.remove(cliente)
                return "Removido com sucesso"
        return "Pet não encontrado"
    except Exception as e:
        print("Erro ao deletar cliente:", e)
        raise HTTPException(status_code=500, detail="Erro ao deletar cliente")