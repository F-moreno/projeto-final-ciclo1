# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
from PySide6 import QtCore
from infra.ui import icons_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(784, 536)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setStyleSheet(u"QWidget {\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.login_h = QWidget(Form)
        self.login_h.setObjectName(u"login_h")
        self.login_h.setGeometry(QRect(99, 149, 591, 331))
        self.login_h.setStyleSheet(u"QWidget {\n"
"background-color: white;\n"
"color: black;\n"
"border-radius: 20px;\n"
"\n"
"}")
        self.verticalLayout = QVBoxLayout(self.login_h)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.login_h_2 = QWidget(self.login_h)
        self.login_h_2.setObjectName(u"login_h_2")
        self.login_h_2.setStyleSheet(u"QWidget {\n"
"background-color: qlineargradient(spread:pad, x1:0.465, y1:0.481682, x2:0, y2:0, stop:0.147727 rgba(0, 164, 218, 255), stop:0.931818 rgba(0, 219, 255, 255));\n"
"border-radius: 10px;\n"
"color: black;\n"
"\n"
"}")
        self.Pages = QStackedWidget(self.login_h_2)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setGeometry(QRect(9, -1, 311, 291))
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.pg_home.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"	color: black;\n"
"	border-radius: 20px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.pg_home)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.pg_home)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"background-color: qlineargradient(spread:pad, x1:0.465, y1:0.481682, x2:0, y2:0, stop:0.147727 rgba(0, 164, 218, 255), stop:0.931818 rgba(0, 219, 255, 255));\n"
"border-radius: 0px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lbl_nome_empresa = QLabel(self.frame)
        self.lbl_nome_empresa.setObjectName(u"lbl_nome_empresa")
        self.lbl_nome_empresa.setGeometry(QRect(50, 130, 271, 41))
        font = QFont()
        font.setFamilies([u"Tempus Sans ITC"])
        font.setPointSize(30)
        font.setBold(True)
        self.lbl_nome_empresa.setFont(font)
        self.lbl_nome_empresa.setStyleSheet(u"QLabel {\n"
"	font-family: Tempus Sans ITC;\n"
"	background-color: transparent;\n"
"	font-size: 30pt;\n"
"	color: white;\n"
"	font-weight: 600;\n"
"}")

        self.verticalLayout_2.addWidget(self.frame)

        self.Pages.addWidget(self.pg_home)
        self.pg_cadastrar = QWidget()
        self.pg_cadastrar.setObjectName(u"pg_cadastrar")
        self.pg_cadastrar.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"	color: black;\n"
"}")
        self.frame_4 = QFrame(self.pg_cadastrar)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, -1, 311, 301))
        self.frame_4.setStyleSheet(u"QFrame {\n"
"background-color: qlineargradient(spread:pad, x1:0.465, y1:0.481682, x2:0, y2:0, stop:0.147727 rgba(0, 164, 218, 255), stop:0.931818 rgba(0, 219, 255, 255));\n"
"border-radius: 0px;\n"
"color: black;\n"
"\n"
"}")
        
       
        
        
        self.txt_nome_cadastro = QLineEdit(self.frame_4)
        self.txt_nome_cadastro.setObjectName(u"txt_nome_cadastro")
        self.txt_nome_cadastro.setGeometry(QRect(80, 60, 211, 25))
        self.txt_nome_cadastro.setMinimumSize(QSize(0, 25))
        self.txt_nome_cadastro.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(0,0,0,25);\n"
"	color: white;\n"
"	border-radius: 6px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}")
        self.txt_cpf_cadastro = QLineEdit(self.frame_4)
        self.txt_cpf_cadastro.setObjectName(u"txt_cpf_cadastro")
        self.txt_cpf_cadastro.setGeometry(QRect(80, 90, 211, 25))
        self.txt_cpf_cadastro.setMinimumSize(QSize(0, 25))
        self.txt_cpf_cadastro.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(0,0,0,25);\n"
