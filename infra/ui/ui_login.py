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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QStackedWidget, QWidget)
from PySide6 import QtCore
from infra.ui import icons_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(908, 625)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setStyleSheet(u"QWidget{\n"
"	background-color: white;\n"
"	border: 0px;\n"
"}")
        self.login_h = QFrame(Form)
        self.login_h.setObjectName(u"login_h")
        self.login_h.setGeometry(QRect(70, 150, 691, 321))
        self.login_h.setStyleSheet(u"QFrame {\n"
"background-color: qlineargradient(spread:pad, x1:0.465, y1:0.481682, x2:0, y2:0, stop:0.147727 rgba(0, 164, 218, 255), stop:0.931818 rgba(0, 219, 255, 255));\n"
"border-radius: 8px\n"
"}")
        self.login_h.setFrameShape(QFrame.StyledPanel)
        self.login_h.setFrameShadow(QFrame.Raised)
        self.Pages = QStackedWidget(self.login_h)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setGeometry(QRect(40, 0, 361, 311))
        self.Pages.setStyleSheet(u"background:transparent;")
        self.pg_config = QWidget()
        self.pg_config.setObjectName(u"pg_config")
        self.label_3 = QLabel(self.pg_config)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 20, 131, 41))
        font = QFont()
        font.setFamilies([u"Arial,sans-serif"])
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"QLabel {\n"
"	font-family: Arial, sans-serif;\n"
"	background-color: transparent;\n"
"	font-size: 14pt;\n"
"	color: white;\n"
"}")
        self.txt_ip = QLineEdit(self.pg_config)
        self.txt_ip.setObjectName(u"txt_ip")
        self.txt_ip.setGeometry(QRect(20, 110, 281, 31))
        self.txt_ip.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(0,0,0,25);\n"
"	color: white;\n"
"	border-radius: 6px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}")
        self.txt_porta = QLineEdit(self.pg_config)
        self.txt_porta.setObjectName(u"txt_porta")
        self.txt_porta.setGeometry(QRect(20, 160, 281, 31))
        self.txt_porta.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(0,0,0,25);\n"
"	color: white;\n"
"	border-radius: 6px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}")
        self.btn_salvar = QPushButton(self.pg_config)
        self.btn_salvar.setObjectName(u"btn_salvar")
        self.btn_salvar.setGeometry(QRect(200, 210, 75, 23))
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
        self.btn_padrao = QPushButton(self.pg_config)
        self.btn_padrao.setObjectName(u"btn_padrao")
        self.btn_padrao.setGeometry(QRect(40, 210, 75, 23))
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
        self.Pages.addWidget(self.pg_config)
        self.pg_esqueci_senha = QWidget()
        self.pg_esqueci_senha.setObjectName(u"pg_esqueci_senha")
        self.label_7 = QLabel(self.pg_esqueci_senha)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 20, 171, 41))
        self.label_7.setStyleSheet(u"QLabel {\n"
"	font-family: Arial, sans-serif;\n"
"	background-color: transparent;\n"
"	font-size: 14pt;\n"
"	color: white;\n"
"}")
        self.txt_esqueci_cpf = QLineEdit(self.pg_esqueci_senha)
        self.txt_esqueci_cpf.setObjectName(u"txt_esqueci_cpf")
        self.txt_esqueci_cpf.setGeometry(QRect(20, 80, 301, 31))
        self.txt_esqueci_cpf.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(0,0,0,25);\n"
"	color: white;\n"
"	border-radius: 6px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}")
        self.txt_esqueci_nova_senha = QLineEdit(self.pg_esqueci_senha)
        self.txt_esqueci_nova_senha.setObjectName(u"txt_esqueci_nova_senha")
        self.txt_esqueci_nova_senha.setGeometry(QRect(20, 120, 301, 31))
        self.txt_esqueci_nova_senha.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(0,0,0,25);\n"
