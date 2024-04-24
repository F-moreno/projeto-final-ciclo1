import os
from dotenv import load_dotenv, set_key
from sqlalchemy import (
    create_engine,
    text,
)
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.exc import OperationalError
from typing import Dict
from copy import deepcopy
from infra.data.entidades import *

Base = declarative_base()
config_backup = None
session = None
engine = None

load_dotenv()
config = {
    "db_user": os.getenv("DB_USER"),
    "db_pass": os.getenv("DB_PASS"),
    "db_host": os.getenv("DB_HOST"),
    "db_port": os.getenv("DB_PORT"),
    "db_name": os.getenv("DB_NAME"),
}

# CONFIGURAÇÕES BD
def set_config(
    db_user: str = None,
    db_pass: str = None,
    db_host: str = None,
    db_port: str = None,
    db_name: str = None,
) -> None:
    """Altera as configurações do servidor e banco de dados no arquivo .env.
    Reconecta ao banco automaticamente.
    restaura as configurações anteriores caso haja algum erro ao reconectar ao banco de dados.
    Use importlib.reload(gerenciamento) caso haja algum problema em gerenciamento.py

    Args:
        db_user (str): nome de usuário para acessar o servidor.
        db_pass (str): senha do servidor.
        db_host (str): ip do servidor ("localhost" para rodar localmente).
        db_port (str): porta do servidor (None quando rodando localmente).
        db_name (str): nome do banco de dados.
    
    Returns:
        bool:
            True: se a configuração for efetuada corretamente e o banco se conectar com sucesso.
            False: se houver erro ao salvar a configuração ou ao se conectar com o banco.
    """
    global config
    global config_backup
    config_backup = deepcopy(get_config())

    session.close()

    try:
        dotenv_path = ".env"  # Caminho para o arquivo '.env'

        if db_user:
            set_key(dotenv_path, "DB_USER", db_user)
            config["db_user"] = db_user
        if db_pass:
            set_key(dotenv_path, "DB_PASS", db_pass)
            config["db_pass"] = db_pass
        if db_host:
            set_key(dotenv_path, "DB_HOST", db_host)
            config["db_host"] = db_host
        if db_port:
            set_key(dotenv_path, "DB_PORT", db_port)
            config["db_port"] = db_port
        if db_name:
            set_key(dotenv_path, "DB_NAME", db_name)
            config["db_name"] = db_name

        return connect_bd()
    
    except Exception as e:
        set_key(dotenv_path, "DB_USER", config_backup["db_user"])
        set_key(dotenv_path, "DB_PASS", config_backup["db_pass"])
        set_key(dotenv_path, "DB_HOST", config_backup["db_host"])
        set_key(dotenv_path, "DB_PORT", config_backup["db_port"])
        set_key(dotenv_path, "DB_NAME", config_backup["db_name"])
        config["db_user"] = config_backup["db_user"]
        config["db_pass"] = config_backup["db_pass"]
        config["db_host"] = config_backup["db_host"]
        config["db_port"] = config_backup["db_port"]
        config["db_name"] = config_backup["db_name"]
        print(f"Erro ao alterar configurações. Backup das configurações realizado: {e}")
        return False

def get_config() -> Dict[str, str]:
    """Retorna as configurações atuais do servidor e banco de dados escritas no arquivo '.env'

    Returns:
        Dict[str, str]: dicionário com as configurações:
            db_user (str): nome de usuário para acessar o servidor.
            db_pass (str): senha do servidor.
            db_host (str): ip do servidor ("localhost" para rodar localmente).
            db_port (str): porta do servidor (None quando rodando localmente).
            db_name (str): nome do banco de dados.
    """
    config_dict_str = deepcopy(config)
    config_dict_str["db_port"] = config_dict_str["db_port"]
    return config_dict_str


def connect_bd() -> bool:
    """Verifica a existência do banco de dados no servidor configurado no
    arquivo '.env'. Se existir, tenta conectar no mesmo, senão, cria e tenta
    conectar novamente.

    Returns:
        bool:
            True: se conectar com sucesso.
            False: se houver erro ao conectar.
            
    raises:
        Exception: Erro ao conectar Banco de Dados.
    """
    config_atual = get_config()
    db_user = config_atual["db_user"]
    db_pass = config_atual["db_pass"]
    db_host = config_atual["db_host"]
    db_port = int(config_atual["db_port"]) if config_atual["db_port"] else ""
    db_name = config_atual["db_name"]

    try:
        global Session
        global session
        global engine

        # Usando POSTGRESQL
        # Verificando existência do Banco de Dados do projeto
        engine = create_engine(
            f'postgresql://{db_user}:{db_pass}@{db_host}{f":{db_port}" if db_port else ""}/postgres'
        )
        conn = engine.connect()
        result = conn.execute(
            text(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{db_name}';")
        )
        conn.close()

        if not result.scalar():
            print(
                f"Banco de Dados não encontrado - Criando Banco de Dados '{db_name}'."
            )
            try:
                # Criando banco caso ainda não exista
                with engine.connect() as connection:
                    connection.execution_options(isolation_level="AUTOCOMMIT").execute(
                        text(f"CREATE DATABASE {db_name};")
                    )
                print(f"Banco de Dados '{db_name}' criado com sucesso.")

            except OperationalError as e:
                print(f"Erro ao criar Banco de Dados '{db_name}': {e}")

        # Conectando ao Banco de Dados do projeto
        engine = create_engine(
            f'postgresql://{db_user}:{db_pass}@{db_host}{f":{db_port}" if db_port else ""}/{db_name}'
        )
        Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
        session = Session()
        Base.metadata.create_all(engine)
        print(f"Conectado ao Banco de Dados '{db_name}' com sucesso.")
        return True
    
    except Exception as e:
        raise Exception(f"Erro ao conectar Banco de Dados '{db_name}': {e}")

connect_bd()
