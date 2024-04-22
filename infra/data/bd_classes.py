import os
from passlib.hash import argon2
from dotenv import load_dotenv, set_key
from sqlalchemy import (
    create_engine,
    text,
    Column,
    Integer,
    String,
    Date,
    ForeignKey,
    Time,
    LargeBinary,
    Index,
    DateTime,
)
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.exc import OperationalError
from datetime import datetime
from typing import Dict
from copy import deepcopy

Base = declarative_base()
config_backup = None

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


class Cliente(Base):
    """Representa um cliente cadastrado no sistema através dos documentos.

    Atributos:
        id (int): Identificador único do cliente (chave primária).
        nome (str): Nome completo do cliente.
        cpf (str): Número de CPF do cliente.
        rg (str): Número de RG do cliente.
        filiacao (str): pai ou mae do cliente.
        estado (str): Estado em que o cliente está localizado.
        municipio (str): Cidade em que o cliente está localizado.
        endereco (str): Endereço do cliente.
        data_nascimento (Date): Data de nascimento do cliente.
        telefone (str, opcional): Número de telefone do cliente.
        email (str, opcional): Endereço de e-mail do cliente.

        documentos (relationship): Relacionamento com os documentos associado ao cliente.
    """

    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True)
    nome = Column(String(90), nullable=False)
    cpf = Column(String(13), nullable=False, unique=True)
    rg = Column(String(9), nullable=False, unique=True)
    filiacao = Column(String(90), nullable=False)
    municipio = Column(String(50), nullable=False)
    estado = Column(String(20), nullable=False)
    endereco = Column(String(120), nullable=False)
    data_nascimento = Column(Date, nullable=False)
    telefone = Column(String(15))
    email = Column(String)

    documentos = relationship("Documento", back_populates="cliente", cascade="all, delete")

    idx_cliente_id = Index("idx_cliente_id", id)
    idx_cliente_nome = Index("idx_cliente_nome", nome)
    idx_cliente_cpf = Index("idx_cliente_cpf", cpf)


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
    nome = Column(String(90), nullable=False)
    cpf = Column(String(13), nullable=False, unique=True)
    telefone = Column(String(15), nullable=False)
    email = Column(String, nullable=False, unique=True)
    senha = Column(String, nullable=False)

    sessoes = relationship("Sessao", back_populates="funcionario", cascade="all, delete")

    idx_funcionario_id = Index("idx_funcionario_id", id)
    idx_funcionario_nome = Index("idx_funcionario_nome", nome)
    idx_funcionario_cpf = Index("idx_funcionario_cpf", cpf)
    idx_funcionario_email = Index("idx_funcionario_email", email)

    def atualizar(
        self, nome: str = None, cpf: str = None, telefone: str = None, email: str = None
    ) -> None:
        """Atualiza os atributos do Funcionario.

        Args:
            nome (str, opcional): novo nome completo do funcionário.
            cpf (str, opcional): novo número de CPF do funcionário.
            telefone (str, opcional): novo número de telefone do funcionário.
            email (str, opcional): novo endereço de e-mail do funcionario.
        """
        if nome:
            self.nome = nome
        if cpf:
            self.cpf = cpf
        if telefone:
            self.telefone = telefone
        if email:
            self.email = email
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Erro ao atualizar funcionário: {e}")
        
    def atualizar_senha(self, nova_senha: str) -> None:
        """Atualiza somente a senha do Funcionário.

        Args:
            nova_senha (str): nova senha de login do funcionário.
        """
        self.senha = argon2.hash(nova_senha)
        print(nova_senha)
        try:
            session.commit()
            print(f"Senha atualizada.")
        except Exception as e:
            session.rollback()
            print(f"Erro ao atualizar senha: {e}")


class Registro(Base):
    """Representa uma atividade registrada durante uma sessão de um funcionário.

    Atributos:
        id (int): Identificador único do registro (chave primária).
        fk_sessao (int): Chave estrangeira que referencia a sessão associada ao registro.
        horario (DateTime): Timestamp em que a atividade foi registrada.
        titulo_atividade (str): Título da atividade registrada.

        sessao (relationship): Relacionamento com a sessão associada ao registro.
        documento (relationship): Relacionamento com o documento associado ao registro.
    """

    __tablename__ = "registro"

    id = Column(Integer, primary_key=True)
    fk_sessao = Column(Integer, ForeignKey("sessao.id"), nullable=False)
    horario = Column(DateTime, nullable=False)
    titulo_atividade = Column(String)

    sessao = relationship("Sessao", back_populates="registros")
    documento = relationship("Documento", back_populates="registro", cascade="all, delete")

    idx_registro_sessao = Index("idx_registro_sessao", fk_sessao)
    idx_registro_horario = Index("idx_registro_horario", horario)