"	color: white;\n"
"	border-radius: 6px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}")
        self.txt_esqueci_nova_senha.setEchoMode(QLineEdit.Password)
        self.txt_esqueci_codigo = QLineEdit(self.pg_esqueci_senha)
        self.txt_esqueci_codigo.setObjectName(u"txt_esqueci_codigo")
        self.txt_esqueci_codigo.setGeometry(QRect(20, 160, 191, 31))
        self.txt_esqueci_codigo.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(0,0,0,25);\n"
"	color: white;\n"
"	border-radius: 6px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}")
        self.btn_esqueci_confirmar = QPushButton(self.pg_esqueci_senha)
        self.btn_esqueci_confirmar.setObjectName(u"btn_esqueci_confirmar")
        self.btn_esqueci_confirmar.setGeometry(QRect(120, 240, 101, 31))
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
        self.btn_enviar_codigo = QPushButton(self.pg_esqueci_senha)
        self.btn_enviar_codigo.setObjectName(u"btn_enviar_codigo")
        self.btn_enviar_codigo.setGeometry(QRect(230, 160, 91, 31))
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
        self.Pages.addWidget(self.pg_esqueci_senha)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 40, 231, 81))
        font1 = QFont()
        font1.setFamilies([u"Arial,sans-serif"])
        font1.setPointSize(32)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel {\n"
"	font-family: Arial, sans-serif;\n"
"	background-color: transparent;\n"
"	font-size: 32pt;\n"
"	color: white;\n"
"}")
        self.label_2 = QLabel(self.pg_home)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 130, 141, 131))
        self.label_2.setStyleSheet(u"background:transparent;")
        self.label_2.setPixmap(QPixmap(u":/icons/icons/cobra.png"))
        self.label_2.setScaledContents(True)
        self.label_5 = QLabel(self.pg_home)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(300, 290, 51, 20))
        font2 = QFont()
        font2.setPointSize(7)
        self.label_5.setFont(font2)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet(u"background:transparent;\n"
"color: #fff\n"
"")
        self.Pages.addWidget(self.pg_home)
        self.pg_cadastrar = QWidget()
        self.pg_cadastrar.setObjectName(u"pg_cadastrar")
        self.label_4 = QLabel(self.pg_cadastrar)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 20, 151, 31))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"QLabel {\n"
"	font-family: Arial, sans-serif;\n"
"	background-color: transparent;\n"
"	font-size: 14pt;\n"
"	color: white;\n"
"}")
        self.txt_nome_cadastro = QLineEdit(self.pg_cadastrar)
        self.txt_nome_cadastro.setObjectName(u"txt_nome_cadastro")
        self.txt_nome_cadastro.setGeometry(QRect(0, 60, 341, 31))
        font3 = QFont()
        font3.setFamilies([u"Arial,sans-serif"])
        font3.setPointSize(11)
        self.txt_nome_cadastro.setFont(font3)
        self.txt_nome_cadastro.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(0,0,0,25);\n"
"	color: white;\n"
"	border-radius: 6px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}")
        self.txt_cpf_cadastro = QLineEdit(self.pg_cadastrar)
        self.txt_cpf_cadastro.setObjectName(u"txt_cpf_cadastro")
        self.txt_cpf_cadastro.setGeometry(QRect(0, 100, 341, 31))
        self.txt_cpf_cadastro.setFont(font3)
        self.txt_cpf_cadastro.setCursor(QCursor(Qt.IBeamCursor))
        self.txt_cpf_cadastro.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(0,0,0,25);\n"
"	color: white;\n"
"	border-radius: 6px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}")
        self.txt_email_cadastro = QLineEdit(self.pg_cadastrar)
        self.txt_email_cadastro.setObjectName(u"txt_email_cadastro")
        self.txt_email_cadastro.setGeometry(QRect(0, 140, 341, 31))
        self.txt_email_cadastro.setFont(font3)
        self.txt_email_cadastro.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(0,0,0,25);\n"