"	color: white;\n"
"	border-radius: 6px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}")
        self.txt_email_cadastro = QLineEdit(self.frame_4)
        self.txt_email_cadastro.setObjectName(u"txt_email_cadastro")
        self.txt_email_cadastro.setGeometry(QRect(80, 120, 211, 25))
        self.txt_email_cadastro.setMinimumSize(QSize(0, 25))
        self.txt_email_cadastro.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(0,0,0,25);\n"
"	color: white;\n"
"	border-radius: 6px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}")
        self.txt_telefone_cadastro = QLineEdit(self.frame_4)
        self.txt_telefone_cadastro.setObjectName(u"txt_telefone_cadastro")
        self.txt_telefone_cadastro.setGeometry(QRect(80, 150, 211, 25))
        self.txt_telefone_cadastro.setMinimumSize(QSize(0, 25))
        self.txt_telefone_cadastro.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(0,0,0,25);\n"
"	color: white;\n"
"	border-radius: 6px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}")
        self.txt_senha_cadastro = QLineEdit(self.frame_4)
        self.txt_senha_cadastro.setObjectName(u"txt_senha_cadastro")
        self.txt_senha_cadastro.setGeometry(QRect(80, 180, 211, 25))
        self.txt_senha_cadastro.setMinimumSize(QSize(0, 25))
        self.txt_senha_cadastro.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(0,0,0,25);\n"
"	color: white;\n"
"	border-radius: 6px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}")
        self.txt_senha_cadastro.setEchoMode(QLineEdit.Password)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 121, 31))
        self.label.setStyleSheet(u"QLabel {\n"
"	font-family: Arial, sans-serif;\n"
"	background-color: transparent;\n"
"	font-size: 14pt;\n"
"	color: white;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.btn_cadastrar = QPushButton(self.frame_4)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(140, 220, 100, 25))
        self.btn_cadastrar.setMinimumSize(QSize(100, 25))
        self.btn_cadastrar.setMaximumSize(QSize(100, 25))
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.Pages.addWidget(self.pg_cadastrar)
        self.pg_esqueci_senha = QWidget()
        self.pg_esqueci_senha.setObjectName(u"pg_esqueci_senha")
        self.pg_esqueci_senha.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"	color: black;\n"
"}")
        self.frame_5 = QFrame(self.pg_esqueci_senha)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(-9, 1, 321, 291))
        self.frame_5.setStyleSheet(u"QFrame {\n"
"background-color: qlineargradient(spread:pad, x1:0.465, y1:0.481682, x2:0, y2:0, stop:0.147727 rgba(0, 164, 218, 255), stop:0.931818 rgba(0, 219, 255, 255));\n"
"border-radius: 0px;\n"
"color: black;\n"
"\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 20, 181, 31))
        self.label_5.setStyleSheet(u"QLabel {\n"
"	font-family: Arial, sans-serif;\n"
"	background-color: transparent;\n"
"	font-size: 14pt;\n"
"	color: white;\n"
"}")
        self.txt_esqueci_cpf = QLineEdit(self.frame_5)
        self.txt_esqueci_cpf.setObjectName(u"txt_esqueci_cpf")
        self.txt_esqueci_cpf.setGeometry(QRect(70, 80, 231, 25))
        self.txt_esqueci_cpf.setMinimumSize(QSize(0, 25))
        self.txt_esqueci_cpf.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(0,0,0,25);\n"
"	color: white;\n"
"	border-radius: 6px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}")
        self.txt_esqueci_nova_senha = QLineEdit(self.frame_5)
        self.txt_esqueci_nova_senha.setObjectName(u"txt_esqueci_nova_senha")
        self.txt_esqueci_nova_senha.setGeometry(QRect(70, 110, 231, 25))
        self.txt_esqueci_nova_senha.setMinimumSize(QSize(0, 25))
        self.txt_esqueci_nova_senha.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(0,0,0,25);\n"