class Documento(Base):
    """Representa um documento lido pelo sistema.

    Atributos:
        id (int): Identificador único do documento (chave primária).
        fk_cliente (int, opcional): Chave estrangeira que referencia um cliente (Caso haja um associado).
        fk_registro (int, opcional): Chave estrangeira que referencia o registro associado ao documento.
        titulo (str): Campo que representa o titulo específico para identificação do documento.
        tipo (str): Campo que representa o tipo específico do documento (ex: rg, cpf)
        conteudo (str): Conteúdo extraído do arquivo original.
        arquivo_original (LargeBinary): Representação binária do documento original.

        registro (relationship): Relacionamento com o registro associado ao documento.
        cliente (relationship): Relacionamento com o cliente associado ao documento.
    """

    __tablename__ = "documento"

    id = Column(Integer, primary_key=True)
    fk_registro = Column(Integer, ForeignKey("registro.id"))
    fk_cliente = Column(Integer, ForeignKey("cliente.id"))
    titulo = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    conteudo = Column(String, nullable=False)
    arquivo_original = Column(LargeBinary, nullable=False)

    registro = relationship("Registro", back_populates="documento")
    cliente = relationship("Cliente", back_populates="documentos")
    
    idx_documento_id = Index("idx_documento_id", id)
    idx_documento_titulo = Index("idx_documento_titulo", titulo)
    idx_documento_tipo = Index("idx_documento_tipo", tipo)
    idx_documento_cliente = Index("idx_documento_cliente", fk_cliente)


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

    idx_sessao_funcionario = Index("idx_sessao_funcionario", fk_funcionario)
    idx_sessao_data = Index("idx_sessao_data", data)


    def cadastrar_cliente(
        self,
        nome: str,
        cpf: str,
        rg: str,
        filiacao: str,
        estado: str,
        municipio: str,
        endereco: str,
        data_nascimento: str,
        telefone: str = None,
        email: str = None,
        ) -> Cliente:
        """Adiciona um Cliente ao Banco de Dados e cria um registro do mesmo.

        Args:
            nome (str): Nome completo do cliente.
            cpf (str): Número de CPF do cliente.
            rg (str): Número de RG do cliente.
            filiacao (str): Nome do pai ou mãe do cliente.
            estado (str): Estado em que o cliente está localizado.
            municipio (str): Cidade em que o cliente está localizado.
            endereco (str): Endereço do cliente.
            data_nascimento (str): Data de nascimento do cliente (formato dd-mm-aaaa).
            telefone (str, opcional): Número de telefone do cliente.
            email (str, opcional): Endereço de e-mail do cliente.

        Returns:
            Cliente: Objeto referente ao cliente criado.
        """

        novo_cliente = Cliente(
            nome=nome,
            cpf=cpf,
            rg=rg,
            filiacao=filiacao,
            estado=estado,
            municipio=municipio,
            endereco=endereco,
            data_nascimento=datetime.strptime(data_nascimento, "%d-%m-%Y"),
            telefone=telefone,
            email=email,
        )
        
        session.add(novo_cliente)

        try:
            session.commit()
            return novo_cliente
        except Exception as e:
            raise Exception(f"Erro ao cadastrar cliente: {e}")
    
    
    def salvar_documento(
        self, titulo: str, tipo: str, arquivo_original: bytes, conteudo: str, cliente: Cliente = None
        ) -> Documento:
        """Registra um documento no Banco de Dados a partir dos dados dessa sessão

        Args:
            titulo (str): Campo que representa o titulo específico para identificação do documento.
            tipo (str): Campo que representa o tipo específico do documento (ex: rg, cpf)
            arquivo_original (LargeBinary): Representação binária do documento original.
            conteudo (str): Conteúdo extraído do arquivo original.
            cliente (Cliente, opcional): Caso haja um cliente associado.

        Raises:
            Exception: Erro ao efetuar o commit do registro e documento.
        """

        titulo_registro = f"Salvou o documento '{titulo}'"
        if cliente:
            titulo_registro += f" de {cliente.nome}"

        # Criando Registro.
        registro = Registro(
            fk_sessao=self.id, horario=datetime.now(), titulo_atividade=titulo_registro
        )

        # Criando Documento.
        documento = Documento(
            fk_cliente=cliente.id if cliente else None,
            titulo=titulo,
            tipo=tipo,
            conteudo=conteudo,
            arquivo_original=arquivo_original,
        )

        documento.registro = registro

        session.add(documento)
        try:
            session.commit()
            return documento
        except Exception as e:
            raise Exception(f"Erro ao salvar documento: {e}")

def main():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    main()
