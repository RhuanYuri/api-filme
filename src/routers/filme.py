
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas
from ..database import SessionLocal

router = APIRouter(
    prefix="/filmes",
    tags=["Filmes"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.FilmeResponse)
def adicionar_filme(filme: schemas.FilmeCreate, db: Session = Depends(get_db)):
    """
    Adiciona um novo filme ao banco de dados.
    """
    novo_filme = models.Filme(**filme.dict())
    db.add(novo_filme)
    db.commit()
    db.refresh(novo_filme)
    return novo_filme

@router.get("/", response_model=List[schemas.FilmeResponse])
def listar_todos_os_filmes(db: Session = Depends(get_db)):
    """
    Retorna uma lista de todos os filmes cadastrados.
    """
    filmes = db.query(models.Filme).all()
    return filmes

@router.get("/{filme_id}", response_model=schemas.FilmeResponse)
def obter_detalhes_do_filme(filme_id: int, db: Session = Depends(get_db)):
    """
    Obtém os detalhes de um filme específico pelo ID.
    """
    filme = db.query(models.Filme).filter(models.Filme.id == filme_id).first()
    if not filme:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Filme não encontrado")
    return filme

@router.put("/{filme_id}", response_model=schemas.FilmeResponse)
def atualizar_filme(filme_id: int, filme_atualizado: schemas.FilmeCreate, db: Session = Depends(get_db)):
    """
    Atualiza os detalhes de um filme específico pelo ID.
    """
    filme_query = db.query(models.Filme).filter(models.Filme.id == filme_id)
    filme_existente = filme_query.first()

    if not filme_existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Filme não encontrado")

    filme_query.update(filme_atualizado.dict(), synchronize_session=False)
    db.commit()
    return filme_query.first()

@router.delete("/{filme_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_filme(filme_id: int, db: Session = Depends(get_db)):
    """
    Remove um filme específico pelo ID.
    """
    filme_query = db.query(models.Filme).filter(models.Filme.id == filme_id)
    filme = filme_query.first()

    if not filme:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Filme não encontrado")

    filme_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
