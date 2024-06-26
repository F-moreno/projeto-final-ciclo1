from sqlalchemy import func
from infra.data.entidades import (
    session,
    Cliente,
    Funcionario,
    Sessao,
    Registro,
    Documento,
    argon2
)
from datetime import datetime
from dateutil import relativedelta
from typing import List

# GESTÃO DE USUARIOS

def cadastro_funcionario(
    nome: str, cpf: str, telefone: str, email: str, senha: str
) -> Funcionario:
    """Adiciona um Funcionario ao Banco de Dados.

    Args:
        nome (str): Nome completo do funcionário.
        cpf (str): Número de CPF do funcionário.
        telefone (str): Número de telefone do funcionário.
        email (str): Endereço de e-mail do funcionario.
        senha (str): Senha de login do funcionário.

    Returns:
        Funcionario: Objeto referente ao funcionario criado.
    """
    novo_funcionario = Funcionario(
        nome=nome, cpf=cpf, telefone=telefone, email=email, senha=argon2.hash(senha)
    )

    session.add(novo_funcionario)

    try:
        session.commit()
        return novo_funcionario
    except Exception as e:
        raise Exception(f"Erro ao cadastrar funcionario: {e}")

# GERENCIAMENTO DE SESSÃO

def iniciar_sessao(cpf: str, senha: str) -> Sessao:
    """Seleciona um Funcionario do Banco de Dados a partir do cpf do funcionário e senha.
    Além disso, cria uma instância de sessão com a data e horário atual.

    Args:
        cpf (str): Cpf do funcionario, informado pelo utilizador.
        senha (str): Senha do funcionario referente ao cpf inserido.

    Returns:
        Sessao: Objeto referente à sessão iniciada
    """
    funcionario = (
        session.query(Funcionario).filter_by(cpf=cpf).first()
    )  # Selecionando funcionario
    if funcionario and argon2.verify(senha, funcionario.senha):

        sessao = Sessao(
            fk_funcionario=funcionario.id,  # Criando sessão
            data=datetime.date(datetime.now()),
            inicio=datetime.time(datetime.now()),
        )

        session.add(sessao)

        try:
            session.commit()
        except Exception as e:
            raise Exception(f"Erro ao registrar início de sessão: {e}")

        return sessao
    else:
        raise Exception("usuario ou senha incorretos")


def encerrar_sessao(sessao: Sessao):
    """Atualiza a sessão, registrando o horário de fim no Banco de Dados.

    Args:
        sessao (Sessao): Objeto referente à sessão retornada por iniciar_sessao().
    """
    sessao.fim = datetime.time(datetime.now())

    try:
        session.commit()
    except Exception as e:
        raise Exception(f"Erro ao registrar fim de sessão: {e}")

# CONSULTAS

def get_clientes(
    id: int = None,
    nome: str = None,
    cpf: str = None,
) -> List[Cliente]:
    """Retorna uma lista de clientes com base nos argumentos.
    OBS: Se não houver argumentos, retorna todos os clientes.

    Args:
        id (int, opcional): filtrar por id único de um cliente.
        nome (str, opcional): filtrar por nome completo do cliente.
        cpf (str, opcional): filtrar por número de CPF do cliente.

    Returns:
        List[Cliente]: lista de clientes filtrados.
    """
    kwargs = {}
    if id:
        kwargs["id"] = id

    if nome:
        kwargs["nome"] = nome

    if cpf:
        kwargs["cpf"] = cpf

    try:
        clientes = session.query(Cliente).filter_by(**kwargs)
        return clientes.all()
    except Exception as e:
        raise Exception(f"Erro ao procurar Clientes: {e}")


def get_funcionarios(
    id: int = None,
    nome: str = None,
    cpf: str = None,
    email: str = None,
) -> List[Funcionario]:
    """Retorna uma lista de funcionários com base nos argumentos.
    OBS: Se não houver argumentos, retorna todos os funcionários.

    Args:
        id (int, opcional): filtrar por id único de um funcionário.
        nome (str, opcional): filtrar por nome completo do funcionário.
        cpf (str, opcional): filtrar por número de CPF do funcionário.
        email (str, opcional): filtrar por email do funcionário.

    Returns:
        List[Funcionario]: lista de funcionários filtrados.
    """
    kwargs = {}
    if id:
        kwargs["id"] = id

    if nome:
        kwargs["nome"] = nome

    if cpf:
        kwargs["cpf"] = cpf
    
    if email:
        kwargs["email"] = email

    try:
        funcionarios = session.query(Funcionario).filter_by(**kwargs)
        return funcionarios.all()
    except Exception as e:
        raise Exception(f"Erro ao procurar Funcionários: {e}")


