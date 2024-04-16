# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sistema.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QToolBox, QVBoxLayout, QWidget)
from ui import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(932, 589)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.465, y1:0.481682, x2:0, y2:0, stop:0.147727 rgba(0, 164, 218, 255), stop:0.931818 rgba(0, 219, 255, 255));")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.menu = QFrame(self.centralwidget)
        self.menu.setObjectName(u"menu")
        self.menu.setMaximumSize(QSize(9, 16777215))
        self.menu.setStyleSheet(u"background: transparent;")
        self.menu.setFrameShape(QFrame.StyledPanel)
        self.menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.menu)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(self.menu)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.toolBox = QToolBox(self.frame)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 113, 448))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_home_menu = QPushButton(self.page)
        self.btn_home_menu.setObjectName(u"btn_home_menu")
        self.btn_home_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home_menu.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.btn_home_menu)

        self.btn_cadastrar_menu = QPushButton(self.page)
        self.btn_cadastrar_menu.setObjectName(u"btn_cadastrar_menu")
        self.btn_cadastrar_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar_menu.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.btn_cadastrar_menu)

        self.btn_historico_menu = QPushButton(self.page)
        self.btn_historico_menu.setObjectName(u"btn_historico_menu")
        self.btn_historico_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_historico_menu.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.btn_historico_menu)

        self.btn_enviar_menu = QPushButton(self.page)
        self.btn_enviar_menu.setObjectName(u"btn_enviar_menu")
        self.btn_enviar_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_enviar_menu.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.btn_enviar_menu)

        self.btn_perfil_menu = QPushButton(self.page)
        self.btn_perfil_menu.setObjectName(u"btn_perfil_menu")
        self.btn_perfil_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_perfil_menu.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.btn_perfil_menu)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.btn_encerrar_menu = QPushButton(self.page)
        self.btn_encerrar_menu.setObjectName(u"btn_encerrar_menu")
        self.btn_encerrar_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_encerrar_menu.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(255, 75, 75);\n"
