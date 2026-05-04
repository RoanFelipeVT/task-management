import os
import pytest
from sqlalchemy import create_engine, text # Import 'text' adicionado
from sqlalchemy.orm import sessionmaker
from alembic.config import Config
from alembic import command

# Define o arquivo de ambiente antes de importar o settings
os.environ["ENV_FILE"] = ".env.test"
from src.core.config import settings

# Configuração do Engine de Teste
engine = create_engine(settings.DATABASE_URL)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """
    Prepara o banco de dados uma vez por sessão de testes.
    """
    alembic_cfg = Config("alembic.ini")
    
    
    with engine.connect() as conn:
        conn.execute(text("DROP SCHEMA public CASCADE; CREATE SCHEMA public;"))
        conn.commit()
    
    
    command.upgrade(alembic_cfg, "head")
    
    yield


@pytest.fixture
def db_session():
    """
    Cria uma sessão de banco de dados isolada por função de teste.
    Tudo que for feito aqui sofrerá rollback ao final do teste.
    """
    connection = engine.connect()
    transaction = connection.begin()

    
    db = TestingSessionLocal(bind=connection)

    try:
        yield db
    finally:
        db.close()
        transaction.rollback() 
        connection.close() 