"	color: white;\n"
"	border-radius: 6px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}")
        self.txt_telefone_cadastro = QLineEdit(self.pg_cadastrar)
        self.txt_telefone_cadastro.setObjectName(u"txt_telefone_cadastro")
        self.txt_telefone_cadastro.setGeometry(QRect(0, 180, 341, 31))
        self.txt_telefone_cadastro.setFont(font3)
        self.txt_telefone_cadastro.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(0,0,0,25);\n"
"	color: white;\n"
"	border-radius: 6px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}")
        self.txt_telefone_cadastro.setEchoMode(QLineEdit.Normal)
        self.txt_senha_cadastro = QLineEdit(self.pg_cadastrar)
        self.txt_senha_cadastro.setObjectName(u"txt_senha_cadastro")
        self.txt_senha_cadastro.setGeometry(QRect(0, 220, 341, 31))
        self.txt_senha_cadastro.setFont(font3)
        self.txt_senha_cadastro.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(0,0,0,25);\n"
"	color: white;\n"
"	border-radius: 6px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}")
        self.txt_senha_cadastro.setEchoMode(QLineEdit.Password)
        self.btn_cadastrar = QPushButton(self.pg_cadastrar)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(60, 260, 201, 31))
        self.btn_cadastrar.setFont(font3)
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
        self.btn_config = QPushButton(self.login_h)
        self.btn_config.setObjectName(u"btn_config")
        self.btn_config.setGeometry(QRect(0, 280, 41, 31))
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
        self.btn_config.setIconSize(QSize(30, 30))
        self.login_v = QFrame(Form)
        self.login_v.setObjectName(u"login_v")
        self.login_v.setGeometry(QRect(470, 100, 261, 411))
        self.login_v.setStyleSheet(u"QFrame {\n"
"background-color: qlineargradient(spread:pad, x1:0.465, y1:0.481682, x2:0, y2:0, stop:0.147727 rgba(0, 164, 218, 255), stop:0.931818 rgba(0, 219, 255, 255));\n"
"border-radius: 8px;\n"
"}")
        self.login_v.setFrameShape(QFrame.StyledPanel)
        self.login_v.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.login_v)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(100, 70, 61, 41))
        font4 = QFont()
        font4.setFamilies([u"Arial,sans-serif"])
        font4.setPointSize(18)
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"QLabel {\n"
"	font-family: Arial, sans-serif;\n"
"	background-color: transparent;\n"
"	font-size: 18pt;\n"
"	color: white;\n"
"}")
        self.txt_cpf_login = QLineEdit(self.login_v)
        self.txt_cpf_login.setObjectName(u"txt_cpf_login")
        self.txt_cpf_login.setGeometry(QRect(22, 159, 221, 31))
        self.txt_cpf_login.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(0,0,0,25);\n"
"	color: white;\n"
"	border-radius: 6px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}")
        self.txt_senha_login = QLineEdit(self.login_v)
        self.txt_senha_login.setObjectName(u"txt_senha_login")
        self.txt_senha_login.setGeometry(QRect(20, 210, 221, 31))
        self.txt_senha_login.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(0,0,0,25);\n"
