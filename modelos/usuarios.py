from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from banco_dados.conexao import db

class Usuario(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    usuario: Mapped[str]
    senha: Mapped[float]
    
    def __repr__(self):
        return f'<Usuario {self.id} - {self.usuario} >'