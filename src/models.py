# src/models.py
# Neste arquivo, definimos as classes que representam nossas tabelas do banco de dados.

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base  # Importamos a Base declarativa do nosso arquivo database.py

# Modelo para a tabela FILME
class Filme(Base):
    __tablename__ = "filme"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    ano = Column(Integer, nullable=False)
    diretor = Column(String(100), nullable=False)
    genero = Column(String(50), nullable=False)
    sinopse = Column(Text, nullable=False)
    classificacao = Column(Integer, nullable=False)
    duracao = Column(Integer, nullable=False)
    pais = Column(String(50), nullable=False)

    # Relacionamentos com outras tabelas
    reviews = relationship("Review", back_populates="filme")
    favoritos = relationship("Favorito", back_populates="filme")

# Modelo para a tabela USERS
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True, index=True)
    senha = Column(String(100), nullable=False)
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())

    # Relacionamentos com outras tabelas
    reviews = relationship("Review", back_populates="usuario")
    favoritos = relationship("Favorito", back_populates="usuario")

# Modelo para a tabela REVIEWS
class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    filme_id = Column(Integer, ForeignKey("filme.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    avaliacao = Column(Integer, nullable=False)
    comentario = Column(Text, nullable=True)
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())
    
    # Adicionando o check constraint
    __table_args__ = (
        CheckConstraint('avaliacao >= 1 AND avaliacao <= 5', name='check_avaliacao_range'),
    )

    # Relacionamentos para facilitar o acesso aos objetos Filme e User
    filme = relationship("Filme", back_populates="reviews")
    usuario = relationship("User", back_populates="reviews")

# Modelo para a tabela FAVORITOS
class Favorito(Base):
    __tablename__ = "favoritos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    filme_id = Column(Integer, ForeignKey("filme.id"), nullable=False)
    data_adicao = Column(DateTime(timezone=True), server_default=func.now())

    # Relacionamentos
    usuario = relationship("User", back_populates="favoritos")
    filme = relationship("Filme", back_populates="favoritos")

# --------------------------------------------------------------------------------------
