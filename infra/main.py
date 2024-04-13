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
        self.btn_cadastrar_login.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_cadastrar)
        )
        self.btn_config.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_config)
        )
        self.btn_closed.clicked.connect(self.close)

    # Parte de teste na fase de criação da tela principal
    def abrir_sistema(self):

        if self.txt_senha_login.text() == "1234":
            self.w = MainWindow()
            self.w.show()
            self.close()

        else:
            print("senha inválida")


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Cadastro de Áreas Remotas")
        self.btn_toogle.clicked.connect(self.LeftMenu)
        self.btn_home_menu.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_home)
        )
        self.btn_cadastrar_menu.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_cadastrar)
        )
        self.btn_historico_menu.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_historico)
        )
        self.btn_enviar_menu.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_enviar_doc)
        )
        self.btn_perfil_menu.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_perfil)
        )
        self.btn_alterar_dados.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_alteracao_perfil)
        )
        self.btn_carregar_formulario.clicked.connect(self.AbrirArquivo)
        self.btn_encerrar_menu.clicked.connect(self.close)

    def LeftMenu(self):
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

    def AbrirArquivo(self):
        options = QFileDialog.Option()
        nomeArquivo, _ = QFileDialog.getOpenFileName(
            self, "Selecione o Arquivo", "", "All Files(*)", options=options
        )
        if nomeArquivo:
            print("Arquivo selecionado", nomeArquivo)
            texto = TesseractOCR().read_text(nomeArquivo)
            image = TesseractOCR().read_image(nomeArquivo)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()
