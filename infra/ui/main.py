from PySide6 import QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QFileDialog, QMainWindow, QMessageBox, QTreeWidgetItem, QWidget)
from ui_login import Ui_Form
import sys

class Login(QWidget, Ui_Form):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")
        
        #self.btn_entrar_login.clicked(self)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()