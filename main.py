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

@app.post("/admin", response_model=AdminResponse, status_code=201 )
def criar_admin(admin: AdminCreate, db:Session = Depends(get_db)):
    admin_criado = db.query(Admin).filter(Admin.email == admin.email).first()

    if admin_criado:
        raise HTTPException(status_code=400, detail="Credenciais inválidas, tente novamente")
    
    novo_admin = Admin(**admin.model_dump())
    db.add(novo_admin)
    db.commit()
    db.refresh(novo_admin)

    message = novo_admin.nome

    return message