from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from schemas.schema import Cliente
from schemas.schema import Pet
from sqlalchemy.orm import Session
from infra.sqlalchemy.config.database import get_db, criar_bd
from infra.sqlalchemy.repositories.cliente import RepositorioCliente
from infra.sqlalchemy.repositories.pet import RepositorioPet

app = FastAPI()

origins = ['http://localhost:5500']

cliente_db: List[Cliente] = []
pet_db: List[Pet] = []

criar_bd()

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
def listar_pet(db:Session = Depends(get_db)):
    return RepositorioPet(db).listar()

@app.post("/pet", response_model=Pet)
def cadastrar_pet(pet: Pet, db:Session = Depends(get_db)):
    try:
        RepositorioPet(db).criar(pet)
        return pet
    except Exception as e:
        print("Erro ao criar pet:", e)
        raise HTTPException(status_code=500, detail="Erro ao criar pet")

@app.get("/pet/{id}", response_model=Pet)
def buscar_pet(id: int, db:Session = Depends(get_db)):
    return RepositorioPet(db).obter(id)

@app.delete("/pet/{id}")
def deletar_pet(id: int, db:Session = Depends(get_db)):
    try:
        if RepositorioPet(db).remover(id):
            return "Removido com sucesso"
        return "Pet não encontrado"
    except Exception as e:
        print("Erro ao deletar pet:", e)
        raise HTTPException(status_code=500, detail="Erro ao deletar pet")

# Clientes
@app.get("/cliente", response_model=List[Cliente])
def listar_clientes(db:Session = Depends(get_db)):
    return RepositorioCliente(db).listar()

@app.post("/cliente", response_model=Cliente)
def cadastrar_cliente(cliente: Cliente, db:Session = Depends(get_db)):
    try:
        RepositorioCliente(db).criar(cliente)
        return cliente
    except Exception as e:
        print("Erro ao criar cliente:", e)
        raise HTTPException(status_code=500, detail="Erro ao criar cliente")

@app.get("/cliente/{id}", response_model=Cliente)
def buscar_cliente(id: int, db:Session = Depends(get_db)):
    return RepositorioCliente(db).obter(id)

@app.delete("/cliente/{id}")
def deletar_cliente(id: int, db:Session = Depends(get_db)):
    try:
        if RepositorioCliente(db).remover(id):
            return "Removido com sucesso"
        return "Pet não encontrado"
    except Exception as e:
        print("Erro ao deletar cliente:", e)
        raise HTTPException(status_code=500, detail="Erro ao deletar cliente")