"	color: white;\n"
"	border-radius: 6px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}")
        self.txt_senha_login.setEchoMode(QLineEdit.Password)
        self.btn_esqueci_login = QPushButton(self.login_v)
        self.btn_esqueci_login.setObjectName(u"btn_esqueci_login")
        self.btn_esqueci_login.setGeometry(QRect(20, 250, 111, 23))
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
"	background-color: rgb(0, 170, 255);\n"
"}")
        self.btn_cadastrar_login = QPushButton(self.login_v)
        self.btn_cadastrar_login.setObjectName(u"btn_cadastrar_login")
        self.btn_cadastrar_login.setGeometry(QRect(150, 250, 81, 23))
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
"	background-color: rgb(0, 170, 255);\n"
"}")
        self.btn_entrar_login = QPushButton(self.login_v)
        self.btn_entrar_login.setObjectName(u"btn_entrar_login")
        self.btn_entrar_login.setGeometry(QRect(30, 290, 201, 31))
        font5 = QFont()
        font5.setFamilies([u"Arial,sans-serif"])
        font5.setPointSize(12)
        self.btn_entrar_login.setFont(font5)
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
"	font-size: 12pt;\n"
"}\n"
"")
        self.btn_closed = QPushButton(self.login_v)
        self.btn_closed.setObjectName(u"btn_closed")
        self.btn_closed.setGeometry(QRect(235, 10, 20, 20))
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
        self.btn_closed.setAutoDefault(False)

        self.retranslateUi(Form)

        self.Pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Configura\u00e7\u00e3o", None))
#if QT_CONFIG(tooltip)
        self.txt_ip.setToolTip(QCoreApplication.translate("Form", u"Endere\u00e7o IP", None))
#endif // QT_CONFIG(tooltip)
        self.txt_ip.setPlaceholderText(QCoreApplication.translate("Form", u"  Endere\u00e7o de IP", None))
#if QT_CONFIG(tooltip)
        self.txt_porta.setToolTip(QCoreApplication.translate("Form", u"Porta", None))
#endif // QT_CONFIG(tooltip)
        self.txt_porta.setPlaceholderText(QCoreApplication.translate("Form", u"  Porta", None))
