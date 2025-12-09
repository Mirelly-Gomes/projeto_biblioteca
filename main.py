from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db, engine, Base
from models import (Admin, Favorito as FavoritoMl, Editora,
                    Autor,Emprestimo, Usuario, Livro) 
from schemas import (AdminCreate, AdminUpdate, AdminResponse,
                    EditoraCreate, EditoraUpdate,
                    EditoraResponse, AutorCreate, AutorUpdate,
                    AutorResponse, EmprestimoCreate, EmprestimoUpdate,
                    EmprestimoResponse,UsuarioCreate,UsuarioUpdate,
                    UsuarioResponse, LivroCreate, LivroUpdate, 
                    LivroResponse, FavoritoCreate, FavoritoResponse)
                      

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

@app.put("/admin/{admin_id}", response_model=AdminResponse)
def atualizar_admin(admin_id: int, admin_model: AdminUpdate, db: Session = Depends(get_db)):
    admin = db.query(Admin).filter(Admin.id == admin_id).first()

    if not admin:
        raise HTTPException(status_code=404, detail="Admin não encontrado")

    dados_atualizado = admin_model.model_dump(exclude_unset=True)
    for campo, valor in dados_atualizado.items():
        setattr(admin, campo, valor)

    db.commit()
    db.refresh(admin)
    return admin

@app.delete("/admin/{admin_id}", status_code=204)
def deletar_admin(admin_id: int, db: Session = Depends(get_db)):
    admin = db.query(Admin).filter(Admin.id == admin_id).first()

    if not admin:
        raise HTTPException(status_code=404, detail="Admin não encontrado")

    db.delete(admin)
    db.commit()
    return None

# Usuario
@app.post("/usuarios", response_model=UsuarioResponse, status_code=201)
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_criado = db.query(Usuario).filter(Usuario.email == usuario.email).first()

    if usuario_criado:
        raise HTTPException(status_code=400, detail="Credenciais inválidas, tente novamente")
    
    novo_usuario = Usuario(**usuario.model_dump())
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
@app.post("/livros", response_model=LivroResponse, status_code=201 )
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

# autor

@app.post("/autores", response_model=AutorResponse, status_code=201 )
def criar_autor(autor: AutorCreate, db:Session = Depends(get_db)):
    autor_criado = db.query(Autor).filter(Autor.nome == autor.nome).first()

    if autor_criado:
        raise HTTPException(status_code=400, detail="Autor já registrado, tente novamente")
    
    novo_autor= Autor(**autor.model_dump())
    db.add(novo_autor)
    db.commit()
    db.refresh(novo_autor)

    return novo_autor

@app.get("/autores", response_model=List[AutorResponse])
def listar_autores(db: Session = Depends(get_db)):
    return db.query(Autor).all()

@app.put("/autores/{autor_id}", response_model= AutorResponse)
def atualizar_autor(autor_id: int, autor_model:AutorUpdate, db: Session = Depends(get_db)):
    autor = db.query(Autor).filter(Autor.id == autor_id ).first()

    if not autor:
        raise HTTPException(status_code=404, detail="Autor não encontrado")
    
    dados_atualizado = autor_model.model_dump(exclude_unset=True)
    
    for campo, valor in dados_atualizado.items():
        setattr(autor,campo,valor)

    db.commit()
    db.refresh(autor)

    return autor

@app.delete("/autores/{autor_id}",status_code=204)
def deletar_autor(autor_id: int, db: Session = Depends(get_db)):
    autor = db.query(Autor).filter(Autor.id == autor_id).first()
   
    if not autor:
        raise HTTPException(status_code=404, detail="Autor não encontrado")

    db.delete(autor)
    db.commit()

# editoras

@app.post("/editoras", response_model=EditoraResponse, status_code=201)
def criar_editora(editora: EditoraCreate, db: Session = Depends(get_db)):
    editora_criada = db.query(Editora).filter(Editora.nome == editora.nome).first()

    if editora_criada:
        raise HTTPException(status_code=400, detail="Editora já cadastrada")

    nova_editora = Editora(**editora.model_dump())
    db.add(nova_editora)
    db.commit()
    db.refresh(nova_editora)

    return nova_editora