"	color: white;\n"
"	border-radius: 6px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}")
        self.txt_esqueci_codigo = QLineEdit(self.frame_5)
        self.txt_esqueci_codigo.setObjectName(u"txt_esqueci_codigo")
        self.txt_esqueci_codigo.setGeometry(QRect(70, 140, 121, 25))
        self.txt_esqueci_codigo.setMinimumSize(QSize(0, 25))
        self.txt_esqueci_codigo.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(0,0,0,25);\n"
"	color: white;\n"
"	border-radius: 6px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}")
        self.txt_esqueci_nova_senha.setEchoMode(QLineEdit.Password)
        self.btn_enviar_codigo = QPushButton(self.frame_5)
        self.btn_enviar_codigo.setObjectName(u"btn_enviar_codigo")
        self.btn_enviar_codigo.setGeometry(QRect(200, 140, 101, 25))
        self.btn_enviar_codigo.setMinimumSize(QSize(0, 25))
        self.btn_enviar_codigo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_enviar_codigo.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	\n"
"	background-color: rgb(93, 186, 0);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	border-radius: 10px\n"
"}")
        self.btn_esqueci_confirmar = QPushButton(self.frame_5)
        self.btn_esqueci_confirmar.setObjectName(u"btn_esqueci_confirmar")
        self.btn_esqueci_confirmar.setGeometry(QRect(120, 190, 150, 25))
        self.btn_esqueci_confirmar.setMinimumSize(QSize(150, 25))
        self.btn_esqueci_confirmar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_esqueci_confirmar.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	\n"
"	background-color: rgb(93, 186, 0);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	border-radius: 10px\n"
"}")
        
        self.Pages.addWidget(self.pg_esqueci_senha)
        self.pg_config = QWidget()
        self.pg_config.setObjectName(u"pg_config")
        self.pg_config.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"	color: black;\n"
"}")
        self.frame_6 = QFrame(self.pg_config)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(-1, -1, 321, 301))
        self.frame_6.setStyleSheet(u"QFrame {\n"
"background-color: qlineargradient(spread:pad, x1:0.465, y1:0.481682, x2:0, y2:0, stop:0.147727 rgba(0, 164, 218, 255), stop:0.931818 rgba(0, 219, 255, 255));\n"
"border-radius: 0px;\n"
"color: black;\n"
"\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 20, 121, 31))
        self.label_6.setStyleSheet(u"QLabel {\n"
"	font-family: Arial, sans-serif;\n"
"	background-color: transparent;\n"
"	font-size: 14pt;\n"
"	color: white;\n"
"}")
        self.txt_ip = QLineEdit(self.frame_6)
        self.txt_ip.setObjectName(u"txt_ip")
        self.txt_ip.setGeometry(QRect(70, 100, 221, 25))
        self.txt_ip.setMinimumSize(QSize(0, 25))
        self.txt_ip.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(0,0,0,25);\n"
"	color: white;\n"
"	border-radius: 6px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}")
        self.txt_porta = QLineEdit(self.frame_6)
        self.txt_porta.setObjectName(u"txt_porta")
        self.txt_porta.setGeometry(QRect(72, 130, 221, 25))
        self.txt_porta.setMinimumSize(QSize(0, 25))
        self.txt_porta.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(0,0,0,25);\n"
"	color: white;\n"
"	border-radius: 6px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}")
        self.btn_padrao = QPushButton(self.frame_6)
        self.btn_padrao.setObjectName(u"btn_padrao")
        self.btn_padrao.setGeometry(QRect(100, 160, 75, 25))
        self.btn_padrao.setMinimumSize(QSize(0, 25))
        self.btn_padrao.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_padrao.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	border-radius: 10px\n"
"}\n"
"")
        self.btn_salvar = QPushButton(self.frame_6)
        self.btn_salvar.setObjectName(u"btn_salvar")
        self.btn_salvar.setGeometry(QRect(190, 160, 75, 25))
        self.btn_salvar.setMinimumSize(QSize(0, 25))
        self.btn_salvar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_salvar.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	\n"
