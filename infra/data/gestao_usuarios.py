from bd_classes import session, Cliente, Funcionario, Sessao
from datetime import datetime
from passlib.hash import argon2


# GESTÃO DE USUARIOS

def cadastro_cliente(nome:str,
                     cpf:str,
                     rg:str,
                     filiacao:str,
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
        filiacao (str): Nome do pai ou mãe do cliente
        endereco (str): Endereço do cliente.
        data_nascimento (str, dd-mm-aaaa): Data de nascimento do cliente.
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
