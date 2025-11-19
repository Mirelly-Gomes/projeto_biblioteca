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
    livro_id = Column(Integer, ForeignKey("livros.id"), nullable=False)
    usuario_id =Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    alunos = relationship("Livro", back_populates="livros")
    usuarios = relationship("Usuario", back_populates="usuarios") 

class Editora(Base):
    __tablename__= "editoras"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)

class Autor(Base):
    __tablename__= "autores"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)

class Emprestimo(Base):
    __tablename__= "emprestimos"
    id = Column(Integer, primary_key=True, index=True)
    livro_id = Column(Integer, ForeignKey("livros.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    data_retirada = Column(Date, index=True)
    data_devolucao = Column(Date, index=True)

    alunos = relationship("Livro", back_populates="livros")
    usuarios = relationship("Usuario", back_populates="usuarios") 


class Usuario(Base):
    __tablename__= "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True , nullable=False)
    email = Column(String, index=True, unique=True , nullable=False)
    senha =Column(String, index=True, nullable=False)

class Livro(Base):
    __tablename__= "livros"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True, nullable=False)
    autor_id = Column(Integer, ForeignKey("autores.id"), nullable=False)
    editora_id = Column(Integer, ForeignKey("editoras.id"), nullable=False)

    autores = relationship("Autor", back_populates="autores")
    editoras = relationship("Editora", back_populates="editoras") 




   