"	background-color: rgb(93, 186, 0);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	border-radius: 10px\n"
"}\n"
"")
        self.label_6.raise_()
        self.txt_ip.raise_()
        self.btn_salvar.raise_()
        self.txt_porta.raise_()
        self.btn_padrao.raise_()
        self.Pages.addWidget(self.pg_config)
        self.lbl_versao = QLabel(self.login_h_2)
        self.lbl_versao.setObjectName(u"lbl_versao")
        self.lbl_versao.setGeometry(QRect(250, 290, 61, 20))
        self.lbl_versao.setStyleSheet(u"QLabel {\n"
"background:transparent;\n"
"color: #fff;\n"
"}")
        self.btn_config = QPushButton(self.login_h_2)
        self.btn_config.setObjectName(u"btn_config")
        self.btn_config.setGeometry(QRect(560, 300, 31, 31))
        self.btn_config.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_config.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background: transparent;;\n"
"}\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_config.setIcon(icon)
        self.btn_config.setIconSize(QSize(25, 25))
        self.btn_config.setCheckable(True)
        self.btn_config.setChecked(True)
        self.btn_closed = QPushButton(self.login_h_2)
        self.btn_closed.setObjectName(u"btn_closed")
        self.btn_closed.setGeometry(QRect(560, 10, 16, 16))
        self.btn_closed.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_closed.setStyleSheet(u"QPushButton {\n"
"	background: transparent;\n"
"    border-radius: 20px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: red;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_closed.setIcon(icon1)
        self.btn_closed.setIconSize(QSize(38, 38))

        self.verticalLayout.addWidget(self.login_h_2)

        self.login_h_3 = QWidget(Form)
        self.login_h_3.setObjectName(u"login_h_3")
        self.login_h_3.setGeometry(QRect(420, 110, 231, 401))
        self.login_h_3.setStyleSheet(u"QWidget {\n"
"background-color: white;\n"
"border-radius: 20px;\n"
"\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.login_h_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.login_h_4 = QWidget(self.login_h_3)
        self.login_h_4.setObjectName(u"login_h_4")
        self.login_h_4.setStyleSheet(u"QWidget {\n"
"background-color: qlineargradient(spread:pad, x1:0.465, y1:0.481682, x2:0, y2:0, stop:0.147727 rgba(0, 164, 218, 255), stop:0.931818 rgba(0, 219, 255, 255));\n"
"border-radius: 20px;\n"
"color: black;\n"
"\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.login_h_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 2, 10, 4)
        self.stackedWidget_2 = QStackedWidget(self.login_h_4)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"	border-radius: 20px;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.page_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.page_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame {\n"
"background-color: qlineargradient(spread:pad, x1:0.465, y1:0.481682, x2:0, y2:0, stop:0.147727 rgba(0, 164, 218, 255), stop:0.931818 rgba(0, 219, 255, 255));\n"
"border-radius: 0px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"	font-family: Arial, sans-serif;\n"
"	background-color: transparent;\n"
"	font-size: 18pt;\n"
"	color: white;\n"
"}")

        self.verticalLayout_6.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.txt_cpf_login = QLineEdit(self.frame_2)
        self.txt_cpf_login.setObjectName(u"txt_cpf_login")
        self.txt_cpf_login.setMinimumSize(QSize(0, 25))
        self.txt_cpf_login.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(0,0,0,25);\n"
"	color: white;\n"
"	border-radius: 6px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}")

        self.verticalLayout_6.addWidget(self.txt_cpf_login)

        self.txt_senha_login = QLineEdit(self.frame_2)
        self.txt_senha_login.setObjectName(u"txt_senha_login")
        self.txt_senha_login.setMinimumSize(QSize(0, 25))
        self.txt_senha_login.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(0,0,0,25);\n"
"	color: white;\n"
"	border-radius: 6px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}")
        self.txt_senha_login.setEchoMode(QLineEdit.Password)

        self.verticalLayout_6.addWidget(self.txt_senha_login)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_esqueci_login = QPushButton(self.frame_3)
        self.btn_esqueci_login.setObjectName(u"btn_esqueci_login")
        self.btn_esqueci_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_esqueci_login.setStyleSheet(u"QPushButton {\n"
"	background:transparent;\n"
"	border-radius: 0px;\n"
"	color: white;	\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 8pt;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.btn_esqueci_login)

        self.btn_cadastrar_login = QPushButton(self.frame_3)
        self.btn_cadastrar_login.setObjectName(u"btn_cadastrar_login")
        self.btn_cadastrar_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar_login.setStyleSheet(u"QPushButton {\n"
"	background:transparent;\n"
"	border-radius: 0px;\n"
"	color: white;	\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 8pt;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_cadastrar_login)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.btn_entrar_login = QPushButton(self.frame_2)
        self.btn_entrar_login.setObjectName(u"btn_entrar_login")
        self.btn_entrar_login.setMinimumSize(QSize(150, 25))
        self.btn_entrar_login.setMaximumSize(QSize(150, 25))
        self.btn_entrar_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_entrar_login.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	border-radius: 10px;\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.btn_entrar_login, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.stackedWidget_2.addWidget(self.page_3)

        self.verticalLayout_5.addWidget(self.stackedWidget_2)


        self.verticalLayout_3.addWidget(self.login_h_4)

        self.icone = QLabel(Form)
        self.icone.setObjectName(u"icone")
        self.icone.setGeometry(QRect(-10, 290, 241, 251))
        self.icone.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"}")
        self.icone.setPixmap(QPixmap(u":/icons/icons/cobra_HD.png"))
        self.icone.setScaledContents(True)

        self.retranslateUi(Form)

        self.Pages.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_nome_empresa.setText(QCoreApplication.translate("Form", u"RuralConnect", None))
#if QT_CONFIG(tooltip)
        self.btn_cadastrar.setToolTip(QCoreApplication.translate("Form", u"Enviar Cadastro", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_cadastrar.setAccessibleDescription(QCoreApplication.translate("Form", u"Botao de enviar cadastro de usuario", None))
#endif // QT_CONFIG(accessibility)
        self.btn_cadastrar.setText(QCoreApplication.translate("Form", u"Cadastrar", None))
#if QT_CONFIG(tooltip)
        self.txt_email_cadastro.setToolTip(QCoreApplication.translate("Form", u"Email", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_email_cadastro.setAccessibleDescription(QCoreApplication.translate("Form", u"Campo de texto para inserir email de Usuario para Cadastro", None))
#endif // QT_CONFIG(accessibility)
        self.txt_email_cadastro.setPlaceholderText(QCoreApplication.translate("Form", u" Email Corporativo", None))
#if QT_CONFIG(tooltip)
        self.txt_senha_cadastro.setToolTip(QCoreApplication.translate("Form", u"Senha", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_senha_cadastro.setAccessibleDescription(QCoreApplication.translate("Form", u"Campo de texto para inserir senha de Usuario para Cadastro", None))
#endif // QT_CONFIG(accessibility)
        self.txt_senha_cadastro.setPlaceholderText(QCoreApplication.translate("Form", u" Senha", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Cadastrar-se</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.txt_cpf_cadastro.setToolTip(QCoreApplication.translate("Form", u"CPF", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_cpf_cadastro.setAccessibleDescription(QCoreApplication.translate("Form", u"Campo de texto para inserir CPF de Usuario para Cadastro", None))
#endif // QT_CONFIG(accessibility)
        self.txt_cpf_cadastro.setPlaceholderText(QCoreApplication.translate("Form", u" CPF", None))
#if QT_CONFIG(tooltip)
        self.txt_telefone_cadastro.setToolTip(QCoreApplication.translate("Form", u"Telefone", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_telefone_cadastro.setAccessibleDescription(QCoreApplication.translate("Form", u"Campo de texto para inserir telefone de Usuario para Cadastro", None))
#endif // QT_CONFIG(accessibility)
        self.txt_telefone_cadastro.setPlaceholderText(QCoreApplication.translate("Form", u" Telefone", None))
#if QT_CONFIG(tooltip)
        self.txt_nome_cadastro.setToolTip(QCoreApplication.translate("Form", u"Nome", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_nome_cadastro.setAccessibleDescription(QCoreApplication.translate("Form", u"Campo de texto para inserir nome de Usuario para Cadastro", None))
#endif // QT_CONFIG(accessibility)
        self.txt_nome_cadastro.setPlaceholderText(QCoreApplication.translate("Form", u" Nome", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Troque sua Senha", None))
#if QT_CONFIG(tooltip)
        self.txt_esqueci_cpf.setToolTip(QCoreApplication.translate("Form", u"CPF", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_esqueci_cpf.setAccessibleDescription(QCoreApplication.translate("Form", u"Campo de texto para digitacao do CPF para recuperacao de senha", None))
#endif // QT_CONFIG(accessibility)
        self.txt_esqueci_cpf.setPlaceholderText(QCoreApplication.translate("Form", u" Informe seu CPF", None))
#if QT_CONFIG(tooltip)
        self.txt_esqueci_nova_senha.setToolTip(QCoreApplication.translate("Form", u"Nova Senha", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_esqueci_nova_senha.setAccessibleDescription(QCoreApplication.translate("Form", u"Campo de texto para digitacao de nova senha a ser cadastrada", None))
#endif // QT_CONFIG(accessibility)
        self.txt_esqueci_nova_senha.setPlaceholderText(QCoreApplication.translate("Form", u" Nova Senha", None))
#if QT_CONFIG(tooltip)
        self.btn_enviar_codigo.setToolTip(QCoreApplication.translate("Form", u"Receber C\u00f3digo de Verifica\u00e7\u00e3o", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_enviar_codigo.setAccessibleDescription(QCoreApplication.translate("Form", u"Bot\u00e3o para receber o codigo no email vinculado ao CPF informado", None))
#endif // QT_CONFIG(accessibility)
        self.btn_enviar_codigo.setText(QCoreApplication.translate("Form", u"Receber", None))
#if QT_CONFIG(tooltip)
        self.btn_esqueci_confirmar.setToolTip(QCoreApplication.translate("Form", u"Trocar a Senha", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_esqueci_confirmar.setAccessibleDescription(QCoreApplication.translate("Form", u"Botao para confirmar a troca da senha", None))
#endif // QT_CONFIG(accessibility)
        self.btn_esqueci_confirmar.setText(QCoreApplication.translate("Form", u"Trocar Senha", None))
#if QT_CONFIG(tooltip)
        self.txt_esqueci_codigo.setToolTip(QCoreApplication.translate("Form", u"C\u00f3digo de Verifica\u00e7\u00e3o", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_esqueci_codigo.setAccessibleDescription(QCoreApplication.translate("Form", u"Campo para digitacao de codigo de verificacao para efetuar troca de senha", None))
#endif // QT_CONFIG(accessibility)
        self.txt_esqueci_codigo.setPlaceholderText(QCoreApplication.translate("Form", u" C\u00f3digo", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Configura\u00e7\u00e3o", None))
#if QT_CONFIG(tooltip)
        self.txt_ip.setToolTip(QCoreApplication.translate("Form", u"Endere\u00e7o de IP", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_ip.setAccessibleDescription(QCoreApplication.translate("Form", u"Campo de texto para insercao de endereco de ip na configuracao de conexao com Banco de Dados", None))
#endif // QT_CONFIG(accessibility)
        self.txt_ip.setPlaceholderText(QCoreApplication.translate("Form", u" Endere\u00e7o de IP", None))
#if QT_CONFIG(tooltip)
        self.txt_porta.setToolTip(QCoreApplication.translate("Form", u"Porta", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_porta.setAccessibleDescription(QCoreApplication.translate("Form", u"Campo para informar a porta para configuracao de conexao com Banco de Dados", None))
#endif // QT_CONFIG(accessibility)
        self.txt_porta.setPlaceholderText(QCoreApplication.translate("Form", u" Porta", None))
#if QT_CONFIG(tooltip)
        self.btn_padrao.setToolTip(QCoreApplication.translate("Form", u"Padr\u00e3o", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_padrao.setAccessibleDescription(QCoreApplication.translate("Form", u"Botao de atribuir valores padrao para IP e Porta", None))
#endif // QT_CONFIG(accessibility)
        self.btn_padrao.setText(QCoreApplication.translate("Form", u"Padr\u00e3o", None))
#if QT_CONFIG(tooltip)
        self.btn_salvar.setToolTip(QCoreApplication.translate("Form", u"Salvar", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_salvar.setAccessibleDescription(QCoreApplication.translate("Form", u"Botao de salvar configuracao de conexao", None))
#endif // QT_CONFIG(accessibility)
        self.btn_salvar.setText(QCoreApplication.translate("Form", u"Salvar", None))
        self.lbl_versao.setText(QCoreApplication.translate("Form", u"Vers\u00e3o 1.2", None))
#if QT_CONFIG(tooltip)
        self.btn_config.setToolTip(QCoreApplication.translate("Form", u"Configura\u00e7\u00f5es", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_config.setAccessibleDescription(QCoreApplication.translate("Form", u"Botao de COnfiguracoes de conexao com Banco de Dados", None))
#endif // QT_CONFIG(accessibility)
        self.btn_config.setText("")
#if QT_CONFIG(tooltip)
        self.btn_closed.setToolTip(QCoreApplication.translate("Form", u"Fechar", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_closed.setAccessibleDescription(QCoreApplication.translate("Form", u"Botao de fechar sistema", None))
#endif // QT_CONFIG(accessibility)
        self.btn_closed.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Login", None))
#if QT_CONFIG(tooltip)
        self.txt_cpf_login.setToolTip(QCoreApplication.translate("Form", u"CPF", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_cpf_login.setAccessibleDescription(QCoreApplication.translate("Form", u"Campo de digita\u00e7\u00e3o de CPF para Login", None))
#endif // QT_CONFIG(accessibility)
        self.txt_cpf_login.setPlaceholderText(QCoreApplication.translate("Form", u" CPF", None))
#if QT_CONFIG(tooltip)
        self.txt_senha_login.setToolTip(QCoreApplication.translate("Form", u"Senha", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_senha_login.setAccessibleDescription(QCoreApplication.translate("Form", u"Campo de digita\u00e7\u00e3o de senha para Login", None))
#endif // QT_CONFIG(accessibility)
        self.txt_senha_login.setPlaceholderText(QCoreApplication.translate("Form", u"Senha", None))
#if QT_CONFIG(tooltip)
        self.btn_esqueci_login.setToolTip(QCoreApplication.translate("Form", u"Esqueci a senha", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_esqueci_login.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.btn_esqueci_login.setAccessibleDescription(QCoreApplication.translate("Form", u"Botao de recupera\u00e7\u00e3o de Senha", None))
#endif // QT_CONFIG(accessibility)
        self.btn_esqueci_login.setText(QCoreApplication.translate("Form", u"Esqueci a senha", None))
#if QT_CONFIG(tooltip)
        self.btn_cadastrar_login.setToolTip(QCoreApplication.translate("Form", u"Cadastrar Usu\u00e1rio", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_cadastrar_login.setAccessibleDescription(QCoreApplication.translate("Form", u"Botao de Cadastrar novo Usuario", None))
#endif // QT_CONFIG(accessibility)
        self.btn_cadastrar_login.setText(QCoreApplication.translate("Form", u"Cadastrar", None))
#if QT_CONFIG(tooltip)
        self.btn_entrar_login.setToolTip(QCoreApplication.translate("Form", u"Entrar no Sistema", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_entrar_login.setAccessibleDescription(QCoreApplication.translate("Form", u"Botao de Confirmar Login", None))
#endif // QT_CONFIG(accessibility)
        self.btn_entrar_login.setText(QCoreApplication.translate("Form", u"Entrar", None))
        self.icone.setText("")
    # retranslateUi

