from pydantic import BaseModel
from typing import Optional, List
from datetime import date

# admin

class AdminCreate(BaseModel):
    nome: str
    email: str
    senha: str

class AdminUpdate(BaseModel):
    nome: Optional[str] = None
    senha: Optional[str] = None

class AdminResponse(BaseModel):
    id: int
    nome: str
    email: str
    senha: str

    class Config:
        from_attributes = True

# fav e Editora

class Favorito(BaseModel):
    livro_id: int
    usuario_id: int

class EditoraCreate(BaseModel):
    nome: str

class EditoraUpdate(BaseModel):
    nome: Optional[str] = None

class EditoraResponse(BaseModel):
    id: int
    nome: str

    class Config:
        from_attributes = True


# autor 

class AutorCreate(BaseModel):
    nome: str

class AutorUpdate(BaseModel):
    nome: Optional[str] = None
 
class AutorResponse(BaseModel):
    id: int
    nome: str

    class Config:
        from_attributes = True

# emprestimo 

class EmprestimoCreate(BaseModel):
    livro_id: int
    usuario_id: int
    data_retirada: date 
    data_devolucao: date

class EmprestimoUpdate(BaseModel):
    data_retirada: Optional[date] = None   
    data_devolucao: Optional[date] = None

class EmprestimoResponse(BaseModel):
    livro_id: int
    usuario_id: int
    data_retirada: str  
    data_devolucao: str

    class Config:
        from_attributes = True

# usuario

class UsuarioCreate(BaseModel):
    nome: str
    email: str
    senha: str

class UsuarioUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    senha: Optional[str] = None

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str
    senha: str

    class Config:
        from_attributes = True

#livro

class LivroCreate(BaseModel):
    titulo: str
    autor_id: int
    editora_id: int


class LivroUpdate(BaseModel):
     titulo: Optional[str] = None

class LivroResponse(BaseModel):
    id: int
    titulo: str
    autor_id: int
    editora_id: int

    class Config:
        from_attributes = True