
from contextlib import asynccontextmanager
from fastapi import FastAPI
from . import models
from .database import engine

#Controllers
import src.routers.filme as filme
import src.routers.user as user
import src.routers.review as review
import src.routers.favoritos as favoritos

# --- ALTERAÇÃO AQUI: Usando o 'lifespan' do FastAPI ---
# Esta é a forma recomendada para executar código na inicialização e no encerramento.
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Iniciando a API... Verificando e criando tabelas do banco de dados.")
    # O SQLAlchemy irá criar todas as tabelas associadas à Base (se não existirem)
    models.Base.metadata.create_all(bind=engine)
    yield
    print("Encerrando a API...")

app = FastAPI(
    lifespan=lifespan, # Adicionamos o gerenciador de ciclo de vida à nossa aplicação
    title="API de Filmes",
    description="Uma API para gerenciar e avaliar filmes.",
    version="1.0.0"
)

app.include_router(filme.router)
app.include_router(user.router)
app.include_router(review.router)
app.include_router(favoritos.router)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Filmes! As tabelas do banco de dados foram verificadas/criadas com sucesso."}
