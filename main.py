from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db, engine, Base
from models import (Admin, Favorito, Editora,
                    Autor,Emprestimo, Usuario, Livro) 
from schemas import (AdminCreate, AdminUpdate, AdminResponse,
                    Favorito,EditoraCreate, EditoraUpdate,
                    EditoraResponse, AutorCreate, AutorUpdate,
                    AutorResponse, EmprestimoCreate, EmprestimoUpdate,
                    EmprestimoResponse,UsuarioCreate,UsuarioUpdate,
                    UsuarioResponse, LivroCreate, LivroUpdate, 
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

@app.put("/admin/{usuario_id}", response_model= AdminResponse)
def atualizar_admin(usuario_id: int, admin_model:AdminUpdate, db: Session = Depends(get_db)):
    admin = db.query(Admin).filter(Admin.id == usuario_id ).first()

    if not admin:
        raise HTTPException(status_code=404, detail="Admin não encontrado")
    
    dados_atualizado = admin_model.model_dump(exclude_unset=True)
    for campo, valor in dados_atualizado.items():
        setattr(admin,campo,valor)

    db.commit()
    db.refresh(admin)
    return admin

@app.delete("/admin/{admin_id}",status_code=204)
def deletar_admin(usuarioid: int, db: Session = Depends(get_db)):
    admin = db.query(Admin).filter(Admin.id == usuarioid).first()
    if not admin:
        raise HTTPException(status_code=404, detail="admin não encontrado")

    db.delete(admin)
    db.commit()
    return None

# Usuario
@app.post("/usuarios", response_model=UsuarioResponse, status_code=204 )
def criar_usuario(usuario: UsuarioCreate, db:Session = Depends(get_db)):
    usuario_criado = db.query(Usuario).filter(Usuario.email == usuario.email).first()

    if usuario_criado:
        raise HTTPException(status_code=400, detail="Credenciais inválidas, tente novamente")
    
    novo_usuario= Usuario(**usuario.model_dump())
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario


@app.put("/usuarios/{usuario_id}", response_model= UsuarioResponse)
def atualizar_usuario(usuario_id: int, usuario_model:UsuarioUpdate, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id ).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    
    dados_atualizado = usuario_model.model_dump(exclude_unset=True)
    for campo, valor in dados_atualizado.items():
        setattr(usuario,campo,valor)

    db.commit()
    db.refresh(usuario)
    return usuario

@app.delete("/usuarios/{usuario_id}",status_code=204)
def deletar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="usuario não encontrado")

    db.delete(usuario)
    db.commit()
    return None

# livro 
@app.post("/livros", response_model=LivroResponse, status_code=204 )
def criar_livro(livro: LivroCreate, db:Session = Depends(get_db)):
    livro_criado = db.query(Livro).filter(Livro.titulo == livro.titulo).first()

    if livro_criado:
        raise HTTPException(status_code=400, detail="Título já registrado, tente novamente")
    
    novo_livro= Livro(**livro.model_dump())
    db.add(novo_livro)
    db.commit()
    db.refresh(novo_livro)

    return novo_livro

@app.put("/livros/{livros_id}", response_model= LivroResponse)
def atualizar_livro(livros_id: int, livro_model:LivroUpdate, db: Session = Depends(get_db)):
    livro = db.query(Livro).filter(Livro.id == livros_id ).first()

    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    
    dados_atualizado = livro_model.model_dump(exclude_unset=True)
    for campo, valor in dados_atualizado.items():
        setattr(livro,campo,valor)

    db.commit()
    db.refresh(livro)
    return livro

@app.delete("/livros/{livros_id}",status_code=204)
def deletar_livro(livros_id: int, db: Session = Depends(get_db)):
    livro = db.query(Livro).filter(Livro.id == livros_id).first()
    if not livro:
        raise HTTPException(status_code=404, detail="livro não encontrado")

    db.delete(livro)
    db.commit()
    return None