@app.get("/editoras", response_model=List[EditoraResponse])
def listar_editoras(db: Session = Depends(get_db)):
    return db.query(Editora).all()

@app.put("/editoras/{editora_id}", response_model=EditoraResponse)
def atualizar_editora(editora_id: int, editora_model: EditoraUpdate, db: Session = Depends(get_db)):
    editora = db.query(Editora).filter(Editora.id == editora_id).first()

    if not editora:
        raise HTTPException(status_code=404, detail="Editora não encontrada")

    dados_atualizado = editora_model.model_dump(exclude_unset=True)
    for campo, valor in dados_atualizado.items():
        setattr(editora, campo, valor)

    db.commit()
    db.refresh(editora)

    return editora

@app.delete("/editoras/{editora_id}", status_code=204)
def deletar_editora(editora_id: int, db: Session = Depends(get_db)):
    editora = db.query(Editora).filter(Editora.id == editora_id).first()

    if not editora:
        raise HTTPException(status_code=404, detail="Editora não encontrada")

    db.delete(editora)
    db.commit()
    

#favoritos
@app.post("/favoritos", response_model=FavoritoResponse, status_code=201)
def adicionar_favorito(favorito: FavoritoCreate, db: Session = Depends(get_db)):

    ja_existe = db.query(FavoritoMl).filter(
        FavoritoMl.usuario_id == favorito.usuario_id,
        FavoritoMl.livro_id == favorito.livro_id
    ).first()

    if ja_existe:
        raise HTTPException(status_code=400, detail="Favorito já existe")

    novo = FavoritoMl(**favorito.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)

    return novo



@app.get("/favoritos/{usuario_id}")
def listar_favoritos(usuario_id: int, db: Session = Depends(get_db)):
    return db.query(FavoritoMl).filter(FavoritoMl.usuario_id == usuario_id).all()


@app.delete("/favoritos/{favorito_id}", status_code=204)
def remover_favorito(favorito_id: int, db: Session = Depends(get_db)):
    favorito = db.query(FavoritoMl).filter(FavoritoMl.id == favorito_id).first()

    if not favorito:
        raise HTTPException(status_code=404, detail="Favorito não encontrado")

    db.delete(favorito)
    db.commit()

@app.post("/emprestimos", response_model=EmprestimoResponse, status_code=201)
def criar_emprestimo(emp: EmprestimoCreate, db: Session = Depends(get_db)):
    novo = Emprestimo(**emp.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


@app.get("/emprestimos", response_model=List[EmprestimoResponse])
def listar_emprestimos(db: Session = Depends(get_db)):
    return db.query(Emprestimo).all()


@app.get("/emprestimos/usuario/{usuario_id}", response_model=List[EmprestimoResponse])
def listar_por_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return db.query(Emprestimo).filter(Emprestimo.usuario_id == usuario_id).all()


@app.put("/emprestimos/{emp_id}", response_model=EmprestimoResponse)
def atualizar_emprestimo(emp_id: int, emp_model: EmprestimoUpdate, db: Session = Depends(get_db)):
    emp = db.query(Emprestimo).filter(Emprestimo.id == emp_id).first()

    if not emp:
        raise HTTPException(status_code=404, detail="Empréstimo não encontrado")

    dados = emp_model.model_dump(exclude_unset=True)
    for campo, valor in dados.items():
        setattr(emp, campo, valor)

    db.commit()
    db.refresh(emp)
    return emp


@app.delete("/emprestimos/{emp_id}", status_code=204)
def deletar_emprestimo(emp_id: int, db: Session = Depends(get_db)):
    emp = db.query(Emprestimo).filter(Emprestimo.id == emp_id).first()

    if not emp:
        raise HTTPException(status_code=404, detail="Empréstimo não encontrado")

    db.delete(emp)
    db.commit()