def get_registros(
    id: int = None,
    fk_sessao: int = None,
    dia: str = None,
    mes: str = None,
    ano: str = None,
) -> List[Registro]:
    """Retorna uma lista de registros com base nos argumentos.
    OBS: Se não houver argumentos, retorna todos os registros.

    Args:
        id (int, opcional): filtrar por id único do registro.
        fk_sessao (int, opcional): filtrar por id de uma sessão específica.
        dia (str, opcional): filtrar por dia específico (formato dd-mm-aaaa).
        mes (str, opcional): filtrar por mês específico (formato mm-aaaa).
        ano (str, opcional): filtrar por ano específico (formato aaaa).

    Returns:
        List[Registro]: lista de registros filtrados.
    """

    kwargs = {}
    if id:
        kwargs["id"] = id

    if fk_sessao:
        kwargs["fk_sessao"] = fk_sessao

    # Condições de filtro (filtragem vazia se nenhum argumento for válido)
    filtros = []

    if dia and datetime.strptime(dia, "%d-%m-%Y").date() is not None:
        filtros.append(
            func.date(Registro.horario) == datetime.strptime(dia, "%d-%m-%Y").date()
        )

    if mes:
        data_inicio = datetime.strptime("01-" + mes, "%d-%m-%Y").date()
        data_fim = (
            data_inicio
            + relativedelta.relativedelta(months=+1, day=1)
            - relativedelta.relativedelta(days=1)
        )
        filtros.append(func.date(Registro.horario) >= data_inicio)
        filtros.append(func.date(Registro.horario) < data_fim)

    if ano:
        data_inicio = datetime.strptime("01-01-" + ano, "%d-%m-%Y").date()
        data_fim = datetime.strptime("31-12-" + ano, "%d-%m-%Y").date()
        filtros.append(func.date(Registro.horario) >= data_inicio)
        filtros.append(func.date(Registro.horario) <= data_fim)

    # Construir a consulta
    try:
        registros = session.query(Registro).filter_by(**kwargs)
        if filtros:
            registros = registros.filter(*filtros)
        return registros.all()
    except Exception as e:
        raise Exception(f"Erro ao procurar Registros: {e}")


def get_sessoes(
    id: int = None,
    fk_funcionario: int = None,
    dia: str = None,
    mes: str = None,
    ano: str = None,
) -> List[Sessao]:
    """Retorna uma lista de sessões com base nos argumentos.
    OBS: Se não houver argumentos, retorna todas as sessões.

    Args:
        id (int, opcional): filtrar por id único da sessão.
        fk_funcionario (int, opcional): filtrar por id de um funcionário específico.
        dia (str, opcional): filtrar por dia específico (formato dd-mm-aaaa).
        mes (str, opcional): filtrar por mês específico (formato mm-aaaa).
        ano (str, opcional): filtrar por ano específico (formato aaaa).

    Returns:
        List[Sessao]: lista de sessões filtradas.
    """

    kwargs = {}
    if id:
        kwargs["id"] = id

    if fk_funcionario:
        kwargs["fk_funcionario"] = fk_funcionario

    # Condições de filtro (filtragem vazia se nenhum argumento for válido)
    filtros = []

    if dia and datetime.strptime(dia, "%d-%m-%Y").date() is not None:
        filtros.append(
            func.date(Sessao.data) == datetime.strptime(dia, "%d-%m-%Y").date()
        )

    if mes:
        data_inicio = datetime.strptime("01-" + mes, "%d-%m-%Y").date()
        data_fim = (
            data_inicio
            + relativedelta.relativedelta(months=+1, day=1)
            - relativedelta.relativedelta(days=1)
        )
        filtros.append(func.date(Sessao.data) >= data_inicio)
        filtros.append(func.date(Sessao.data) < data_fim)

    if ano:
        data_inicio = datetime.strptime("01-01-" + ano, "%d-%m-%Y").date()
        data_fim = datetime.strptime("31-12-" + ano, "%d-%m-%Y").date()
        filtros.append(func.date(Sessao.data) >= data_inicio)
        filtros.append(func.date(Sessao.data) <= data_fim)

    # Construir a consulta
    try:
        sessoes = session.query(Sessao).filter_by(**kwargs)
        if filtros:
            sessoes = sessoes.filter(*filtros)
        return sessoes.all()
    except Exception as e:
        raise Exception(f"Erro ao procurar Sessões: {e}")


def get_documentos(
    id: int = None,
    fk_funcionario: int = None,
    fk_cliente: int = None,
    titulo: str = None,
    tipo: str = None,
    ) -> List[Documento]:
    """Retorna uma lista de documentos com base nos argumentos.
    OBS: Se não houver argumentos, retorna todos os documentos.

    Args:
        id (int, opcional): filtrar por id único de um documento.
        fk_cliente (int, opcional): filtrar por id de um cliente específico.
        fk_funcionario (int, opcional): filtrar por id do funcionário que enviou o documento.
        titulo (str, opcional): Campo que representa o titulo específico para identificação do documento.
        tipo (str, opcional): filtrar por tipo de documento.

    Returns:
        List[Documento]: lista de documentos filtrados.
    """
    kwargs = {}
            
    if id:
        kwargs["id"] = id

    if fk_cliente:
        kwargs["fk_cliente"] = fk_cliente

    if tipo:
        kwargs["tipo"] = tipo
    
    if titulo:
        kwargs["titulo"] = titulo

    try:
        documentos = session.query(Documento).filter_by(**kwargs)
        
        if fk_funcionario:
            documentos = documentos.join(Registro) \
            .join(Sessao) \
            .join(Funcionario) \
            .filter(Funcionario.id == fk_funcionario)
            
        return documentos.all()
    except Exception as e:
        raise Exception(f"Erro ao procurar Documentos: {e}")
