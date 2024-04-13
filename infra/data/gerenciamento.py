from sqlalchemy import func
from bd_classes import session, Cliente, Funcionario, Sessao, Registro
from datetime import datetime
from dateutil import relativedelta
from passlib.hash import argon2
from typing import List

# GESTÃO DE USUARIOS

def cadastro_cliente(nome:str,
                     cpf:str,
                     rg:str,
                     filiacao:str,
                     estado:str,
                     municipio:str,
                     endereco:str,
                     data_nascimento:str,
                     telefone:str=None,
                     email:str=None
                     ) -> Cliente:
    """Adiciona um Cliente ao Banco de Dados.

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
                    email=email
                    )
    
    session.add(novo_cliente)

    try:
        session.commit()
        return novo_cliente
    except Exception as e:
        print(f"Erro ao cadastrar cliente: {e}")
    

def cadastro_funcionario(nome:str, cpf:str, telefone:str, email:str, senha:str) -> Funcionario:
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
                        nome=nome,
                        cpf=cpf,
                        telefone=telefone,
                        email=email,
                        senha=argon2.hash(senha)
                        )
    
    session.add(novo_funcionario)

    try:
        session.commit()
        return novo_funcionario
    except Exception as e:
        print(f"Erro ao cadastrar funcionario: {e}")


# GERENCIAMENTO DE SESSÃO

def iniciar_sessao(cpf:str, senha:str) -> Sessao:
    """Seleciona uma Funcionario do Banco de Dados a partir do cpf do funcionário e senha.
    Além disso, cria uma instância de sessão com a data e horário atual.

    Args:
        cpf (str): Cpf do funcionario, informado pelo utilizador.
        senha (str): Senha do funcionario referente ao cpf inserido.

    Returns:
        Sessao: Objeto referente à sessão iniciada
    """
    funcionario = session.query(Funcionario).filter_by(cpf=cpf).first() # Selecionando funcionario
    if funcionario and argon2.verify(senha, funcionario.senha):
        
        sessao = Sessao(fk_funcionario=funcionario.id, # Criando sessão
                        data=datetime.date(datetime.now()),
                        inicio=datetime.time(datetime.now())
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
        sessao (Sessao): Registro de sessão do funcionario retornado pela função iniciar_sessao().
    """
    sessao.fim = datetime.time(datetime.now())
    
    try:
        session.commit()
    except Exception as e:
        raise Exception(f"Erro ao registrar fim de sessão: {e}")
    

# CONSULTAS

def get_clientes(id:int=None,
                nome:str=None,
                cpf:str=None,
                ) -> List[Cliente]:
    """Retorna uma lista de Clientes com base nos argumentos.
    OBS: Se não houver argumentos, retorna todos os clientes.

    Args:
        id (int, opcional): filtrar por id único de um cliente.
        nome (str, opcional): filtrar por nome completo do cliente.
        cpf (str, opcional): filtrar por número de CPF do cliente.

    Returns:
        List[Cliente]: Uma lista de Clientes que coincidem com os argumentos.
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
        print(f"Erro ao procurar Cliente: {e}")


def get_registros(id: int = None,
                  fk_sessao: int = None,
                  dia: str = None,
                  mes: str = None,
                  ano: str = None,
                  ) -> List[Registro]:
    """Retorna uma lista de Registros com base nos argumentos.
    OBS: Se não houver argumentos, retorna todos os registros.

    Args:
        id (int, opcional): filtrar por id único do registro.
        fk_sessao (int, opcional): filtrar por id de uma sessão específica.
        dia (str, opcional): filtrar por dia específico (formato dd-mm-aaaa).
        mes (str, opcional): filtrar por mês específico (formato mm-aaaa).
        ano (str, opcional): filtrar por ano específico (formato aaaa).

    Returns:
        List[Registro]: Lista de registros filtrados.
    """

    kwargs = {}
    if id:
        kwargs["id"] = id

    if fk_sessao:
        kwargs["fk_sessao"] = fk_sessao

    # Condições de filtro (filtragem vazia se nenhum argumento for válido)
    filtros = []
    
    if dia and datetime.strptime(dia, "%d-%m-%Y").date() is not None:
        filtros.append(func.date(Registro.horario) == datetime.strptime(dia, "%d-%m-%Y").date())

    if mes:
        # Manter a filtragem por mês e ano específicos (se for o caso)
        data_inicio = datetime.strptime("01-"+mes, "%d-%m-%Y").date()
        data_fim = data_inicio + relativedelta.relativedelta(months=+1, day=1) - relativedelta.relativedelta(days=1)
        filtros.append(func.date(Registro.horario) >= data_inicio)
        filtros.append(func.date(Registro.horario) < data_fim)
        
    if ano:
        data_inicio = datetime.strptime("01-01-"+ano, "%d-%m-%Y").date()
        data_fim = datetime.strptime("31-12-"+ano, "%d-%m-%Y").date()
        filtros.append(func.date(Registro.horario) >= data_inicio)
        filtros.append(func.date(Registro.horario) <= data_fim)

    # Construir a consulta
    try:
        registros = session.query(Registro).filter_by(**kwargs)
        if filtros:
            registros = registros.filter(*filtros) 
        return registros.all()
    except Exception as e:
        print(f"Erro ao procurar Registro: {e}")
        