#if QT_CONFIG(tooltip)
        self.btn_salvar.setToolTip(QCoreApplication.translate("Form", u"Salvar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_salvar.setText(QCoreApplication.translate("Form", u"Salvar", None))
#if QT_CONFIG(tooltip)
        self.btn_padrao.setToolTip(QCoreApplication.translate("Form", u"Padr\u00e3o", None))
#endif // QT_CONFIG(tooltip)
        self.btn_padrao.setText(QCoreApplication.translate("Form", u"Padr\u00e3o", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Troque sua Senha", None))
#if QT_CONFIG(tooltip)
        self.txt_esqueci_cpf.setToolTip(QCoreApplication.translate("Form", u"CPF", None))
#endif // QT_CONFIG(tooltip)
        self.txt_esqueci_cpf.setPlaceholderText(QCoreApplication.translate("Form", u"Informe seu CPF", None))
#if QT_CONFIG(tooltip)
        self.txt_esqueci_nova_senha.setToolTip(QCoreApplication.translate("Form", u"Nova Senha", None))
#endif // QT_CONFIG(tooltip)
        self.txt_esqueci_nova_senha.setPlaceholderText(QCoreApplication.translate("Form", u"Nova Senha", None))
#if QT_CONFIG(tooltip)
        self.txt_esqueci_codigo.setToolTip(QCoreApplication.translate("Form", u"C\u00f3digo de Verifica\u00e7\u00e3o", None))
#endif // QT_CONFIG(tooltip)
        self.txt_esqueci_codigo.setPlaceholderText(QCoreApplication.translate("Form", u"C\u00f3digo de Verifica\u00e7\u00e3o", None))
#if QT_CONFIG(tooltip)
        self.btn_esqueci_confirmar.setToolTip(QCoreApplication.translate("Form", u"Confirmar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_esqueci_confirmar.setText(QCoreApplication.translate("Form", u"Trocar Senha", None))
#if QT_CONFIG(tooltip)
        self.btn_enviar_codigo.setToolTip(QCoreApplication.translate("Form", u"Receber C\u00f3digo", None))
#endif // QT_CONFIG(tooltip)
        self.btn_enviar_codigo.setText(QCoreApplication.translate("Form", u"Receber", None))
        self.label.setText(QCoreApplication.translate("Form", u"Bem Vindo", None))
        self.label_2.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Vers\u00e3o 1.1", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Cadastrar-se</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.txt_nome_cadastro.setToolTip(QCoreApplication.translate("Form", u"Nome", None))
#endif // QT_CONFIG(tooltip)
        self.txt_nome_cadastro.setText("")
        self.txt_nome_cadastro.setPlaceholderText(QCoreApplication.translate("Form", u"  Nome", None))
#if QT_CONFIG(tooltip)
        self.txt_cpf_cadastro.setToolTip(QCoreApplication.translate("Form", u"Email", None))
#endif // QT_CONFIG(tooltip)
        self.txt_cpf_cadastro.setText("")
        self.txt_cpf_cadastro.setPlaceholderText(QCoreApplication.translate("Form", u"  CPF", None))
#if QT_CONFIG(tooltip)
        self.txt_email_cadastro.setToolTip(QCoreApplication.translate("Form", u"Telefone", None))
#endif // QT_CONFIG(tooltip)
        self.txt_email_cadastro.setText("")
        self.txt_email_cadastro.setPlaceholderText(QCoreApplication.translate("Form", u"  Email corporativo", None))
#if QT_CONFIG(tooltip)
        self.txt_telefone_cadastro.setToolTip(QCoreApplication.translate("Form", u"Senha", None))
#endif // QT_CONFIG(tooltip)
        self.txt_telefone_cadastro.setText("")
        self.txt_telefone_cadastro.setPlaceholderText(QCoreApplication.translate("Form", u"  Telefone", None))
#if QT_CONFIG(tooltip)
        self.txt_senha_cadastro.setToolTip(QCoreApplication.translate("Form", u"CPF", None))
#endif // QT_CONFIG(tooltip)
        self.txt_senha_cadastro.setText("")
        self.txt_senha_cadastro.setPlaceholderText(QCoreApplication.translate("Form", u"  Senha", None))
#if QT_CONFIG(tooltip)
        self.btn_cadastrar.setToolTip(QCoreApplication.translate("Form", u"Cadastrar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_cadastrar.setText(QCoreApplication.translate("Form", u"Cadastrar", None))
#if QT_CONFIG(tooltip)
        self.btn_config.setToolTip(QCoreApplication.translate("Form", u"Configura\u00e7\u00f5es", None))
#endif // QT_CONFIG(tooltip)
        self.btn_config.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"Login", None))
#if QT_CONFIG(tooltip)
        self.txt_cpf_login.setToolTip(QCoreApplication.translate("Form", u"CPF", None))
#endif // QT_CONFIG(tooltip)
        self.txt_cpf_login.setPlaceholderText(QCoreApplication.translate("Form", u"  CPF", None))
#if QT_CONFIG(tooltip)
        self.txt_senha_login.setToolTip(QCoreApplication.translate("Form", u"Senha", None))
#endif // QT_CONFIG(tooltip)
        self.txt_senha_login.setPlaceholderText(QCoreApplication.translate("Form", u"  Senha", None))
#if QT_CONFIG(tooltip)
        self.btn_esqueci_login.setToolTip(QCoreApplication.translate("Form", u"Esqueci a Senha", None))
#endif // QT_CONFIG(tooltip)
        self.btn_esqueci_login.setText(QCoreApplication.translate("Form", u"Esqueci a senha", None))
#if QT_CONFIG(tooltip)
        self.btn_cadastrar_login.setToolTip(QCoreApplication.translate("Form", u"Cadastrar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_cadastrar_login.setText(QCoreApplication.translate("Form", u"Cadastrar", None))
#if QT_CONFIG(tooltip)
        self.btn_entrar_login.setToolTip(QCoreApplication.translate("Form", u"Entrar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_entrar_login.setText(QCoreApplication.translate("Form", u"Entrar", None))
#if QT_CONFIG(tooltip)
        self.btn_closed.setToolTip(QCoreApplication.translate("Form", u"Fechar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_closed.setText("")
    # retranslateUi

