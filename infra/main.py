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
from data import gerenciamento
from ui.ui_login import Ui_Form
from ui.ui_sistema import Ui_MainWindow
import sys
from func.ocr import TesseractOCR


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
        usuario = self.txt_email_login.text()
        senha = self.txt_senha_login.text()

        sessao = gerenciamento.iniciar_sessao(usuario, senha)

        if sessao:
            self.abrir_main_window()
        else:
            QMessageBox.information(self, "Login", "Usuário ou senha inválidos!")

    def cadastrar_usuario(self):
        nome = self.txt_nome_cadastro.text()
        cpf = self.txt_cpf_cadastro.text()
        email = self.txt_email_cadastro.text()
        telefone = self.txt_telefone_cadastro.text()
        senha = self.txt_senha_cadastro.text()

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

    def abrir_main_window(self):
        self.w = MainWindow()
        self.w.show()
        self.close()

    def mostrar_pag_cadastro(self):
        self.Pages.setCurrentWidget(self.pg_cadastrar)

    def mostrar_pag_config(self):
        self.Pages.setCurrentWidget(self.pg_config)
        # txt_ip
        # txt_porta
        # btn_padrao
        # btn_salvar_config


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
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

        if width == 9:
            newWidth = 200
        else:
            newWidth = 9
        self.animation = QtCore.QPropertyAnimation(self.menu, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.animation.start()

    def mostrar_pag_home(self):
        self.Pages.setCurrentWidget(self.pg_home)

    def mostrar_pag_cadastro(self):
        self.Pages.setCurrentWidget(self.pg_cadastrar)

    def mostrar_pag_historico(self):
        self.Pages.setCurrentWidget(self.pg_historico)

    ############################################################
    #########Página de envio de Documentos Genéricos############
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

    #####################################################################

    def mostrar_pag_perfil(self):
        self.Pages.setCurrentWidget(self.pg_perfil)

    def mostrar_pag_alteracao_perfil(self):
        self.Pages.setCurrentWidget(self.pg_alteracao_perfil)
        # txt_perfil_alterar_nome
        # txt_perfil_alterar_email
        # txt_perfil_alterar_telefone
        # btn_salvar_alteracoes

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
            self.txt_cadastro_nome.setText(json["nome"])
            self.txt_cadastro_cpf.setText(json["cpf"])
            self.txt_cadastro_rg.setText(json["rg"])
            self.txt_cadastro_filiacao.setText(json["filiacao"])
            self.txt_cadastro_nascimento.setText(json["nascimento"])
            self.txt_cadastro_endereco.setText(json["endereco"])
            self.txt_cadastro_cidade.setText(json["cidade"])
            self.txt_cadastro_estado.setText(json["estado"])
            self.txt_cadastro_telefone.setText(json["telefone"])
            self.txt_cadastro_email.setText(json["email"])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()
