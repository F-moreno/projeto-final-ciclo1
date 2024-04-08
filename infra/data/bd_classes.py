import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Time, LargeBinary
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

load_dotenv()

db_usuario = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_path = os.getenv("DB_PATH")

# Using POSTGRESQL
engine = create_engine(f"postgresql+psycopg2://{db_usuario}:{db_pass}@{db_path}")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Cliente(Base):
    """Representa um cliente cadastrado no sistema através dos documentos.
    
    Atributos:
        id (int): Identificador único do cliente (chave primária).
        nome (str): Nome completo do cliente.
        cpf (str): Número de CPF do cliente.
        rg (str): Número de RG do cliente.
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
    endereco = Column(String, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    telefone = Column(String)
    email = Column(String)
    
    
    
class Funcionario(Base):
    """Representa um funcionário autorizado a utilizar o sistema.
    
    Atributos:
        id (int): Identificador único do funcionário (chave primária).
        nome (str): Nome completo do funcionário.
        cpf (str): Número de CPF do funcionário.
        rg (str): Número de RG do funcionário.
        endereco (str): Endereço do funcionário.
        telefone (str): Número de telefone do funcionário.
        senha (str): Senha de login do funcionário.
        email (str): Endereço de e-mail do funcionario.
        data_nascimento (Date): Data de nascimento do funcionario.
        
        sessoes (relationship): Relacionamento com as sessões do funcionário.
    """
    __tablename__ = "funcionario"
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    rg = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    senha = Column(String, nullable=False)
    data_nascimento = Column(Date)
    
    sessoes = relationship("Sessao", back_populates="funcionario")
    
    
class Sessao(Base):
    """Representa uma sessão de login de um funcionário no sistema.
    
    Atributos:
        id (int): Identificador único da sessão (chave primária).
        fk_funcionario (int): Chave estrangeira que referencia o funcionário da sessão.
        Data (Date): Data da sessão.
        inicio (Time): Hora de início da sessão.
        fim (Time): Hora de fim da sessão.
        
        funcionario (relationship): Relacionamento com o funcionário da sessão.
        registros (relationship): Relacionamento com os registros da sessão.
    """
    __tablename__ = "sessao"
    
    id = Column(Integer, primary_key=True)
    fk_funcionario = Column(Integer, ForeignKey("funcionario.id"), nullable=False)
    Data = Column(Date, nullable=False)
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
        conteudo (int): ID do documento associado à atividade.
        
        sessao (relationship): Relacionamento com a sessão associada ao registro.
        documento (relationship): Relacionamento com o documento associado ao registro.
    """
    __tablename__ = "registro"
    
    id = Column(Integer, primary_key=True)
    fk_sessao = Column(Integer, ForeignKey("sessao.id"), nullable=False)
    horario = Column(Time, nullable=False)
    titulo_atividade = Column(String)
    conteudo = Column(Integer, ForeignKey("documento.id"))
    
    sessao = relationship("Sessao", back_populates="registros")
    documento = relationship("Documento", back_populates="registro")


class Documento(Base):
    """Indica um documento digitalizado pelo sistema.
    
    Atributos:
        id (int): Identificador único do documento (chave primária).
        digitalizado (str): Caminho do arquivo digitalizado.
        original (LargeBinary): Representação binária do documento original.
        
        registro (relationship): Relacionamento com o registro associado ao documento.
    """
    __tablename__ = "documento"
    
    id = Column(Integer, primary_key=True)
    digitalizado = Column(String)
    original = Column(LargeBinary)
    
    registro = relationship("Registro", back_populates="documento")
    

if __name__ == "__main__":
    Base.metadata.create_all(engine)