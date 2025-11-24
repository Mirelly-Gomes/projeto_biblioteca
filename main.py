from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db, engine, Base
from models import (Admin, Favorito, Editora,
                    Autor,Emprestimo, Usuario, Livro) 
from schemas import (AdminCreate, AdminUpdate, AdminResponse,
                    Favorito,EditoraCreated, EditoraUpdate,
                    EditoraResponse, AutorCreated, AutorUpdate,
                    AutorResponse, EmprestimoCreated, EmprestimoUpdate,
                    EmprestimoResponse,UsuarioCreated,UsuarioUpdate,
                    UsuarioResponse, LivroCreated, LivroUpdate, 
                    LivroResponse)
                      

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return "Está no ar"

@app.get("/livros", response_model=List[LivroResponse])
def listar_livros(db:Session = Depends(get_db)):
    livros = db.query(Livro).all()

    return livros

# @app.post("/donos", response_model=DonoResponse, status_code=201 )
# def criar_dono(dono: DonoCreate, db:Session = Depends(get_db)):
#     dono_existe = db.query(Dono).filter(Dono.cpf == dono.cpf).first()

#     if dono_existe:
#         raise HTTPException(status_code=400, detail="CPF já cadastrado")
    
#     novo_dono = Dono(**dono.model_dump())
#     db.add(novo_dono)
#     db.commit()
#     db.refresh(novo_dono)
#     return novo_dono