"	\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.btn_encerrar_menu)

        self.toolBox.addItem(self.page, u"Menu")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.menu)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setStyleSheet(u"background: transparent;")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.hand_frame = QFrame(self.main_container)
        self.hand_frame.setObjectName(u"hand_frame")
        self.hand_frame.setStyleSheet(u"background:transparent;")
        self.hand_frame.setFrameShape(QFrame.StyledPanel)
        self.hand_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.hand_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_toogle = QPushButton(self.hand_frame)
        self.btn_toogle.setObjectName(u"btn_toogle")
        self.btn_toogle.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/option.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toogle.setIcon(icon)
        self.btn_toogle.setIconSize(QSize(28, 28))

        self.horizontalLayout_2.addWidget(self.btn_toogle, 0, Qt.AlignLeft)

        self.label = QLabel(self.hand_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.hand_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setStyleSheet(u"background: transparent;")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.main_frame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.Pages = QStackedWidget(self.main_frame)
        self.Pages.setObjectName(u"Pages")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_5 = QVBoxLayout(self.pg_home)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_8 = QFrame(self.pg_home)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_8)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_15.addWidget(self.label_4)


        self.verticalLayout_5.addWidget(self.frame_8)

        self.Pages.addWidget(self.pg_home)
        self.pg_cadastrar = QWidget()
        self.pg_cadastrar.setObjectName(u"pg_cadastrar")
        self.verticalLayout_6 = QVBoxLayout(self.pg_cadastrar)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_9 = QFrame(self.pg_cadastrar)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background:transparent;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_9)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_carregar_formulario = QPushButton(self.frame_11)
        self.btn_carregar_formulario.setObjectName(u"btn_carregar_formulario")
        self.btn_carregar_formulario.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.btn_carregar_formulario)

        self.btn_carregar_documentos = QPushButton(self.frame_11)
        self.btn_carregar_documentos.setObjectName(u"btn_carregar_documentos")
        self.btn_carregar_documentos.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.btn_carregar_documentos)


        self.verticalLayout_16.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setStyleSheet(u"background:transparent;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background:transparent;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_13)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.txt_cadastro_nome = QLineEdit(self.frame_13)
        self.txt_cadastro_nome.setObjectName(u"txt_cadastro_nome")
        self.txt_cadastro_nome.setStyleSheet(u"background-color: rgba(0, 0, 0, 20);")

        self.verticalLayout_18.addWidget(self.txt_cadastro_nome)

        self.txt_cadastro_cpf = QLineEdit(self.frame_13)
        self.txt_cadastro_cpf.setObjectName(u"txt_cadastro_cpf")
        self.txt_cadastro_cpf.setStyleSheet(u"background-color: rgba(0, 0, 0, 20);")

        self.verticalLayout_18.addWidget(self.txt_cadastro_cpf)

        self.txt_cadastro_rg = QLineEdit(self.frame_13)
        self.txt_cadastro_rg.setObjectName(u"txt_cadastro_rg")
        self.txt_cadastro_rg.setStyleSheet(u"background-color: rgba(0, 0, 0, 20);")

        self.verticalLayout_18.addWidget(self.txt_cadastro_rg)

        self.txt_cadastro_filiacao = QLineEdit(self.frame_13)
        self.txt_cadastro_filiacao.setObjectName(u"txt_cadastro_filiacao")
        self.txt_cadastro_filiacao.setStyleSheet(u"background-color: rgba(0, 0, 0, 20);")

        self.verticalLayout_18.addWidget(self.txt_cadastro_filiacao)

        self.txt_cadastro_endereco = QLineEdit(self.frame_13)
        self.txt_cadastro_endereco.setObjectName(u"txt_cadastro_endereco")
        self.txt_cadastro_endereco.setStyleSheet(u"background-color: rgba(0, 0, 0, 20);")

        self.verticalLayout_18.addWidget(self.txt_cadastro_endereco)

        self.txt_cadastro_nascimento = QLineEdit(self.frame_13)
        self.txt_cadastro_nascimento.setObjectName(u"txt_cadastro_nascimento")
        self.txt_cadastro_nascimento.setStyleSheet(u"background-color: rgba(0, 0, 0, 20);")

        self.verticalLayout_18.addWidget(self.txt_cadastro_nascimento)

        self.txt_cadastro_cidade = QLineEdit(self.frame_13)
        self.txt_cadastro_cidade.setObjectName(u"txt_cadastro_cidade")
        self.txt_cadastro_cidade.setStyleSheet(u"background-color: rgba(0, 0, 0, 20);")

        self.verticalLayout_18.addWidget(self.txt_cadastro_cidade)

        self.txt_cadastro_estado = QLineEdit(self.frame_13)
        self.txt_cadastro_estado.setObjectName(u"txt_cadastro_estado")
        self.txt_cadastro_estado.setStyleSheet(u"background-color: rgba(0, 0, 0, 20);")

        self.verticalLayout_18.addWidget(self.txt_cadastro_estado)

        self.txt_cadastro_telefone = QLineEdit(self.frame_13)
        self.txt_cadastro_telefone.setObjectName(u"txt_cadastro_telefone")
        self.txt_cadastro_telefone.setStyleSheet(u"background-color: rgba(0, 0, 0, 20);")

        self.verticalLayout_18.addWidget(self.txt_cadastro_telefone)

        self.txt_cadastro_email = QLineEdit(self.frame_13)
        self.txt_cadastro_email.setObjectName(u"txt_cadastro_email")
        self.txt_cadastro_email.setStyleSheet(u"background-color: rgba(0, 0, 0, 20);")

        self.verticalLayout_18.addWidget(self.txt_cadastro_email)


        self.horizontalLayout_9.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setStyleSheet(u"background:transparent;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_14)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.lista_documentos_cadastro = QListView(self.frame_14)
        self.lista_documentos_cadastro.setObjectName(u"lista_documentos_cadastro")
        self.lista_documentos_cadastro.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_17.addWidget(self.lista_documentos_cadastro)

        self.btn_cadastro_enviar = QPushButton(self.frame_14)
        self.btn_cadastro_enviar.setObjectName(u"btn_cadastro_enviar")
        self.btn_cadastro_enviar.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"}\n"
"")

        self.verticalLayout_17.addWidget(self.btn_cadastro_enviar)


        self.horizontalLayout_9.addWidget(self.frame_14)


        self.verticalLayout_16.addWidget(self.frame_12)


        self.verticalLayout_6.addWidget(self.frame_9)

        self.Pages.addWidget(self.pg_cadastrar)
        self.pg_historico = QWidget()
        self.pg_historico.setObjectName(u"pg_historico")
        self.verticalLayout_7 = QVBoxLayout(self.pg_historico)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_10 = QFrame(self.pg_historico)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_19.addWidget(self.label_5)

        self.tabela_historico = QTableWidget(self.frame_10)
        if (self.tabela_historico.columnCount() < 4):
            self.tabela_historico.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabela_historico.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabela_historico.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabela_historico.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabela_historico.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tabela_historico.rowCount() < 6):
            self.tabela_historico.setRowCount(6)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabela_historico.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabela_historico.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabela_historico.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabela_historico.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabela_historico.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabela_historico.setVerticalHeaderItem(5, __qtablewidgetitem9)
        self.tabela_historico.setObjectName(u"tabela_historico")

        self.verticalLayout_19.addWidget(self.tabela_historico)


        self.verticalLayout_7.addWidget(self.frame_10)

        self.Pages.addWidget(self.pg_historico)
        self.pg_enviar_doc = QWidget()
        self.pg_enviar_doc.setObjectName(u"pg_enviar_doc")
        self.verticalLayout_13 = QVBoxLayout(self.pg_enviar_doc)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_7 = QFrame(self.pg_enviar_doc)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_7)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_15 = QFrame(self.frame_7)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.frame_15)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)


        self.gridLayout.addWidget(self.frame_15, 0, 0, 1, 2)

        self.tipo_documento = QComboBox(self.frame_7)
        self.tipo_documento.addItem("")
        self.tipo_documento.addItem("")
        self.tipo_documento.addItem("")
        self.tipo_documento.addItem("")
        self.tipo_documento.addItem("")
        self.tipo_documento.setObjectName(u"tipo_documento")
        self.tipo_documento.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.tipo_documento, 1, 0, 1, 1)

        self.btn_arquivo_documento = QPushButton(self.frame_7)
        self.btn_arquivo_documento.setObjectName(u"btn_arquivo_documento")
        self.btn_arquivo_documento.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_arquivo_documento, 1, 1, 1, 1)

        self.btn_enviar_arquivo = QPushButton(self.frame_7)
        self.btn_enviar_arquivo.setObjectName(u"btn_enviar_arquivo")
        self.btn_enviar_arquivo.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_enviar_arquivo, 2, 1, 1, 1)


        self.verticalLayout_13.addWidget(self.frame_7)

        self.Pages.addWidget(self.pg_enviar_doc)
        self.pg_alteracao_perfil = QWidget()
        self.pg_alteracao_perfil.setObjectName(u"pg_alteracao_perfil")
        self.pg_alteracao_perfil.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.pg_alteracao_perfil)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_6 = QFrame(self.pg_alteracao_perfil)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_12.addWidget(self.label_11)

        self.txt_perfil_alterar_nome = QLineEdit(self.frame_6)
        self.txt_perfil_alterar_nome.setObjectName(u"txt_perfil_alterar_nome")

        self.verticalLayout_12.addWidget(self.txt_perfil_alterar_nome)

        self.txt_perfil_alterar_email = QLineEdit(self.frame_6)
        self.txt_perfil_alterar_email.setObjectName(u"txt_perfil_alterar_email")

        self.verticalLayout_12.addWidget(self.txt_perfil_alterar_email)

        self.txt_perfil_alterar_telefone = QLineEdit(self.frame_6)
        self.txt_perfil_alterar_telefone.setObjectName(u"txt_perfil_alterar_telefone")

        self.verticalLayout_12.addWidget(self.txt_perfil_alterar_telefone)

        self.btn_salvar_alteracoes = QPushButton(self.frame_6)
        self.btn_salvar_alteracoes.setObjectName(u"btn_salvar_alteracoes")
        self.btn_salvar_alteracoes.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_salvar_alteracoes.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"}\n"
