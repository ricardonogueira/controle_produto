from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from banco_dados.conexao import db

class Produto(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str]
    preco: Mapped[float]
    quantidade: Mapped[int]
    foto: Mapped[str]

    def __repr__(self):
        return f'<Produto {self.id} - {self.nome} - {self.preco} >'