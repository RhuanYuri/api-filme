# src/schemas.py

from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

# Schema para criação de usuário (o que a API recebe)
class UserCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str

# Schema para resposta de usuário (o que a API retorna)
# NUNCA retorne a senha!
class UserResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr
    data_criacao: datetime

    class Config:
        orm_mode = True # Permite que o Pydantic leia dados de um objeto ORM


class UserLogin(BaseModel):
    email: EmailStr
    senha: str        


class UserResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr
    data_criacao: datetime

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    senha: str

# --- SCHEMAS PARA FILMES (ADICIONADO) ---
class FilmeBase(BaseModel):
    titulo: str
    ano: int
    diretor: str
    genero: str
    sinopse: str
    classificacao: int
    duracao: int
    pais: str

class FilmeCreate(FilmeBase):
    pass

class FilmeResponse(FilmeBase):
    id: int

    class Config:
        orm_mode = True    

class ReviewBase(BaseModel):
    avaliacao: int = Field(..., ge=1, le=5, description="Avaliação de 1 a 5 estrelas")
    comentario: str | None = None

class ReviewCreate(ReviewBase):
    filme_id: int
    usuario_id: int # Em uma app simplificada, o cliente envia. Numa real, viria do token de auth.

class ReviewResponse(ReviewBase):
    id: int
    filme_id: int
    usuario_id: int
    data_criacao: datetime

    class Config:
        orm_mode = True

class FavoritoBase(BaseModel):
    usuario_id: int
    filme_id: int

class FavoritoCreate(FavoritoBase):
    pass

class FavoritoResponse(FavoritoBase):
    id: int
    data_adicao: datetime

    class Config:
        orm_mode = True