"\n"
"")

        self.verticalLayout_12.addWidget(self.btn_salvar_alteracoes)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_3)


        self.verticalLayout_11.addWidget(self.frame_6)

        self.Pages.addWidget(self.pg_alteracao_perfil)
        self.pg_perfil = QWidget()
        self.pg_perfil.setObjectName(u"pg_perfil")
        self.verticalLayout_8 = QVBoxLayout(self.pg_perfil)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_5 = QFrame(self.pg_perfil)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.pg_perfil)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_9.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_9.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_9.addWidget(self.label_10)


        self.verticalLayout_8.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.pg_perfil)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.btn_alterar_dados = QPushButton(self.frame_3)
        self.btn_alterar_dados.setObjectName(u"btn_alterar_dados")
        self.btn_alterar_dados.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_dados.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"}\n"
"")

        self.verticalLayout_10.addWidget(self.btn_alterar_dados)


        self.verticalLayout_8.addWidget(self.frame_3)

        self.Pages.addWidget(self.pg_perfil)

        self.verticalLayout_14.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setStyleSheet(u"background: transparent;")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nome da Empresa", None))
        self.btn_home_menu.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_cadastrar_menu.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_historico_menu.setText(QCoreApplication.translate("MainWindow", u"Hist\u00f3rico", None))
        self.btn_enviar_menu.setText(QCoreApplication.translate("MainWindow", u"Enviar Documento", None))
        self.btn_perfil_menu.setText(QCoreApplication.translate("MainWindow", u"Perfil", None))
        self.btn_encerrar_menu.setText(QCoreApplication.translate("MainWindow", u"Encerrar", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.btn_toogle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Nome do Sistema</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">Seja Bem Vindo!</span></p><p align=\"center\"><img src=\":/icons/icons/cobra.png\"/></p></body></html>", None))
        self.btn_carregar_formulario.setText(QCoreApplication.translate("MainWindow", u"Formul\u00e1rio", None))
        self.btn_carregar_documentos.setText(QCoreApplication.translate("MainWindow", u"Documentos", None))
        self.txt_cadastro_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Nome", None))
        self.txt_cadastro_cpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  CPF", None))
        self.txt_cadastro_rg.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  RG", None))
        self.txt_cadastro_filiacao.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Fili\u00e7\u00e3o", None))
        self.txt_cadastro_endereco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Endere\u00e7o", None))
        self.txt_cadastro_nascimento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Data de Nascimento", None))
        self.txt_cadastro_cidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Cidade", None))
        self.txt_cadastro_estado.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Estado", None))
        self.txt_cadastro_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Telefone", None))
        self.txt_cadastro_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Email", None))
        self.btn_cadastro_enviar.setText(QCoreApplication.translate("MainWindow", u"Enviar Cadastro", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">Hist\u00f3rico de Cadastros</span></p></body></html>", None))
        ___qtablewidgetitem = self.tabela_historico.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem1 = self.tabela_historico.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Data do Cadastro", None));
        ___qtablewidgetitem2 = self.tabela_historico.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtablewidgetitem3 = self.tabela_historico.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Area destinada ao envio de documentos </span></p></body></html>", None))
        self.tipo_documento.setItemText(0, QCoreApplication.translate("MainWindow", u"Escolha o tipo de arquivo", None))
        self.tipo_documento.setItemText(1, QCoreApplication.translate("MainWindow", u"CPF", None))
        self.tipo_documento.setItemText(2, QCoreApplication.translate("MainWindow", u"RG", None))
        self.tipo_documento.setItemText(3, QCoreApplication.translate("MainWindow", u"CNH", None))
        self.tipo_documento.setItemText(4, QCoreApplication.translate("MainWindow", u"PASSAPORTE", None))

        self.btn_arquivo_documento.setText(QCoreApplication.translate("MainWindow", u"Arquivo", None))
        self.btn_enviar_arquivo.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">Altere seus Dados</span></p></body></html>", None))
        self.txt_perfil_alterar_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.txt_perfil_alterar_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"email", None))
        self.txt_perfil_alterar_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"telefone", None))
        self.btn_salvar_alteracoes.setText(QCoreApplication.translate("MainWindow", u"Salvar Altera\u00e7\u00f5es", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Perfil</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Nome do Usu\u00e1rio</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Email do Usu\u00e1rio</p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Telefone do Usu\u00e1rio</p></body></html>", None))
        self.btn_alterar_dados.setText(QCoreApplication.translate("MainWindow", u"Alterar meus dados", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nome da Empresa", None))
    # retranslateUi

