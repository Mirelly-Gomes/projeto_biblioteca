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

#admin
@app.post("/admin", response_model=AdminResponse, status_code=201 )
def criar_admin(admin: AdminCreate, db:Session = Depends(get_db)):
    admin_criado = db.query(Admin).filter(Admin.email == admin.email).first()

    if admin_criado:
        raise HTTPException(status_code=400, detail="Credenciais inválidas, tente novamente")
    
    novo_admin = Admin(**admin.model_dump())
    db.add(novo_admin)
    db.commit()
    db.refresh(novo_admin)

    return novo_admin

@app.put("/admin/{admin_id}", response_model= AdminResponse)
def atualizar_admin(admin_id: int, admin_model:AdminUpdate, db: Session = Depends(get_db)):
    admin = db.query(Admin).filter(Admin.id == admin_id ).first()

    if not admin:
        raise HTTPException(status_code=404, detail="Admin não encontrado")
    
    dados_atualizado = admin_model.model_dump(exclude_unset=True)
    for campo, valor in dados_atualizado.items():
        setattr(admin,campo,valor)

    db.commit()
    db.refresh(admin)
    return admin

@app.delete("/admin/{admin_id}",status_code=204)
def deletar_admin(admin_id: int, db: Session = Depends(get_db)):
    admin = db.query(admin).filter(admin.id == admin_id).first()
    if not admin:
        raise HTTPException(status_code=404, detail="admin não encontrado")

    db.delete(admin)
    db.commit()
    return None