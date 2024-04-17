from PySide6 import QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QMessageBox,
    QTreeWidgetItem,
    QWidget,
)
from infra.data import gerenciamento
from infra.ui.ui_login import Ui_Form
from infra.ui.ui_sistema import Ui_MainWindow
import sys
from infra.func.ocr import TesseractOCR


class Login(QWidget, Ui_Form):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")

        self.btn_entrar_login.clicked.connect(self.abrir_sistema)
        self.btn_cadastrar_login.clicked.connect(self.mostrar_pag_cadastro)
        self.btn_config.clicked.connect(self.mostrar_pag_config)
        self.btn_closed.clicked.connect(self.close)
        self.btn_cadastrar.clicked.connect(self.cadastrar_usuario)

    def abrir_sistema(self):
        usuario = self.txt_cpf_login.text()
        senha = self.txt_senha_login.text()

        sessao = gerenciamento.iniciar_sessao(usuario, senha)

        if sessao:
            self.abrir_main_window(sessao)
        else:
            QMessageBox.information(self, "Login", "Usuário ou senha inválidos!")

    def validar_cpf(self, cpf):
        cpf = "".join(filter(str.isdigit, cpf))

        if len(cpf) != 11:
            return False

        if cpf == cpf[0] * 11:
            return False

        soma = sum(int(cpf[i]) * (10 - i) for i in range(9)) % 11
        digito_verif_1 = 0 if soma < 2 else 11 - soma

        if int(cpf[9]) != digito_verif_1:
            return False

        soma = sum(int(cpf[i]) * (11 - i) for i in range(10)) % 11
        digito_verif_2 = 0 if soma < 2 else 11 - soma

        if int(cpf[10]) != digito_verif_2:
            return False

        return True

    def validar_email(self, email):
        # Verifica se o e-mail possui um "@" e pelo menos um ponto após o "@"
        if "@" in email and "." in email[email.index("@") :]:
            return True
        else:
            return False

    def cadastrar_usuario(self):
        nome = self.txt_nome_cadastro.text()
        cpf = self.txt_cpf_cadastro.text()
        email = self.txt_email_cadastro.text()
        telefone = self.txt_telefone_cadastro.text()
        senha = self.txt_senha_cadastro.text()

        if email.lower() != "teste":
            if not self.validar_email(email):
                QMessageBox.warning(
                    self, "E-mail Inválido", "Por favor, insira um e-mail válido."
                )
                return

            if not self.validar_cpf(cpf):
                QMessageBox.warning(
                    self, "CPF Inválido", "Por favor, insira um CPF válido."
                )
                return

        gerenciamento.cadastro_funcionario(
            nome=nome, cpf=cpf, email=email, telefone=telefone, senha=senha
        )

        QMessageBox.information(self, "Cadastro", "Usuário cadastrado com sucesso!")
        self.limpar_campos_cadastro()

    def limpar_campos_cadastro(self):
        self.txt_nome_cadastro.clear()
        self.txt_cpf_cadastro.clear()
        self.txt_email_cadastro.clear()
        self.txt_telefone_cadastro.clear()
        self.txt_senha_cadastro.clear()

    def mostrar_pag_cadastro(self):
        self.Pages.setCurrentWidget(self.pg_cadastrar)

        # Conectar o botão de cadastrar ao método cadastrar_usuario
        self.btn_cadastrar.clicked.connect(self.cadastrar_usuario)

    def abrir_main_window(self, sessao):
        self.w = MainWindow(sessao)
        self.w.show()
        self.close()

    def mostrar_pag_cadastro(self):
        self.Pages.setCurrentWidget(self.pg_cadastrar)

    def mostrar_pag_config(self):
        self.Pages.setCurrentWidget(self.pg_config)

        configuracao = gerenciamento.obter_configuracao_banco()
        if configuracao:
            ip, porta = configuracao
            self.txt_ip.setText(ip)
            self.txt_porta.setText(porta)
        else:
            QMessageBox.information(
                self, "Configuração", "Configuração do banco de dados não encontrada!"
            )

    def salvar_configuracao(self):
        ip = self.txt_ip.text()
        porta = self.txt_porta.text()

        gerenciamento.atualizar_configuracao_banco(ip, porta)
        QMessageBox.information(
            self,
            "Configuração",
            "Configuração do banco de dados atualizada com sucesso!",
        )


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, sessao):
        super(MainWindow, self).__init__()
        self.sessao = sessao
        self.setupUi(self)
        self.setWindowTitle("Sistema de Cadastro de Áreas Remotas")
        self.btn_toogle.clicked.connect(self.left_menu)
        self.btn_home_menu.clicked.connect(self.mostrar_pag_home)
        self.btn_cadastrar_menu.clicked.connect(self.mostrar_pag_cadastro)
        self.btn_historico_menu.clicked.connect(self.mostrar_pag_historico)
        self.btn_enviar_menu.clicked.connect(self.mostrar_pag_enviar_doc)
        self.btn_perfil_menu.clicked.connect(self.mostrar_pag_perfil)
        self.btn_alterar_dados.clicked.connect(self.mostrar_pag_alteracao_perfil)
        self.btn_carregar_formulario.clicked.connect(self.abrir_arquivo)
        self.btn_encerrar_menu.clicked.connect(self.close)
        self.btn_arquivo_documento.clicked.connect(self.carregar_arquivo)
        self.btn_enviar_arquivo.clicked.connect(self.enviar_docs)

    def left_menu(self):
        width = self.menu.width()

        if width == 0:
            newWidth = 200
        else:
            newWidth = 0
        self.animation = QtCore.QPropertyAnimation(self.menu, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.animation.start()

    def mostrar_pag_home(self):
        self.Pages.setCurrentWidget(self.pg_home)

    ############################################################
    #########Página de envio de Documentos Genéricos############
    # Essas funções terão que permitir ao usuário escolher o tipo
    # do arquivo que vai enviar e ao clicar no botão de envio
    # esse documento subir para o banco.

    def mostrar_pag_enviar_doc(self):
        self.Pages.setCurrentWidget(self.pg_enviar_doc)

    def carregar_arquivo(self):
        options = QFileDialog.Option()
        nomeArquivo, _ = QFileDialog.getOpenFileName(
            self, "Selecione o Arquivo", "", "All Files(*)", options=options
        )

    def enviar_docs(self):
        print("Arquivo enviado com sucesso!")
        # btn_arquivo_documento
        # btn_enviar_arquivo
        # tipo_documento

    ##############################################################################
    #########Página de exibição de Perfil e alteração de Dados básicos############
    # Essas funções deverão permitir que ao usuário visualizar seus dados básico de
    # Perfil, que ele ao clicar no botão de alterar perfil a página de alteração
    # seja aberta e o usuário possa adicionar novos valores para os dados que quer
    # alterar. Ao clicar em salvar os dados serão atualizados no Banco de Dados.
    # Um ponto importante é que para exibir esses dados iniciais precisamos ter
    # um retorno do Banco com esses dados do usuário no momento que ele fizer login.

    def mostrar_pag_perfil(self):
        sessao = self.sessao

        if sessao:
            informacoes = sessao.funcionario
            if informacoes:
                self.txt_nome_perfil.setText(informacoes.nome)
                self.txt_email_perfil.setText(informacoes.email)
                self.txt_telefone_perfil.setText(informacoes.telefone)
                self.Pages.setCurrentWidget(self.pg_perfil)
            else:
                QMessageBox.information(
                    self, "Perfil", "Informações do usuário não encontradas!"
                )
        else:
            QMessageBox.information(
                self, "Perfil", "Sessão inválida! Faça login novamente."
            )

    def mostrar_pag_alteracao_perfil(self):
        self.Pages.setCurrentWidget(self.pg_alteracao_perfil)
        # txt_perfil_alterar_nome
        # txt_perfil_alterar_email
        # txt_perfil_alterar_telefone
        # btn_salvar_alteracoes

    #############################################################################
    ############ Página de Cadastro de Cliente ##################################
    # Essas funções devem permitir que o usuário carregue o arquivo digitalizado
    # e que esse arquivo extraia as informações para preenchimento do formulário
    # e mostre na tela. Os campos são editávei pois quando o usuário verificar
    # que precisa melhorar alguma informação ele terá essa facilidade. Outra
    # função importante é a parte de selecionar documentos que serão anexados ao
    # cadastro como CNH, RG, etc. Os documentos vão aparecer na lista que fica na
    # tela para que ao final o usuário possa visualizar tanto o formulário
    # preenchido quanto os arquivo selecionados. Ao clicar em enviar cadastro o
    # sistema enviará para o banco a criação daquele cadastro e vinculação dos
    # documentos àquele cliente.

    def mostrar_pag_cadastro(self):
        self.Pages.setCurrentWidget(self.pg_cadastrar)

    def carregar_docs_cadastro(self):
        # btn_carregar_documentos
        # lista_documentos_cadastro
        # btn_cadastro_enviar
        pass

    def abrir_arquivo(self):
        options = QFileDialog.Option()
        nomeArquivo, _ = QFileDialog.getOpenFileName(
            self, "Selecione o Arquivo", "", "All Files(*)", options=options
        )
        if nomeArquivo:
            print("Arquivo selecionado", nomeArquivo)
            texto = TesseractOCR().read_text(nomeArquivo)
            image = TesseractOCR().read_image(nomeArquivo)
            json = TesseractOCR().read_json(texto)
            print(json)
            self.txt_cadastro_nome.setText(json.get("nome", ""))
            self.txt_cadastro_cpf.setText(json.get("cpf", ""))
            self.txt_cadastro_rg.setText(json.get("rg", ""))
            self.txt_cadastro_filiacao.setText(json.get("filiacao", ""))
            self.txt_cadastro_nascimento.setText(json.get("nascimento", ""))
            self.txt_cadastro_endereco.setText(json.get("endereco", ""))
            self.txt_cadastro_cidade.setText(json.get("cidade", ""))
            self.txt_cadastro_estado.setText(json.get("estado", ""))
            self.txt_cadastro_telefone.setText(json.get("telefone", ""))
            self.txt_cadastro_email.setText(json.get("email", ""))

    #################################################################################
    ################## Página de Exibição do Histórico ##############################
    # Essas funções tratarão da exibição do histórico de cadastros realizados por
    # aquele usuário. Portanto teremos a necessidade de funções que busquem um SELECT
    # no BD com os cadastros daquele usuário.

    def mostrar_pag_historico(self):
        self.Pages.setCurrentWidget(self.pg_historico)


def main():
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
