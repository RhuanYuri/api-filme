
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas
from ..database import SessionLocal

router = APIRouter(
    prefix="/favoritos",
    tags=["Favoritos"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.FavoritoResponse)
def adicionar_favorito(favorito: schemas.FavoritoCreate, db: Session = Depends(get_db)):
    """
    Adiciona um filme à lista de favoritos de um usuário.
    """
    # Verifica se o filme e o usuário existem
    filme = db.query(models.Filme).filter(models.Filme.id == favorito.filme_id).first()
    if not filme:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Filme não encontrado.")
    
    usuario = db.query(models.User).filter(models.User.id == favorito.usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado.")

    # Verifica se o filme já foi favoritado por este usuário
    favorito_existente = db.query(models.Favorito).filter(
        models.Favorito.filme_id == favorito.filme_id,
        models.Favorito.usuario_id == favorito.usuario_id
    ).first()
    if favorito_existente:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Filme já está na lista de favoritos.")

    novo_favorito = models.Favorito(**favorito.dict())
    db.add(novo_favorito)
    db.commit()
    db.refresh(novo_favorito)
    return novo_favorito

@router.get("/usuario/{usuario_id}", response_model=List[schemas.FavoritoResponse])
def listar_favoritos_do_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """
    Lista todos os filmes favoritos de um usuário específico.
    """
    favoritos = db.query(models.Favorito).filter(models.Favorito.usuario_id == usuario_id).all()
    return favoritos

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def remover_favorito(favorito: schemas.FavoritoCreate, db: Session = Depends(get_db)):
    """
    Remove um filme da lista de favoritos de um usuário.
    """
    favorito_query = db.query(models.Favorito).filter(
        models.Favorito.usuario_id == favorito.usuario_id,
        models.Favorito.filme_id == favorito.filme_id
    )
    
    favorito_db = favorito_query.first()

    if not favorito_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Favorito não encontrado.")
    
    favorito_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)