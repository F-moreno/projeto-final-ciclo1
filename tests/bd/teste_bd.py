import importlib
from infra.data.gerenciamento import func_bd
from infra.data.entidades import session
from infra.data.gerenciamento.config_bd import get_config, set_config
import cv2
import numpy as np
import io

"""POSSÍVEIS SOLUÇÕES

- Verifique se está na ambiente virtual do projeto poetry (Use "poetry shell" no terminal);
- Verifique se todas as dependências estão instaladas (Use "poetry install" no terminal);
- Verifique se possui o arquivo '.env' com as configurações do seu servidor postgres;
- Verifique se suas tabelas estão atualizadas.

"""


def main():
    deletar_registros_teste = True

    print(get_config())

    set_config(db_name="bd_projeto")
    importlib.reload(func_bd)

    # Teste gerenciamento.cadastro_funcionario().
    try:
        funcionario = func_bd.cadastro_funcionario(
            "Funcionario Teste",
            "12345678912",
            "93988149930",
            "funcionarioteste@gmail.com",
            "teste123",
        )
        print("cadastro_funcionario(): OK")
        funcionario.atualizar_senha("teste1234")
        print(funcionario.senha)

    except Exception as e:
        print(f"ERRO EM 'gerenciamento.cadastro_funcionario()': {e}")

    # Teste gerenciamento.iniciar_sessao().
    try:
        sessao = func_bd.iniciar_sessao("12345678912", "teste1234")

        print("iniciar_sessao(): OK")
    except Exception as e:
        print(f"ERRO EM 'gerenciamento.iniciar_sessao()': {e}")

    # Teste gerenciamento.cadastro_cliente().
    try:
        cliente = sessao.cadastrar_cliente(
            "Cliente Teste",
            "12345678912",
            "1234567",
            "Pai/Mãe Teste",
            "Estado Teste",
            "Municipio Teste",
            "Endereço Teste",
            "30-05-2005",
            "99999999999",
            "clienteteste@gmail.com",
        )
        print("cadastro_cliente(): OK")
    except Exception as e:
        print(f"ERRO EM 'gerenciamento.cadastro_cliente()': {e}")

    # Teste gerenciamento.get_clientes().
    try:
        clientes = func_bd.get_clientes(nome="Cliente Teste")
        clientes = func_bd.get_clientes()
        clientes = func_bd.get_clientes(cpf="12345678912")
        clientes = func_bd.get_clientes(id=cliente.id)
        clientes = func_bd.get_clientes(
            nome="Cliente Teste", cpf="12345678912", id=cliente.id
        )

        print("get_clientes(): OK")
    except Exception as e:
        print(f"ERRO EM 'gerenciamento.get_clientes()': {e}")

    # Teste gerenciamento.get_funcionarios().
    try:
        funcionarios = func_bd.get_funcionarios(nome="Funcionario Teste")
        funcionarios = func_bd.get_funcionarios(cpf="12345678912")
        funcionarios = func_bd.get_funcionarios(email="funcionarioteste@gmail.com")
        print(funcionarios[0].email)
        funcionarios = func_bd.get_funcionarios(id=funcionario.id)
        funcionarios = func_bd.get_funcionarios(
            nome="Funcionario Teste", cpf="12345678912", id=funcionario.id
        )

        funcionarios[0].atualizar(nome="RAFAEL")  # Teste Funcionario.atualizar

        print("get_funcionarios(): OK")
    except Exception as e:
        print(f"ERRO EM 'gerenciamento.get_funcionarios()': {e}")

    # Teste bd_classes.Sessao.salvar_documento()
    try:
        with io.open("tests/bd/img/imagem_teste.jpeg", "rb") as f:
            bytes_imagem = f.read()

        documento = sessao.salvar_documento(
            titulo="AAA",
            tipo="Teste",
            arquivo_original=bytes_imagem,
            conteudo="Teste teste teste",
            cliente=cliente,
        )

        print("salvar_documento(): OK")
    except Exception as e:
        print(f"ERRO EM 'bd_classes.Sessao.salvar_documento()': {e}")

    # Testando get_documentos()
    try:
        documentos = func_bd.get_documentos(id=documento.id)
        documentos = func_bd.get_documentos(fk_cliente=cliente.id)
        documentos = func_bd.get_documentos(tipo="Teste")
        documentos = func_bd.get_documentos(
            id=documento.id, fk_cliente=cliente.id, tipo="Teste"
        )
        documentos = func_bd.get_documentos(
            fk_funcionario=sessao.funcionario.id, tipo="Teste"
        )

        if documentos:
            for documento in documentos:
                print(documento.tipo)
                print(documento.registro.sessao.funcionario.id)

        imagem_numpy = np.frombuffer(documentos[0].arquivo_original, np.uint8)
        imagem_decodificada = cv2.imdecode(imagem_numpy, cv2.IMREAD_COLOR)

        cv2.imshow("Minha Imagem", imagem_decodificada)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print(f"get_documentos': OK")
    except Exception as e:
        print(f"ERRO EM 'gerenciamento.get_documentos()': {e}")

    # Teste gerenciamento.get_registros()
    try:
        # Buscar todos os registros do dia 13 de abril de 2024
        registros = func_bd.get_registros(dia="13-04-2024")
        # Buscar todos os registros da sessão "1"
        registros = func_bd.get_registros(fk_sessao=1)
        # Buscar registro específico (id = 10)
        registros = func_bd.get_registros(id=1)
        # Buscar todos os registros de abril de 2024 (id = 10)
        registros = func_bd.get_registros(mes="04-2024")
        # Buscar todos os registros de 2024
        registros = func_bd.get_registros(ano="2024")
        print("get_registros(): OK")
    except Exception as e:
        print(f"ERRO EM 'gerenciamento.get_registros': {e}")

    # Teste gerenciamento.get_sessoes()
    try:
        # Buscar todas as sessões do dia 13 de abril de 2024
        sessoes = func_bd.get_sessoes(dia="13-04-2024")
        # Buscar todas as sessões do funcionário "1"
        sessoes = func_bd.get_sessoes(fk_funcionario=1)
        # Buscar sessão específica (id = 10)
        sessoes = func_bd.get_sessoes(id=1)
        # Buscar todas as sessões de abril de 2024 (id = 10)
        sessoes = func_bd.get_sessoes(mes="04-2024")
        # Buscar todas as sessões de 2024
        sessoes = func_bd.get_sessoes(ano="2024")
        print("get_sessoes(): OK")
    except Exception as e:
        print(f"ERRO EM 'gerenciamento.get_sessoes': {e}")

    func_bd.encerrar_sessao(sessao)
    if deletar_registros_teste:
        try:
            # Deleção de registros de teste
            func_bd.session.delete(documento.registro)
            func_bd.session.delete(sessao)
            func_bd.session.delete(funcionario)
            func_bd.session.delete(documento)
            func_bd.session.delete(cliente)
            func_bd.session.commit()
            print("Registros Deletados: OK")
        except Exception as e:
            print(f"ERRO AO DELETAR REGISTROS': {e}")
