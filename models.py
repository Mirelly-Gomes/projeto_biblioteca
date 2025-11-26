from sqlalchemy import Column, Integer, String, ForeignKey, Table, Date
from sqlalchemy.orm import relationship
from database import Base


class Admin(Base):
    __tablename__= "admin"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)
    email = Column(String, index=True, unique=True, nullable=False)
    senha = Column(String, index=True, nullable=False)

   
class Favorito(Base):
    __tablename__= "favoritos"
    id = Column(Integer, primary_key=True , nullable=False)
    livro_id = Column(Integer, ForeignKey("livros.id"), nullable=False)
    usuario_id =Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    livros = relationship("Livro", back_populates="favoritos")
    usuarios = relationship("Usuario", back_populates="favoritos") 

class Editora(Base):
    __tablename__= "editoras"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)

    livros  = relationship("Livro", back_populates="editoras")

class Autor(Base):
    __tablename__= "autores"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)

    livros  = relationship("Livro", back_populates="autores")

class Emprestimo(Base):
    __tablename__= "emprestimos"
    id = Column(Integer, primary_key=True, index=True)
    livro_id = Column(Integer, ForeignKey("livros.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    data_retirada = Column(Date, index=True)
    data_devolucao = Column(Date, index=True)

    livros = relationship("Livro", back_populates="emprestimos")
    usuarios = relationship("Usuario", back_populates="emprestimos") 
    



class Usuario(Base):
    __tablename__= "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True , nullable=False)
    email = Column(String, index=True, unique=True , nullable=False)
    senha =Column(String, index=True, nullable=False)

    favoritos =  relationship("Favorito", back_populates="usuarios")
    emprestimos = relationship("Emprestimo", back_populates="usuarios")


class Livro(Base):
    __tablename__= "livros"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True, nullable=False)
    autor_id = Column(Integer, ForeignKey("autores.id"), nullable=False)
    editora_id = Column(Integer, ForeignKey("editoras.id"), nullable=False)

    autores = relationship("Autor", back_populates="livros")
    editoras = relationship("Editora", back_populates="livros")
    favoritos =  relationship("Favorito", back_populates="livros")
    emprestimos = relationship("Emprestimo", back_populates="livros")




   


