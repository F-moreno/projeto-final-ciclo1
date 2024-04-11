from PySide6 import QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QFileDialog, QMainWindow, QMessageBox, QTreeWidgetItem, QWidget)
from ui_login import Ui_Form
from ui_sistema import Ui_MainWindow
import sys

class Login(QWidget, Ui_Form):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")
        
        self.btn_entrar_login.clicked.connect(self.abrir_sistema)
        
    #Parte de teste na fase de criação da tela principal
    def abrir_sistema(self):
        
        if self.txt_senha_login.text() == '1234':
            self.w = MainWindow()
            self.w.show()
            self.close()
            
        else:
            print('senha inválida')
        
class MainWindow(QMainWindow, Ui_MainWindow):
        def __init__(self):
            super(MainWindow,self).__init__()
            self.setupUi(self)
            self.setWindowTitle("Sistema de Cadastro de Áreas Remotas")
            
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()