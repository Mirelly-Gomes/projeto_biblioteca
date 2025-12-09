#  Biblioteca Digital — API FastAPI  
### *Projeto de Conclusão*

Este projeto é uma **API completa para gerenciamento de uma biblioteca**, desenvolvida como **trabalho de conclusão**, utilizando FastAPI e SQLAlchemy. A aplicação permite controlar usuários, livros, autores, editoras, favoritos e empréstimos.

---

##  Tecnologias Utilizadas
- **FastAPI**
- **SQLAlchemy ORM**
- **Pydantic v2**
- **Uvicorn**
- **PostgreSQL**

---

##  Funcionalidades
- **Usuários:** CRUD completo  
- **Livros:** cadastro, edição e remoção  
- **Autores e Editoras:** gerenciamento básico  
- **Favoritos:** vincular livros ao usuário  
- **Empréstimos:** registrar retirada e devolução  

---

##  Como Executar o Projeto

```bash
git clone https://github.com/.../projeto_biblioteca.git
cd projeto_biblioteca

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt

uvicorn main:app --reload
