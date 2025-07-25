
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas
from ..database import SessionLocal

router = APIRouter(
    prefix="/reviews",
    tags=["Reviews"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ReviewResponse)
def criar_review(review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    """
    Cria uma nova review para um filme, garantindo que o filme e o usuário existam.
    """
    # Verifica se o filme existe
    filme = db.query(models.Filme).filter(models.Filme.id == review.filme_id).first()
    if not filme:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Filme com id {review.filme_id} não encontrado.")

    # Verifica se o usuário existe
    usuario = db.query(models.User).filter(models.User.id == review.usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuário com id {review.usuario_id} não encontrado.")

    # Verifica se o usuário já avaliou este filme
    review_existente = db.query(models.Review).filter(
        models.Review.filme_id == review.filme_id,
        models.Review.usuario_id == review.usuario_id
    ).first()

    if review_existente:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Este usuário já avaliou o filme.")

    nova_review = models.Review(**review.dict())
    db.add(nova_review)
    db.commit()
    db.refresh(nova_review)
    return nova_review

@router.get("/filme/{filme_id}", response_model=List[schemas.ReviewResponse])
def listar_reviews_por_filme(filme_id: int, db: Session = Depends(get_db)):
    """
    Retorna todas as reviews de um filme específico.
    """
    reviews = db.query(models.Review).filter(models.Review.filme_id == filme_id).all()
    return reviews

@router.delete("/{review_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_review(review_id: int, db: Session = Depends(get_db)):
    """
    Remove uma review pelo seu ID.
    (Numa aplicação real, você deveria verificar se o usuário autenticado é o dono da review)
    """
    review_query = db.query(models.Review).filter(models.Review.id == review_id)
    review = review_query.first()

    if not review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review não encontrada.")
    
    review_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
