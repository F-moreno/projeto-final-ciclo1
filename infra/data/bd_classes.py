import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text, Column, Integer, String, Date, ForeignKey, Time, LargeBinary
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.exc import OperationalError

load_dotenv()

try:
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASS")
    db_host = os.getenv("DB_HOST")
    db_name = "bd_projeto"
except Exception as e:
    raise Exception(f"Erro ao carregar as configurações do '.env': {e}")

# Usando POSTGRESQL
# Verificando existência do Banco de Dados do projeto
engine = create_engine(f'postgresql://{db_user}:{db_pass}@{db_host}/postgres')
conn = engine.connect()
result = conn.execute(text(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{db_name}';"))
conn.close()

if not result.scalar():
    print(f"Banco de Dados não encontrado - Criando Banco de Dados '{db_name}'.")
    try:
        # Criando banco caso ainda não exista
        with engine.connect() as connection:
            connection.execution_options(isolation_level="AUTOCOMMIT").execute(text(f"CREATE DATABASE {db_name};"))
        print(f"Banco de Dados '{db_name}' criado com sucesso.")
        
    except OperationalError as e:
        raise Exception(f"Erro ao criar Banco de Dados '{db_name}': {e}")

# Conectando ao Banco de Dados do projeto
engine = create_engine(f'postgresql://{db_user}:{db_pass}@{db_host}/{db_name}')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
print(f"Conectado ao Banco de Dados '{db_name}' com sucesso")

class Cliente(Base):
    """Representa um cliente cadastrado no sistema através dos documentos.
    
    Atributos:
        id (int): Identificador único do cliente (chave primária).
        nome (str): Nome completo do cliente.
        cpf (str): Número de CPF do cliente.
        rg (str): Número de RG do cliente.
        filiacao (str): pai ou mae do cliente.
        endereco (str): Endereço do cliente.
        data_nascimento (Date): Data de nascimento do cliente.
        telefone (str, opcional): Número de telefone do cliente.
        email (str, opcional): Endereço de e-mail do cliente.
    """
    __tablename__ = "cliente"
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    rg = Column(String, nullable=False)
    filiacao = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    telefone = Column(String)
    email = Column(String)
    
    documentos = relationship("Documento", back_populates="cliente")
    
    
    
class Funcionario(Base):
    """Representa um funcionário autorizado a utilizar o sistema.
    
    Atributos:
        id (int): Identificador único do funcionário (chave primária).
        nome (str): Nome completo do funcionário.
        cpf (str): Número de CPF do funcionário.
        telefone (str): Número de telefone do funcionário.
        email (str): Endereço de e-mail do funcionario.
        senha (str): Senha de login do funcionário.

        
        sessoes (relationship): Relacionamento com as sessões do funcionário.
    """
    __tablename__ = "funcionario"
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    senha = Column(String, nullable=False)
    
    sessoes = relationship("Sessao", back_populates="funcionario")
    
    
class Sessao(Base):
    """Representa uma sessão de login de um funcionário no sistema.
    
    Atributos:
        id (int): Identificador único da sessão (chave primária).
        fk_funcionario (int): Chave estrangeira que referencia o funcionário da sessão.
        data (Date): Data da sessão.
        inicio (Time): Hora de início da sessão.
        fim (Time, opcional): Hora de fim da sessão.
        
        funcionario (relationship): Relacionamento com o funcionário da sessão.
        registros (relationship): Relacionamento com os registros da sessão.
    """
    __tablename__ = "sessao"
    
    id = Column(Integer, primary_key=True)
    fk_funcionario = Column(Integer, ForeignKey("funcionario.id"), nullable=False)
    data = Column(Date, nullable=False)
    inicio = Column(Time, nullable=False)
    fim = Column(Time)
    
    funcionario = relationship("Funcionario", back_populates="sessoes")
    registros = relationship("Registro", back_populates="sessao")
    

class Registro(Base):
    """Representa uma atividade registrada durante uma sessão de um funcionário.
    
    Atributos:
        id (int): Identificador único do registro (chave primária).
        fk_sessao (int): Chave estrangeira que referencia a sessão associada ao registro.
        horario (Time): Horário em que a atividade foi registrada.
        titulo_atividade (str): Título da atividade registrada.
        fk_documento (int, opcional): ID do documento associado à atividade.
        
        sessao (relationship): Relacionamento com a sessão associada ao registro.
        documento (relationship): Relacionamento com o documento associado ao registro.
    """
    __tablename__ = "registro"
    
    id = Column(Integer, primary_key=True)
    fk_sessao = Column(Integer, ForeignKey("sessao.id"), nullable=False)
    horario = Column(Time, nullable=False)
    titulo_atividade = Column(String)
    fk_documento = Column(Integer, ForeignKey("documento.id"))
    
    sessao = relationship("Sessao", back_populates="registros")
    documento = relationship("Documento", back_populates="registro")


class Documento(Base):
    """Indica um documento lido pelo sistema.
    
    Atributos:
        id (int): Identificador único do documento (chave primária).
        fk_cliente (int, opcional): Chave estrangeira que referencia um cliente (Caso haja um associado).
        tipo (str): Campo que representa o tipo específico do documento (ex: rg, cpf)
        conteudo (str): Conteúdo extraído do arquivo original.
        original (LargeBinary): Representação binária do documento original.
        
        registro (relationship): Relacionamento com o registro associado ao documento.
    """
    __tablename__ = "documento"
    
    id = Column(Integer, primary_key=True)
    fk_cliente = Column(Integer, ForeignKey("cliente.id"))
    tipo = Column(String, nullable=False)
    conteudo = Column(String, nullable=False)
    arquivo_original = Column(LargeBinary, nullable=False)
    
    registro = relationship("Registro", back_populates="documento")
    cliente = relationship("Cliente", back_populates="documentos")
    

if __name__ == "__main__":
    
    Base.metadata.create_all(engine)