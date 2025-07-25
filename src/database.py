# src/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# --- ALTERAÇÃO AQUI ---
# Em vez de importar de um arquivo de configuração, definimos a URL diretamente.
SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"
# --------------------

# O resto do arquivo permanece exatamente o mesmo.

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,  # Usamos a variável definida acima
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()