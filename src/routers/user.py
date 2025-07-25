
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session



from .. import models, schemas
from ..database import SessionLocal

# Cria uma instância do APIRouter
router = APIRouter(
    prefix="/user",  # Adiciona um prefixo a todas as rotas neste arquivo
    tags=["Usuário"]    # Agrupa as rotas na documentação interativa (Swagger UI)
)

# Dependência para obter a sessão do banco de dados a cada requisição
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def register_user(body: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Registra um novo usuário no banco de dados.
    """
    # Verifica se o e-mail já existe
    user_exists = db.query(models.User).filter(models.User.email == body.email).first()
    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Usuário com o e-mail '{body.email}' já existe."
        )
    
    # Cria a nova instância do usuário para o banco de dados
    new_user = models.User(
        nome=body.nome,
        email=body.email,
        senha=body.senha  # Salva a senha com hash
    )

    # Adiciona, comita e atualiza
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Retorna os dados do novo usuário (usando o schema de resposta, que não inclui a senha)
    return new_user


@router.post("/login", response_model=schemas.UserResponse)
def login(login_data: schemas.UserLogin, db: Session = Depends(get_db)):
    """
    Metodo para autenticar um usuário.
    Recebe o e-mail e a senha, verifica se o usuário existe e se a senha está correta.
    Retorna os dados do usuário se a autenticação for bem-sucedida.
    """
    # 1. Busca o usuário pelo e-mail
    user = db.query(models.User).filter(models.User.email == login_data.email).first()

    # 2. Verifica se o usuário existe e se a senha (em texto puro) corresponde
    if not user or not (user.senha == login_data.senha):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="E-mail ou senha incorretos."
        )

    # 3. Se tudo estiver correto, retorna os dados do usuário.
    # Em uma app real, aqui você geraria um token.
    return user