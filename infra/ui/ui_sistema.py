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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)
from infra.ui import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(942, 672)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.container_geral = QWidget(self.centralwidget)
        self.container_geral.setObjectName(u"container_geral")
        self.container_geral.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.gridLayout = QGridLayout(self.container_geral)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_fechado = QWidget(self.container_geral)
        self.menu_fechado.setObjectName(u"menu_fechado")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.menu_fechado.sizePolicy().hasHeightForWidth())
        self.menu_fechado.setSizePolicy(sizePolicy1)
        self.menu_fechado.setMaximumSize(QSize(55, 16777215))
        self.menu_fechado.setLayoutDirection(Qt.RightToLeft)
        self.menu_fechado.setStyleSheet(u"QWidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.465, y1:0.481682, x2:0, y2:0, stop:0.147727 rgba(0, 164, 218, 255), stop:0.931818 rgba(0, 219, 255, 255));\n"
"}")
        self.verticalLayout = QVBoxLayout(self.menu_fechado)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 0, 0, -1)
        self.frame_7 = QFrame(self.menu_fechado)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"QFrame{\n"
" background-color: transparent;\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_7)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, -1, 0, 9)
        self.btn_toogle_fechado = QPushButton(self.frame_7)
        self.btn_toogle_fechado.setObjectName(u"btn_toogle_fechado")
        self.btn_toogle_fechado.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_toogle_fechado.setLayoutDirection(Qt.RightToLeft)
        self.btn_toogle_fechado.setStyleSheet(u"\n"
"QPushButton {\n"
"	\n"
"	background-color: transparent;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-left-radius: 12px;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu_fechado.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toogle_fechado.setIcon(icon)
        self.btn_toogle_fechado.setIconSize(QSize(25, 25))
        self.btn_toogle_fechado.setCheckable(True)

        self.verticalLayout_16.addWidget(self.btn_toogle_fechado, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.menu_fechado)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setLayoutDirection(Qt.RightToLeft)
        self.frame_8.setStyleSheet(u"QFrame{\n"
" background-color: transparent;\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 32, 2, -1)
        self.btn_home_menu_fechado = QPushButton(self.frame_8)
        self.btn_home_menu_fechado.setObjectName(u"btn_home_menu_fechado")
        self.btn_home_menu_fechado.setMinimumSize(QSize(0, 40))
        self.btn_home_menu_fechado.setMaximumSize(QSize(16777215, 40))
        self.btn_home_menu_fechado.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home_menu_fechado.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: transparent;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-left-radius: 12px;\n"
"	text-align: center;\n"
"	padding-left: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/home_fechado.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home_menu_fechado.setIcon(icon1)
        self.btn_home_menu_fechado.setIconSize(QSize(30, 30))
        self.btn_home_menu_fechado.setCheckable(False)
        self.btn_home_menu_fechado.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.btn_home_menu_fechado)

        self.btn_perfil_menu_fechado = QPushButton(self.frame_8)
        self.btn_perfil_menu_fechado.setObjectName(u"btn_perfil_menu_fechado")
        self.btn_perfil_menu_fechado.setMinimumSize(QSize(0, 40))
        self.btn_perfil_menu_fechado.setMaximumSize(QSize(16777215, 40))
        self.btn_perfil_menu_fechado.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_perfil_menu_fechado.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: transparent;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-left-radius: 12px;\n"
"	text-align: center;\n"
"	padding-left: 10px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/user_fechado.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_perfil_menu_fechado.setIcon(icon2)
        self.btn_perfil_menu_fechado.setIconSize(QSize(30, 30))
        self.btn_perfil_menu_fechado.setCheckable(True)

        self.verticalLayout_3.addWidget(self.btn_perfil_menu_fechado)

        self.btn_cadastrar_menu_fechado = QPushButton(self.frame_8)
        self.btn_cadastrar_menu_fechado.setObjectName(u"btn_cadastrar_menu_fechado")
        self.btn_cadastrar_menu_fechado.setMinimumSize(QSize(0, 40))
        self.btn_cadastrar_menu_fechado.setMaximumSize(QSize(16777215, 40))
        self.btn_cadastrar_menu_fechado.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar_menu_fechado.setLayoutDirection(Qt.RightToLeft)
        self.btn_cadastrar_menu_fechado.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: transparent;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-left-radius: 12px;\n"
"	text-align: center;\n"
"	padding-left: 10px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/cadastros.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastrar_menu_fechado.setIcon(icon3)
        self.btn_cadastrar_menu_fechado.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.btn_cadastrar_menu_fechado)

        self.btn_enviardocumento_menu_fechado = QPushButton(self.frame_8)
        self.btn_enviardocumento_menu_fechado.setObjectName(u"btn_enviardocumento_menu_fechado")
        self.btn_enviardocumento_menu_fechado.setMinimumSize(QSize(0, 40))
        self.btn_enviardocumento_menu_fechado.setMaximumSize(QSize(16777215, 40))
        self.btn_enviardocumento_menu_fechado.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_enviardocumento_menu_fechado.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: transparent;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-left-radius: 12px;\n"
"	text-align: center;\n"
"	padding-left: 10px;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/upload_fechado.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_enviardocumento_menu_fechado.setIcon(icon4)
        self.btn_enviardocumento_menu_fechado.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.btn_enviardocumento_menu_fechado)

        self.btn_historico_menu_fechado = QPushButton(self.frame_8)
        self.btn_historico_menu_fechado.setObjectName(u"btn_historico_menu_fechado")
        self.btn_historico_menu_fechado.setMinimumSize(QSize(0, 40))
        self.btn_historico_menu_fechado.setMaximumSize(QSize(16777215, 40))
        self.btn_historico_menu_fechado.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_historico_menu_fechado.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: transparent;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-left-radius: 12px;\n"
"	text-align: center;\n"
"	padding-left: 10px;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/history.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_historico_menu_fechado.setIcon(icon5)
        self.btn_historico_menu_fechado.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.btn_historico_menu_fechado)


        self.verticalLayout.addWidget(self.frame_8, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 310, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_encerrar_menu_fechado = QPushButton(self.menu_fechado)
        self.btn_encerrar_menu_fechado.setObjectName(u"btn_encerrar_menu_fechado")
        self.btn_encerrar_menu_fechado.setMinimumSize(QSize(0, 40))
        self.btn_encerrar_menu_fechado.setMaximumSize(QSize(16777215, 40))
        self.btn_encerrar_menu_fechado.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_encerrar_menu_fechado.setLayoutDirection(Qt.RightToLeft)
        self.btn_encerrar_menu_fechado.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(255, 75, 75);\n"
"	\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: transparent;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-left-radius: 12px;\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/out.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_encerrar_menu_fechado.setIcon(icon6)
        self.btn_encerrar_menu_fechado.setIconSize(QSize(35, 35))

        self.verticalLayout.addWidget(self.btn_encerrar_menu_fechado)


        self.gridLayout.addWidget(self.menu_fechado, 0, 0, 3, 1)

        self.menu_aberto = QWidget(self.container_geral)
        self.menu_aberto.setObjectName(u"menu_aberto")
        self.menu_aberto.setStyleSheet(u"QWidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.465, y1:0.481682, x2:0, y2:0, stop:0.147727 rgba(0, 164, 218, 255), stop:0.931818 rgba(0, 219, 255, 255));\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.menu_aberto)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, -1)
        self.frame_9 = QFrame(self.menu_aberto)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QFrame{\n"
" background-color: transparent;\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, 1)
        self.icone_menu_aberto = QLabel(self.frame_9)
        self.icone_menu_aberto.setObjectName(u"icone_menu_aberto")
        self.icone_menu_aberto.setMaximumSize(QSize(50, 50))
        self.icone_menu_aberto.setStyleSheet(u"QLabel{\n"
"	background-color:transparent;\n"
"}")
        self.icone_menu_aberto.setPixmap(QPixmap(u":/icons/icons/cobra.png"))
        self.icone_menu_aberto.setScaledContents(True)
        self.icone_menu_aberto.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.icone_menu_aberto)

        self.nome_empresa_menu_aberto = QLabel(self.frame_9)
        self.nome_empresa_menu_aberto.setObjectName(u"nome_empresa_menu_aberto")
        self.nome_empresa_menu_aberto.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"	color: rgb(255, 255, 255);\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 15pt;\n"
"	font-weight:600;\n"
"}")
        self.nome_empresa_menu_aberto.setScaledContents(False)
        self.nome_empresa_menu_aberto.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.nome_empresa_menu_aberto)

        self.btn_toogle_aberto = QPushButton(self.frame_9)
        self.btn_toogle_aberto.setObjectName(u"btn_toogle_aberto")
        self.btn_toogle_aberto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_toogle_aberto.setStyleSheet(u"\n"
"QPushButton {\n"
"	\n"
"	background-color: transparent;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-left-radius: 12px;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/menu_aberto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toogle_aberto.setIcon(icon7)
        self.btn_toogle_aberto.setIconSize(QSize(25, 25))
        self.btn_toogle_aberto.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btn_toogle_aberto)


        self.verticalLayout_4.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.menu_aberto)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"QFrame{\n"
" background-color: transparent;\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 24, 0, -1)
        self.btn_home_menu_aberto = QPushButton(self.frame_10)
        self.btn_home_menu_aberto.setObjectName(u"btn_home_menu_aberto")
        self.btn_home_menu_aberto.setMinimumSize(QSize(0, 40))
        self.btn_home_menu_aberto.setMaximumSize(QSize(16777215, 40))
        self.btn_home_menu_aberto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home_menu_aberto.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: transparent;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-left-radius: 12px;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}")
        self.btn_home_menu_aberto.setIcon(icon1)
        self.btn_home_menu_aberto.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.btn_home_menu_aberto)

        self.btn_perfil_menu_aberto = QPushButton(self.frame_10)
        self.btn_perfil_menu_aberto.setObjectName(u"btn_perfil_menu_aberto")
        self.btn_perfil_menu_aberto.setMinimumSize(QSize(0, 40))
        self.btn_perfil_menu_aberto.setMaximumSize(QSize(16777215, 40))
        self.btn_perfil_menu_aberto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_perfil_menu_aberto.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: transparent;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-left-radius: 12px;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}")
        self.btn_perfil_menu_aberto.setIcon(icon2)
        self.btn_perfil_menu_aberto.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.btn_perfil_menu_aberto)

        self.btn_cadastrar_menu_aberto = QPushButton(self.frame_10)
        self.btn_cadastrar_menu_aberto.setObjectName(u"btn_cadastrar_menu_aberto")
        self.btn_cadastrar_menu_aberto.setMinimumSize(QSize(0, 40))
        self.btn_cadastrar_menu_aberto.setMaximumSize(QSize(16777215, 40))
        self.btn_cadastrar_menu_aberto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar_menu_aberto.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: transparent;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-left-radius: 12px;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}")
        self.btn_cadastrar_menu_aberto.setIcon(icon3)
        self.btn_cadastrar_menu_aberto.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.btn_cadastrar_menu_aberto)

        self.btn_enviardocumento_menu_aberto = QPushButton(self.frame_10)
        self.btn_enviardocumento_menu_aberto.setObjectName(u"btn_enviardocumento_menu_aberto")
        self.btn_enviardocumento_menu_aberto.setMinimumSize(QSize(0, 40))
        self.btn_enviardocumento_menu_aberto.setMaximumSize(QSize(16777215, 40))
        self.btn_enviardocumento_menu_aberto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_enviardocumento_menu_aberto.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: transparent;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-left-radius: 12px;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}")
        self.btn_enviardocumento_menu_aberto.setIcon(icon4)
        self.btn_enviardocumento_menu_aberto.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.btn_enviardocumento_menu_aberto)

        self.btn_historico_menu_aberto = QPushButton(self.frame_10)
        self.btn_historico_menu_aberto.setObjectName(u"btn_historico_menu_aberto")
        self.btn_historico_menu_aberto.setMinimumSize(QSize(0, 40))
        self.btn_historico_menu_aberto.setMaximumSize(QSize(16777215, 40))
        self.btn_historico_menu_aberto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_historico_menu_aberto.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: transparent;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-left-radius: 12px;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}")
        self.btn_historico_menu_aberto.setIcon(icon5)
        self.btn_historico_menu_aberto.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.btn_historico_menu_aberto)


        self.verticalLayout_4.addWidget(self.frame_10)

        self.verticalSpacer_2 = QSpacerItem(20, 310, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.btn_encerrar_menu_aberto = QPushButton(self.menu_aberto)
        self.btn_encerrar_menu_aberto.setObjectName(u"btn_encerrar_menu_aberto")
        self.btn_encerrar_menu_aberto.setMinimumSize(QSize(0, 40))
        self.btn_encerrar_menu_aberto.setMaximumSize(QSize(16777215, 40))
        self.btn_encerrar_menu_aberto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_encerrar_menu_aberto.setLayoutDirection(Qt.LeftToRight)
        self.btn_encerrar_menu_aberto.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(255, 75, 75);\n"
"	\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: transparent;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-left-radius: 12px;\n"
"}\n"
"")
        self.btn_encerrar_menu_aberto.setIcon(icon6)
        self.btn_encerrar_menu_aberto.setIconSize(QSize(35, 35))

        self.verticalLayout_4.addWidget(self.btn_encerrar_menu_aberto)


        self.gridLayout.addWidget(self.menu_aberto, 0, 1, 3, 1)

        self.cabecalho = QWidget(self.container_geral)
        self.cabecalho.setObjectName(u"cabecalho")
        self.cabecalho.setStyleSheet(u"QWidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.465, y1:0.481682, x2:0.983, y2:1, stop:0.147727 rgba(0, 164, 218, 255), stop:0.931818 rgba(0, 219, 255, 255));\n"
"\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.cabecalho)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.txt_nome_sistema = QLabel(self.cabecalho)
        self.txt_nome_sistema.setObjectName(u"txt_nome_sistema")
        self.txt_nome_sistema.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"	color: rgb(255, 255, 255);\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 15pt;\n"
"	font-weight:600;\n"
"}")
        self.txt_nome_sistema.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.txt_nome_sistema)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.gridLayout.addWidget(self.cabecalho, 0, 2, 1, 1)

        self.tela_central = QWidget(self.container_geral)
        self.tela_central.setObjectName(u"tela_central")
        sizePolicy1.setHeightForWidth(self.tela_central.sizePolicy().hasHeightForWidth())
        self.tela_central.setSizePolicy(sizePolicy1)
        self.tela_central.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.tela_central)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Pages = QStackedWidget(self.tela_central)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"QStackedWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.horizontalLayout_6 = QHBoxLayout(self.pg_home)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.conteudo_tela_home = QWidget(self.pg_home)
        self.conteudo_tela_home.setObjectName(u"conteudo_tela_home")
        self.verticalLayout_9 = QVBoxLayout(self.conteudo_tela_home)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.conteudo = QWidget(self.conteudo_tela_home)
        self.conteudo.setObjectName(u"conteudo")
        self.verticalLayout_8 = QVBoxLayout(self.conteudo)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.boas_vindas = QWidget(self.conteudo)
        self.boas_vindas.setObjectName(u"boas_vindas")
        self.verticalLayout_7 = QVBoxLayout(self.boas_vindas)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lbl_saudacao = QLabel(self.boas_vindas)
        self.lbl_saudacao.setObjectName(u"lbl_saudacao")
        self.lbl_saudacao.setStyleSheet(u"QLabel {\n"
"	font-family: Arial, sans-serif;\n"
"	background-color: transparent;\n"
"	font-size: 14pt;\n"
"	color: rgb(0,0,0);\n"
"	border: 0px;\n"
"	font-weight:600;\n"
"}")

        self.verticalLayout_7.addWidget(self.lbl_saudacao)

        self.txt_nome_perfil_home = QLabel(self.boas_vindas)
        self.txt_nome_perfil_home.setObjectName(u"txt_nome_perfil_home")
        self.txt_nome_perfil_home.setStyleSheet(u"QLabel {\n"
"	font-family: Arial, sans-serif;\n"
"	background-color: transparent;\n"
"	font-size: 14pt;\n"
"	color: rgb(0,0,0);\n"
"	border: 0px;\n"
"	font-weight:600;\n"
"}")

        self.verticalLayout_7.addWidget(self.txt_nome_perfil_home, 0, Qt.AlignHCenter)


        self.verticalLayout_8.addWidget(self.boas_vindas, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.Logo_Central = QWidget(self.conteudo)
        self.Logo_Central.setObjectName(u"Logo_Central")
        self.verticalLayout_6 = QVBoxLayout(self.Logo_Central)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_icone_empresa_tela_home = QLabel(self.Logo_Central)
        self.lbl_icone_empresa_tela_home.setObjectName(u"lbl_icone_empresa_tela_home")
        self.lbl_icone_empresa_tela_home.setPixmap(QPixmap(u":/icons/icons/cobra.png"))
        self.lbl_icone_empresa_tela_home.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.lbl_icone_empresa_tela_home)


        self.verticalLayout_8.addWidget(self.Logo_Central)


        self.verticalLayout_9.addWidget(self.conteudo, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_6.addWidget(self.conteudo_tela_home)

        self.Pages.addWidget(self.pg_home)
        self.pg_perfil = QWidget()
        self.pg_perfil.setObjectName(u"pg_perfil")
        self.horizontalLayout_7 = QHBoxLayout(self.pg_perfil)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.conteudo_tela_perfil = QWidget(self.pg_perfil)
        self.conteudo_tela_perfil.setObjectName(u"conteudo_tela_perfil")
        self.verticalLayout_17 = QVBoxLayout(self.conteudo_tela_perfil)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label = QLabel(self.conteudo_tela_perfil)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 14pt;\n"
"	color: rgb(0,0,0);\n"
"}")

        self.verticalLayout_17.addWidget(self.label)

        self.widget = QWidget(self.conteudo_tela_perfil)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(300, 200))
        self.widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgba(0, 164, 218, 0.2);\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-right-radius: 20px;\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.widget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_4)

        self.txt_nome_perfil = QLabel(self.widget)
        self.txt_nome_perfil.setObjectName(u"txt_nome_perfil")
        self.txt_nome_perfil.setStyleSheet(u"QLabel{\n"
"	background-color:transparent;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 16px;\n"
"	color: rgb(0,0,0);\n"
"	text-align: center;\n"
"}")

        self.verticalLayout_10.addWidget(self.txt_nome_perfil, 0, Qt.AlignHCenter)

        self.txt_email_perfil = QLabel(self.widget)
        self.txt_email_perfil.setObjectName(u"txt_email_perfil")
        self.txt_email_perfil.setStyleSheet(u"QLabel{\n"
"	background-color:transparent;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 12px;\n"
"	color: rgb(0,0,0);\n"
"	text-align: center;\n"
"}")

        self.verticalLayout_10.addWidget(self.txt_email_perfil, 0, Qt.AlignHCenter)

        self.txt_telefone_perfil = QLabel(self.widget)
        self.txt_telefone_perfil.setObjectName(u"txt_telefone_perfil")
        self.txt_telefone_perfil.setStyleSheet(u"QLabel{\n"
"	background-color:transparent;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 12px;\n"
"	color: rgb(0,0,0);\n"
"	text-align: center;\n"
"}")

        self.verticalLayout_10.addWidget(self.txt_telefone_perfil, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_3)


        self.verticalLayout_17.addWidget(self.widget, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.widget_2 = QWidget(self.conteudo_tela_perfil)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_18 = QVBoxLayout(self.widget_2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.btn_alterar_dados = QPushButton(self.widget_2)
        self.btn_alterar_dados.setObjectName(u"btn_alterar_dados")
        self.btn_alterar_dados.setMinimumSize(QSize(250, 30))
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
"	border-radius: 10px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_alterar_dados.setIcon(icon8)

        self.verticalLayout_18.addWidget(self.btn_alterar_dados)


        self.verticalLayout_17.addWidget(self.widget_2, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.conteudo_tela_perfil)

        self.Pages.addWidget(self.pg_perfil)
        self.pg_alteracao_perfil = QWidget()
        self.pg_alteracao_perfil.setObjectName(u"pg_alteracao_perfil")
        self.horizontalLayout_8 = QHBoxLayout(self.pg_alteracao_perfil)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.conteud_tela_alteracao_perfil = QWidget(self.pg_alteracao_perfil)
        self.conteud_tela_alteracao_perfil.setObjectName(u"conteud_tela_alteracao_perfil")
        self.verticalLayout_19 = QVBoxLayout(self.conteud_tela_alteracao_perfil)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.widget_3 = QWidget(self.conteud_tela_alteracao_perfil)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(500, 0))
        self.widget_3.setStyleSheet(u"QWidget{\n"
"	background-color: rgba(0, 164, 218, 0.2);\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-right-radius: 20px;\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.widget_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_6)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel {\n"
"	font-family: Arial, sans-serif;\n"
"	background-color: transparent;\n"
"	font-size: 14pt;\n"
"	color: rgb(0,0,0);\n"
"}")

        self.verticalLayout_11.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.txt_perfil_alterar_nome = QLineEdit(self.widget_3)
        self.txt_perfil_alterar_nome.setObjectName(u"txt_perfil_alterar_nome")
        self.txt_perfil_alterar_nome.setMinimumSize(QSize(0, 30))
        self.txt_perfil_alterar_nome.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgba(0, 0, 0, 20);\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 10pt;\n"
"	color: rgb(0,0,0);\n"
"}")

        self.verticalLayout_11.addWidget(self.txt_perfil_alterar_nome)

        self.txt_perfil_alterar_email = QLineEdit(self.widget_3)
        self.txt_perfil_alterar_email.setObjectName(u"txt_perfil_alterar_email")
        self.txt_perfil_alterar_email.setMinimumSize(QSize(0, 30))
        self.txt_perfil_alterar_email.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgba(0, 0, 0, 20);\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 10pt;\n"
"	color: rgb(0,0,0);\n"
"}")

        self.verticalLayout_11.addWidget(self.txt_perfil_alterar_email)

        self.txt_perfil_alterar_telefone = QLineEdit(self.widget_3)
        self.txt_perfil_alterar_telefone.setObjectName(u"txt_perfil_alterar_telefone")
        self.txt_perfil_alterar_telefone.setMinimumSize(QSize(0, 30))
        self.txt_perfil_alterar_telefone.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgba(0, 0, 0, 20);\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 10pt;\n"
"	color: rgb(0,0,0);\n"
"}")

        self.verticalLayout_11.addWidget(self.txt_perfil_alterar_telefone)

        self.btn_salvar_alteracoes = QPushButton(self.widget_3)
        self.btn_salvar_alteracoes.setObjectName(u"btn_salvar_alteracoes")
        self.btn_salvar_alteracoes.setMinimumSize(QSize(250, 30))
        self.btn_salvar_alteracoes.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_salvar_alteracoes.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(87, 175, 0);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"	border-radius: 10px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_salvar_alteracoes.setIcon(icon9)

        self.verticalLayout_11.addWidget(self.btn_salvar_alteracoes, 0, Qt.AlignHCenter)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_5)


        self.verticalLayout_19.addWidget(self.widget_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_8.addWidget(self.conteud_tela_alteracao_perfil)

        self.Pages.addWidget(self.pg_alteracao_perfil)
        self.pg_cadastrar = QWidget()
        self.pg_cadastrar.setObjectName(u"pg_cadastrar")
        self.horizontalLayout_9 = QHBoxLayout(self.pg_cadastrar)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.conteudo_tela_cadastro = QWidget(self.pg_cadastrar)
        self.conteudo_tela_cadastro.setObjectName(u"conteudo_tela_cadastro")
        self.conteudo_tela_cadastro.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.verticalLayout_22 = QVBoxLayout(self.conteudo_tela_cadastro)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_2 = QLabel(self.conteudo_tela_cadastro)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"	font-family: Arial, sans-serif;\n"
"	background-color: transparent;\n"
"	font-size: 14pt;\n"
"	color: rgb(0,0,0);\n"
"	font-weight:600;\n"
"}")

        self.verticalLayout_22.addWidget(self.label_2)

        self.frame = QFrame(self.conteudo_tela_cadastro)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0,0,0);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(0, 164, 218, 0.2);\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-right-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.btn_carregar_formulario = QPushButton(self.frame_2)
        self.btn_carregar_formulario.setObjectName(u"btn_carregar_formulario")
        self.btn_carregar_formulario.setMinimumSize(QSize(250, 30))
        self.btn_carregar_formulario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_carregar_formulario.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"	color: rgb(0,0,0);\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/import.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_carregar_formulario.setIcon(icon10)
        self.btn_carregar_formulario.setIconSize(QSize(18, 18))

        self.verticalLayout_12.addWidget(self.btn_carregar_formulario, 0, Qt.AlignHCenter)

        self.btn_limpar_formulario = QPushButton(self.frame_2)
        self.btn_limpar_formulario.setObjectName(u"btn_limpar_formulario")
        self.btn_limpar_formulario.setMinimumSize(QSize(250, 30))
        self.btn_limpar_formulario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_limpar_formulario.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(255, 75, 75);\n"
"	\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	color: rgb(0,0,0);\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_limpar_formulario.setIcon(icon11)
        self.btn_limpar_formulario.setIconSize(QSize(18, 18))

        self.verticalLayout_12.addWidget(self.btn_limpar_formulario, 0, Qt.AlignHCenter)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_7)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	color: rgb(0,0,0);\n"
"}")

        self.verticalLayout_12.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.txt_cadastro_nome = QLineEdit(self.frame_2)
        self.txt_cadastro_nome.setObjectName(u"txt_cadastro_nome")
        self.txt_cadastro_nome.setMinimumSize(QSize(0, 30))
        self.txt_cadastro_nome.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgba(0, 0, 0, 20);\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 10pt;\n"
"	color: rgb(0,0,0);\n"
"}")

        self.verticalLayout_12.addWidget(self.txt_cadastro_nome)

        self.txt_cadastro_cpf = QLineEdit(self.frame_2)
        self.txt_cadastro_cpf.setObjectName(u"txt_cadastro_cpf")
        self.txt_cadastro_cpf.setMinimumSize(QSize(0, 30))
        self.txt_cadastro_cpf.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgba(0, 0, 0, 20);\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 10pt;\n"
"	color: rgb(0,0,0);\n"
"}")

        self.verticalLayout_12.addWidget(self.txt_cadastro_cpf)

        self.txt_cadastro_rg = QLineEdit(self.frame_2)
        self.txt_cadastro_rg.setObjectName(u"txt_cadastro_rg")
        self.txt_cadastro_rg.setMinimumSize(QSize(0, 30))
        self.txt_cadastro_rg.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgba(0, 0, 0, 20);\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 10pt;\n"
"	color: rgb(0,0,0);\n"
"}")

        self.verticalLayout_12.addWidget(self.txt_cadastro_rg)

        self.txt_cadastro_filiacao = QLineEdit(self.frame_2)
        self.txt_cadastro_filiacao.setObjectName(u"txt_cadastro_filiacao")
        self.txt_cadastro_filiacao.setMinimumSize(QSize(0, 30))
        self.txt_cadastro_filiacao.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgba(0, 0, 0, 20);\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 10pt;\n"
"	color: rgb(0,0,0);\n"
"}")

        self.verticalLayout_12.addWidget(self.txt_cadastro_filiacao)

        self.txt_cadastro_endereco = QLineEdit(self.frame_2)
        self.txt_cadastro_endereco.setObjectName(u"txt_cadastro_endereco")
        self.txt_cadastro_endereco.setMinimumSize(QSize(0, 30))
        self.txt_cadastro_endereco.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgba(0, 0, 0, 20);\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 10pt;\n"
"	color: rgb(0,0,0);\n"
"}")

        self.verticalLayout_12.addWidget(self.txt_cadastro_endereco)

        self.txt_cadastro_nascimento = QLineEdit(self.frame_2)
        self.txt_cadastro_nascimento.setObjectName(u"txt_cadastro_nascimento")
        self.txt_cadastro_nascimento.setMinimumSize(QSize(0, 30))
        self.txt_cadastro_nascimento.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgba(0, 0, 0, 20);\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 10pt;\n"
"	color: rgb(0,0,0);\n"
"}")

        self.verticalLayout_12.addWidget(self.txt_cadastro_nascimento)

        self.txt_cadastro_cidade = QLineEdit(self.frame_2)
        self.txt_cadastro_cidade.setObjectName(u"txt_cadastro_cidade")
        self.txt_cadastro_cidade.setMinimumSize(QSize(0, 30))
        self.txt_cadastro_cidade.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgba(0, 0, 0, 20);\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 10pt;\n"
"	color: rgb(0,0,0);\n"
"}")

        self.verticalLayout_12.addWidget(self.txt_cadastro_cidade)

        self.txt_cadastro_estado = QLineEdit(self.frame_2)
        self.txt_cadastro_estado.setObjectName(u"txt_cadastro_estado")
        self.txt_cadastro_estado.setMinimumSize(QSize(0, 30))
        self.txt_cadastro_estado.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgba(0, 0, 0, 20);\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 10pt;\n"
"	color: rgb(0,0,0);\n"
"}")

        self.verticalLayout_12.addWidget(self.txt_cadastro_estado)

        self.txt_cadastro_telefone = QLineEdit(self.frame_2)
        self.txt_cadastro_telefone.setObjectName(u"txt_cadastro_telefone")
        self.txt_cadastro_telefone.setMinimumSize(QSize(0, 30))
        self.txt_cadastro_telefone.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgba(0, 0, 0, 20);\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 10pt;\n"
"	color: rgb(0,0,0);\n"
"}")

        self.verticalLayout_12.addWidget(self.txt_cadastro_telefone)

        self.txt_cadastro_email = QLineEdit(self.frame_2)
        self.txt_cadastro_email.setObjectName(u"txt_cadastro_email")
        self.txt_cadastro_email.setMinimumSize(QSize(0, 30))
        self.txt_cadastro_email.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgba(0, 0, 0, 20);\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 10pt;\n"
"	color: rgb(0,0,0);\n"
"}")

        self.verticalLayout_12.addWidget(self.txt_cadastro_email)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_8)


        self.horizontalLayout_12.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(0, 164, 218, 0.2);\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-right-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_3)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.btn_carregar_documentos = QPushButton(self.frame_3)
        self.btn_carregar_documentos.setObjectName(u"btn_carregar_documentos")
        self.btn_carregar_documentos.setMinimumSize(QSize(0, 30))
        self.btn_carregar_documentos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_carregar_documentos.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_carregar_documentos.setIcon(icon12)
        self.btn_carregar_documentos.setIconSize(QSize(20, 20))

        self.verticalLayout_21.addWidget(self.btn_carregar_documentos)

        self.btn_remover_lista_cadastro = QPushButton(self.frame_3)
        self.btn_remover_lista_cadastro.setObjectName(u"btn_remover_lista_cadastro")
        self.btn_remover_lista_cadastro.setMinimumSize(QSize(0, 30))
        self.btn_remover_lista_cadastro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_remover_lista_cadastro.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(255, 75, 75);\n"
"	\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	color: rgb(0,0,0);\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_remover_lista_cadastro.setIcon(icon13)
        self.btn_remover_lista_cadastro.setIconSize(QSize(15, 15))

        self.verticalLayout_21.addWidget(self.btn_remover_lista_cadastro)

        self.btn_limpar_lista_cadastro = QPushButton(self.frame_3)
        self.btn_limpar_lista_cadastro.setObjectName(u"btn_limpar_lista_cadastro")
        self.btn_limpar_lista_cadastro.setMinimumSize(QSize(0, 30))
        self.btn_limpar_lista_cadastro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_limpar_lista_cadastro.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(255, 75, 75);\n"
"	\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.btn_limpar_lista_cadastro.setIcon(icon11)
        self.btn_limpar_lista_cadastro.setIconSize(QSize(18, 18))

        self.verticalLayout_21.addWidget(self.btn_limpar_lista_cadastro)

        self.lista_documentos_cadastro = QListWidget(self.frame_3)
        self.lista_documentos_cadastro.setObjectName(u"lista_documentos_cadastro")
        sizePolicy1.setHeightForWidth(self.lista_documentos_cadastro.sizePolicy().hasHeightForWidth())
        self.lista_documentos_cadastro.setSizePolicy(sizePolicy1)
        self.lista_documentos_cadastro.setMaximumSize(QSize(250, 250))
        self.lista_documentos_cadastro.setStyleSheet(u"QListWidget{\n"
"	background-color: white;\n"
"	color: rgb(0,0,0);\n"
"	border-radius: 0px;\n"
"	border: 1px solid black;\n"
"}")
        self.lista_documentos_cadastro.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lista_documentos_cadastro.setProperty("showDropIndicator", False)
        self.lista_documentos_cadastro.setMovement(QListView.Static)
        self.lista_documentos_cadastro.setFlow(QListView.LeftToRight)
        self.lista_documentos_cadastro.setProperty("isWrapping", True)
        self.lista_documentos_cadastro.setViewMode(QListView.IconMode)

        self.verticalLayout_21.addWidget(self.lista_documentos_cadastro)

        self.miniatura_documento = QLabel(self.frame_3)
        self.miniatura_documento.setObjectName(u"miniatura_documento")
        self.miniatura_documento.setMinimumSize(QSize(250, 250))
        self.miniatura_documento.setMaximumSize(QSize(250, 250))
        self.miniatura_documento.setStyleSheet(u"QLabel{\n"
"    border-radius: 2px;\n"
"	background-color: transparent;\n"
"	border: 1px solid black;\n"
"    text-align: center;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.miniatura_documento.setScaledContents(True)
        self.miniatura_documento.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.miniatura_documento)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(250, 250))
        self.frame_4.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_4)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.btn_cadastro_enviar = QPushButton(self.frame_4)
        self.btn_cadastro_enviar.setObjectName(u"btn_cadastro_enviar")
        self.btn_cadastro_enviar.setMinimumSize(QSize(0, 30))
        self.btn_cadastro_enviar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastro_enviar.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(87, 175, 0);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"	border-radius: 10px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"\n"
"")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/upload_aberto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastro_enviar.setIcon(icon14)

        self.verticalLayout_20.addWidget(self.btn_cadastro_enviar)


        self.verticalLayout_21.addWidget(self.frame_4)


        self.horizontalLayout_12.addWidget(self.frame_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_22.addWidget(self.frame)


        self.horizontalLayout_9.addWidget(self.conteudo_tela_cadastro)

        self.Pages.addWidget(self.pg_cadastrar)
        self.pg_enviar_doc = QWidget()
        self.pg_enviar_doc.setObjectName(u"pg_enviar_doc")
        self.horizontalLayout_10 = QHBoxLayout(self.pg_enviar_doc)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.conteudo_tela_enviar_docs = QWidget(self.pg_enviar_doc)
        self.conteudo_tela_enviar_docs.setObjectName(u"conteudo_tela_enviar_docs")
        self.gridLayout_3 = QGridLayout(self.conteudo_tela_enviar_docs)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_6 = QFrame(self.conteudo_tela_enviar_docs)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(0, 164, 218, 0.2);\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-right-radius: 20px;\n"
"}\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 8pt;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.label_6)

        self.txt_pesquisa_cliente = QLineEdit(self.frame_6)
        self.txt_pesquisa_cliente.setObjectName(u"txt_pesquisa_cliente")
        self.txt_pesquisa_cliente.setMinimumSize(QSize(250, 30))

        self.verticalLayout_13.addWidget(self.txt_pesquisa_cliente)

        self.tipo_documento = QComboBox(self.frame_6)
        self.tipo_documento.addItem("")
        self.tipo_documento.addItem("")
        self.tipo_documento.addItem("")
        self.tipo_documento.addItem("")
        self.tipo_documento.addItem("")
        self.tipo_documento.addItem("")
        self.tipo_documento.addItem("")
        self.tipo_documento.setObjectName(u"tipo_documento")
        self.tipo_documento.setCursor(QCursor(Qt.PointingHandCursor))
        self.tipo_documento.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0,0,0);\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 10pt;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"\n"
"QComboBox::down-arrow-icon {\n"
"  background-color: rgb(0,0,0);\n"
"  color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox::list {\n"
"  background-color: rgb(255, 255, 255);\n"
"  color: rgb(0, 0, 0); \n"
"}\n"
"\n"
"QComboBox::editField {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0,0,0);\n"
"}")

        self.verticalLayout_13.addWidget(self.tipo_documento)

        self.btn_arquivo_documento = QPushButton(self.frame_6)
        self.btn_arquivo_documento.setObjectName(u"btn_arquivo_documento")
        self.btn_arquivo_documento.setMinimumSize(QSize(250, 30))
        self.btn_arquivo_documento.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_arquivo_documento.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.btn_arquivo_documento.setIcon(icon12)
        self.btn_arquivo_documento.setIconSize(QSize(20, 20))

        self.verticalLayout_13.addWidget(self.btn_arquivo_documento, 0, Qt.AlignHCenter)

        self.btn_remover_doc = QPushButton(self.frame_6)
        self.btn_remover_doc.setObjectName(u"btn_remover_doc")
        self.btn_remover_doc.setMinimumSize(QSize(250, 30))
        self.btn_remover_doc.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_remover_doc.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(255, 75, 75);\n"
"	\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.btn_remover_doc.setIcon(icon11)
        self.btn_remover_doc.setIconSize(QSize(18, 18))

        self.verticalLayout_13.addWidget(self.btn_remover_doc, 0, Qt.AlignHCenter)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_10)

        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_7)

        self.lista_envio_documento = QListWidget(self.frame_6)
        self.lista_envio_documento.setObjectName(u"lista_envio_documento")
        self.lista_envio_documento.setMaximumSize(QSize(16777215, 100))
        self.lista_envio_documento.setStyleSheet(u"QListWidget{\n"
"	background-color: white;\n"
"	color: rgb(0,0,0);\n"
"	border-radius: 0px;\n"
"	border: 1px solid black;\n"
"}")
        self.lista_envio_documento.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_13.addWidget(self.lista_envio_documento, 0, Qt.AlignHCenter)

        self.amostra_imagem = QLabel(self.frame_6)
        self.amostra_imagem.setObjectName(u"amostra_imagem")
        self.amostra_imagem.setMinimumSize(QSize(250, 250))
        self.amostra_imagem.setMaximumSize(QSize(250, 250))
        self.amostra_imagem.setStyleSheet(u"QLabel{\n"
"    border-radius: 2px;\n"
"	background-color: transparent;\n"
"	border: 1px solid black;\n"
"    text-align: center;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.amostra_imagem.setScaledContents(True)
        self.amostra_imagem.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.amostra_imagem, 0, Qt.AlignHCenter)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_9)


        self.gridLayout_3.addWidget(self.frame_6, 0, 0, 1, 1, Qt.AlignHCenter)

        self.frame_5 = QFrame(self.conteudo_tela_enviar_docs)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_5)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_4)

        self.txt_dados_documento = QTextEdit(self.frame_5)
        self.txt_dados_documento.setObjectName(u"txt_dados_documento")
        self.txt_dados_documento.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))

        self.verticalLayout_23.addWidget(self.txt_dados_documento)

        self.btn_enviar_arquivo = QPushButton(self.frame_5)
        self.btn_enviar_arquivo.setObjectName(u"btn_enviar_arquivo")
        self.btn_enviar_arquivo.setMinimumSize(QSize(250, 30))
        self.btn_enviar_arquivo.setMaximumSize(QSize(250, 16777215))
        self.btn_enviar_arquivo.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(87, 175, 0);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"	border-radius: 10px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"\n"
"")
        self.btn_enviar_arquivo.setIcon(icon14)

        self.verticalLayout_23.addWidget(self.btn_enviar_arquivo, 0, Qt.AlignHCenter)


        self.gridLayout_3.addWidget(self.frame_5, 0, 1, 1, 1)


        self.horizontalLayout_10.addWidget(self.conteudo_tela_enviar_docs)

        self.Pages.addWidget(self.pg_enviar_doc)
        self.pg_historico = QWidget()
        self.pg_historico.setObjectName(u"pg_historico")
        self.pg_historico.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.horizontalLayout_11 = QHBoxLayout(self.pg_historico)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.conteudo_tela_historico = QWidget(self.pg_historico)
        self.conteudo_tela_historico.setObjectName(u"conteudo_tela_historico")
        self.conteudo_tela_historico.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.verticalLayout_14 = QVBoxLayout(self.conteudo_tela_historico)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.tabWidget = QTabWidget(self.conteudo_tela_historico)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabela_historico_cadastros = QTableWidget(self.tab)
        if (self.tabela_historico_cadastros.columnCount() < 3):
            self.tabela_historico_cadastros.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabela_historico_cadastros.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabela_historico_cadastros.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabela_historico_cadastros.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tabela_historico_cadastros.rowCount() < 10):
            self.tabela_historico_cadastros.setRowCount(10)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabela_historico_cadastros.setItem(0, 0, __qtablewidgetitem3)
        self.tabela_historico_cadastros.setObjectName(u"tabela_historico_cadastros")
        sizePolicy1.setHeightForWidth(self.tabela_historico_cadastros.sizePolicy().hasHeightForWidth())
        self.tabela_historico_cadastros.setSizePolicy(sizePolicy1)
        self.tabela_historico_cadastros.setMinimumSize(QSize(0, 0))
        self.tabela_historico_cadastros.setStyleSheet(u"QHeaderView::section {\n"
"	background-color: rgb(148, 148, 148);\n"
"	color: rgb(255, 255, 255);\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}\n"
"")
        self.tabela_historico_cadastros.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tabela_historico_cadastros.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela_historico_cadastros.setRowCount(10)
        self.tabela_historico_cadastros.setColumnCount(3)
        self.tabela_historico_cadastros.horizontalHeader().setCascadingSectionResizes(False)
        self.tabela_historico_cadastros.horizontalHeader().setDefaultSectionSize(100)
        self.tabela_historico_cadastros.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabela_historico_cadastros.horizontalHeader().setStretchLastSection(True)
        self.tabela_historico_cadastros.verticalHeader().setCascadingSectionResizes(False)
        self.tabela_historico_cadastros.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.gridLayout_4.addWidget(self.tabela_historico_cadastros, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.tab_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.tabela_historico_documentos = QTableWidget(self.tab_2)
        if (self.tabela_historico_documentos.columnCount() < 5):
            self.tabela_historico_documentos.setColumnCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabela_historico_documentos.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabela_historico_documentos.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabela_historico_documentos.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabela_historico_documentos.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabela_historico_documentos.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        if (self.tabela_historico_documentos.rowCount() < 10):
            self.tabela_historico_documentos.setRowCount(10)
        self.tabela_historico_documentos.setObjectName(u"tabela_historico_documentos")
        self.tabela_historico_documentos.setStyleSheet(u"QHeaderView::section {\n"
"	background-color: rgb(148, 148, 148);\n"
"	color: rgb(255, 255, 255);\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}\n"
"")
        self.tabela_historico_documentos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela_historico_documentos.setRowCount(10)
        self.tabela_historico_documentos.horizontalHeader().setStretchLastSection(True)
        self.tabela_historico_documentos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.verticalLayout_15.addWidget(self.tabela_historico_documentos)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_14.addWidget(self.tabWidget)


        self.horizontalLayout_11.addWidget(self.conteudo_tela_historico)

        self.Pages.addWidget(self.pg_historico)

        self.verticalLayout_5.addWidget(self.Pages)


        self.gridLayout.addWidget(self.tela_central, 1, 2, 1, 1)

        self.rodape = QWidget(self.container_geral)
        self.rodape.setObjectName(u"rodape")
        self.rodape.setStyleSheet(u"QWidget{\n"
"	background-color: white;\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.rodape)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.txt_rodape = QLabel(self.rodape)
        self.txt_rodape.setObjectName(u"txt_rodape")
        self.txt_rodape.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 8pt;\n"
"}")

        self.horizontalLayout_5.addWidget(self.txt_rodape)


        self.gridLayout.addWidget(self.rodape, 2, 2, 1, 1)


        self.gridLayout_2.addWidget(self.container_geral, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_toogle_fechado.toggled.connect(self.menu_fechado.setHidden)
        self.btn_toogle_fechado.toggled.connect(self.menu_aberto.setVisible)
        self.btn_toogle_aberto.toggled.connect(self.menu_aberto.setHidden)
        self.btn_toogle_aberto.toggled.connect(self.menu_fechado.setVisible)

        self.Pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.btn_toogle_fechado.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_toogle_fechado.setAccessibleName(QCoreApplication.translate("MainWindow", u"Botao de Menu fechado", None))
#endif // QT_CONFIG(accessibility)
        self.btn_toogle_fechado.setText("")
#if QT_CONFIG(tooltip)
        self.btn_home_menu_fechado.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_home_menu_fechado.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Botao da pagina home no menu fechado", None))
#endif // QT_CONFIG(accessibility)
        self.btn_home_menu_fechado.setText("")
#if QT_CONFIG(tooltip)
        self.btn_perfil_menu_fechado.setToolTip(QCoreApplication.translate("MainWindow", u"Perfil", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_perfil_menu_fechado.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Botao da pagina de perfil do menu fechado", None))
#endif // QT_CONFIG(accessibility)
        self.btn_perfil_menu_fechado.setText("")
#if QT_CONFIG(tooltip)
        self.btn_cadastrar_menu_fechado.setToolTip(QCoreApplication.translate("MainWindow", u"Cadastrar Cliente", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_cadastrar_menu_fechado.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Botao da pagina de cadastro de Cliente do menu fechado", None))
#endif // QT_CONFIG(accessibility)
        self.btn_cadastrar_menu_fechado.setText("")
#if QT_CONFIG(tooltip)
        self.btn_enviardocumento_menu_fechado.setToolTip(QCoreApplication.translate("MainWindow", u"Enviar Documentos", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_enviardocumento_menu_fechado.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Botao da pagina de envio de documentos do menu fechado", None))
#endif // QT_CONFIG(accessibility)
        self.btn_enviardocumento_menu_fechado.setText("")
#if QT_CONFIG(tooltip)
        self.btn_historico_menu_fechado.setToolTip(QCoreApplication.translate("MainWindow", u"Hist\u00f3rico", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_historico_menu_fechado.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Botao da pagina de historico do menu fechado", None))
#endif // QT_CONFIG(accessibility)
        self.btn_historico_menu_fechado.setText("")
#if QT_CONFIG(tooltip)
        self.btn_encerrar_menu_fechado.setToolTip(QCoreApplication.translate("MainWindow", u"Encerrar Sess\u00e3o", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_encerrar_menu_fechado.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Botao de encerrar sess\u00e3o menu fechado", None))
#endif // QT_CONFIG(accessibility)
        self.btn_encerrar_menu_fechado.setText("")
        self.icone_menu_aberto.setText("")
        self.nome_empresa_menu_aberto.setText(QCoreApplication.translate("MainWindow", u"RuralConnect", None))
#if QT_CONFIG(tooltip)
        self.btn_toogle_aberto.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_toogle_aberto.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Botao de Menu aberto", None))
#endif // QT_CONFIG(accessibility)
        self.btn_toogle_aberto.setText("")
#if QT_CONFIG(tooltip)
        self.btn_home_menu_aberto.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_home_menu_aberto.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Botao da pagina home do menu aberto", None))
#endif // QT_CONFIG(accessibility)
        self.btn_home_menu_aberto.setText(QCoreApplication.translate("MainWindow", u"  Home", None))
#if QT_CONFIG(tooltip)
        self.btn_perfil_menu_aberto.setToolTip(QCoreApplication.translate("MainWindow", u"Perfil", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_perfil_menu_aberto.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Botao da pagina de perfil do menu aberto", None))
#endif // QT_CONFIG(accessibility)
        self.btn_perfil_menu_aberto.setText(QCoreApplication.translate("MainWindow", u"  Perfil", None))
#if QT_CONFIG(tooltip)
        self.btn_cadastrar_menu_aberto.setToolTip(QCoreApplication.translate("MainWindow", u"Cadastrar Cliente", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_cadastrar_menu_aberto.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Botao da pagina de cadastro de Cliente do menu aberto", None))
#endif // QT_CONFIG(accessibility)
        self.btn_cadastrar_menu_aberto.setText(QCoreApplication.translate("MainWindow", u"  Cadastrar", None))
#if QT_CONFIG(tooltip)
        self.btn_enviardocumento_menu_aberto.setToolTip(QCoreApplication.translate("MainWindow", u"Enviar Documento", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_enviardocumento_menu_aberto.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Botao da pagina de envio de documentos do menu aberto", None))
#endif // QT_CONFIG(accessibility)
        self.btn_enviardocumento_menu_aberto.setText(QCoreApplication.translate("MainWindow", u"  Enviar Documento", None))
#if QT_CONFIG(tooltip)
        self.btn_historico_menu_aberto.setToolTip(QCoreApplication.translate("MainWindow", u"Hist\u00f3rico", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_historico_menu_aberto.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Botao da pagina de historico do menu aberto", None))
#endif // QT_CONFIG(accessibility)
        self.btn_historico_menu_aberto.setText(QCoreApplication.translate("MainWindow", u"  Hist\u00f3rico", None))
#if QT_CONFIG(tooltip)
        self.btn_encerrar_menu_aberto.setToolTip(QCoreApplication.translate("MainWindow", u"Encerrar Sess\u00e3o", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_encerrar_menu_aberto.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Botao de encerrar sess\u00e3o menu aberto", None))
#endif // QT_CONFIG(accessibility)
        self.btn_encerrar_menu_aberto.setText(QCoreApplication.translate("MainWindow", u"Encerrar", None))
        self.txt_nome_sistema.setText(QCoreApplication.translate("MainWindow", u"Cadastro de Clientes em \u00c1reas Remotas", None))
        self.lbl_saudacao.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Seja Bem Vindo(a)</p></body></html>", None))
        self.txt_nome_perfil_home.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.lbl_icone_empresa_tela_home.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Perfil", None))
        self.txt_nome_perfil.setText(QCoreApplication.translate("MainWindow", u"Nome do Usuario", None))
        self.txt_email_perfil.setText(QCoreApplication.translate("MainWindow", u"Email do Usu\u00e1rio", None))
        self.txt_telefone_perfil.setText(QCoreApplication.translate("MainWindow", u"Telefone do Usu\u00e1rio", None))
#if QT_CONFIG(tooltip)
        self.btn_alterar_dados.setToolTip(QCoreApplication.translate("MainWindow", u"Alterar meus dados", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_alterar_dados.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.btn_alterar_dados.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Botao de alterar dados da pagina de perfil", None))
#endif // QT_CONFIG(accessibility)
        self.btn_alterar_dados.setText(QCoreApplication.translate("MainWindow", u"Alterar Dados", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Altere seus Dados", None))
#if QT_CONFIG(tooltip)
        self.txt_perfil_alterar_nome.setToolTip(QCoreApplication.translate("MainWindow", u"Digite um nome", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_perfil_alterar_nome.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo de texto para o usuario inseri um novo nome para seu perfil", None))
#endif // QT_CONFIG(accessibility)
        self.txt_perfil_alterar_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
#if QT_CONFIG(tooltip)
        self.txt_perfil_alterar_email.setToolTip(QCoreApplication.translate("MainWindow", u"Digite um email v\u00e1lido", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_perfil_alterar_email.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo de texto para alterar o email", None))
#endif // QT_CONFIG(accessibility)
        self.txt_perfil_alterar_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
#if QT_CONFIG(tooltip)
        self.txt_perfil_alterar_telefone.setToolTip(QCoreApplication.translate("MainWindow", u"Digite o telefone", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_perfil_alterar_telefone.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo de texto para inserir um novo telefone", None))
#endif // QT_CONFIG(accessibility)
        self.txt_perfil_alterar_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
#if QT_CONFIG(tooltip)
        self.btn_salvar_alteracoes.setToolTip(QCoreApplication.translate("MainWindow", u"Salvar Altera\u00e7\u00f5es", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_salvar_alteracoes.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Botao de salvar alteracoes do perfil", None))
#endif // QT_CONFIG(accessibility)
        self.btn_salvar_alteracoes.setText(QCoreApplication.translate("MainWindow", u"Salvar Altera\u00e7\u00f5es", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"P\u00e1gina de Cadastro de Cliente", None))
#if QT_CONFIG(tooltip)
        self.btn_carregar_formulario.setToolTip(QCoreApplication.translate("MainWindow", u"Importar formul\u00e1rio preenchido", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_carregar_formulario.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Botao para selecionar formul\u00e1rio preenchido", None))
#endif // QT_CONFIG(accessibility)
        self.btn_carregar_formulario.setText(QCoreApplication.translate("MainWindow", u"Importar Formul\u00e1rio", None))
#if QT_CONFIG(tooltip)
        self.btn_limpar_formulario.setToolTip(QCoreApplication.translate("MainWindow", u"Limpar o formul\u00e1rio", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_limpar_formulario.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Botao para limpar o formulario ", None))
#endif // QT_CONFIG(accessibility)
        self.btn_limpar_formulario.setText(QCoreApplication.translate("MainWindow", u"Limpar Formul\u00e1rio", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Confira os dados importados do formul\u00e1rio", None))
#if QT_CONFIG(tooltip)
        self.txt_cadastro_nome.setToolTip(QCoreApplication.translate("MainWindow", u"Nome do Cliente", None))
#endif // QT_CONFIG(tooltip)
        self.txt_cadastro_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Nome", None))
#if QT_CONFIG(tooltip)
        self.txt_cadastro_cpf.setToolTip(QCoreApplication.translate("MainWindow", u"CPF do Cliente", None))
#endif // QT_CONFIG(tooltip)
        self.txt_cadastro_cpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  CPF", None))
#if QT_CONFIG(tooltip)
        self.txt_cadastro_rg.setToolTip(QCoreApplication.translate("MainWindow", u"RG do Cliente", None))
#endif // QT_CONFIG(tooltip)
        self.txt_cadastro_rg.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  RG", None))
#if QT_CONFIG(tooltip)
        self.txt_cadastro_filiacao.setToolTip(QCoreApplication.translate("MainWindow", u"Filia\u00e7\u00e3o do Cliente", None))
#endif // QT_CONFIG(tooltip)
        self.txt_cadastro_filiacao.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Filia\u00e7\u00e3o", None))
#if QT_CONFIG(tooltip)
        self.txt_cadastro_endereco.setToolTip(QCoreApplication.translate("MainWindow", u"Endere\u00e7o do Cliente", None))
#endif // QT_CONFIG(tooltip)
        self.txt_cadastro_endereco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Endere\u00e7o", None))
#if QT_CONFIG(tooltip)
        self.txt_cadastro_nascimento.setToolTip(QCoreApplication.translate("MainWindow", u"Data de Nascimento do Cliente", None))
#endif // QT_CONFIG(tooltip)
        self.txt_cadastro_nascimento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Data de Nascimento", None))
#if QT_CONFIG(tooltip)
        self.txt_cadastro_cidade.setToolTip(QCoreApplication.translate("MainWindow", u"Cidade do Cliente", None))
#endif // QT_CONFIG(tooltip)
        self.txt_cadastro_cidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Cidade", None))
#if QT_CONFIG(tooltip)
        self.txt_cadastro_estado.setToolTip(QCoreApplication.translate("MainWindow", u"Estado do Cliente", None))
#endif // QT_CONFIG(tooltip)
        self.txt_cadastro_estado.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Estado", None))
#if QT_CONFIG(tooltip)
        self.txt_cadastro_telefone.setToolTip(QCoreApplication.translate("MainWindow", u"Telefone do Cliente", None))
#endif // QT_CONFIG(tooltip)
        self.txt_cadastro_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
#if QT_CONFIG(tooltip)
        self.txt_cadastro_email.setToolTip(QCoreApplication.translate("MainWindow", u"Email do Cliente", None))
#endif // QT_CONFIG(tooltip)
        self.txt_cadastro_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Email", None))
#if QT_CONFIG(tooltip)
        self.btn_carregar_documentos.setToolTip(QCoreApplication.translate("MainWindow", u"Selecionar Documento", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_carregar_documentos.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Botao de selecao de documentos do cadastro", None))
#endif // QT_CONFIG(accessibility)
        self.btn_carregar_documentos.setText(QCoreApplication.translate("MainWindow", u"Selecionar Documento", None))
#if QT_CONFIG(tooltip)
        self.btn_remover_lista_cadastro.setToolTip(QCoreApplication.translate("MainWindow", u"Remover o item selecionado", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_remover_lista_cadastro.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Botao de remover o documento selecionado da lista", None))
#endif // QT_CONFIG(accessibility)
        self.btn_remover_lista_cadastro.setText(QCoreApplication.translate("MainWindow", u"Remover da Lista", None))
#if QT_CONFIG(tooltip)
        self.btn_limpar_lista_cadastro.setToolTip(QCoreApplication.translate("MainWindow", u"Limpar Lista de Documentos", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_limpar_lista_cadastro.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Botao de limpar a lista de documentos", None))
#endif // QT_CONFIG(accessibility)
        self.btn_limpar_lista_cadastro.setText(QCoreApplication.translate("MainWindow", u"Limpar Lista", None))
#if QT_CONFIG(tooltip)
        self.lista_documentos_cadastro.setToolTip(QCoreApplication.translate("MainWindow", u"Lista dos Documentos a serem enviados no cadastro", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.lista_documentos_cadastro.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo da Lista dos Documentos a serem enviados no cadastro", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(tooltip)
        self.miniatura_documento.setToolTip(QCoreApplication.translate("MainWindow", u"Amostra da imagem selecionada", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.miniatura_documento.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo onde \u00e9 mostrada a miniatura de amostra da imagem selecionada na lista", None))
#endif // QT_CONFIG(accessibility)
        self.miniatura_documento.setText(QCoreApplication.translate("MainWindow", u"Amostra de imagem", None))
#if QT_CONFIG(tooltip)
        self.btn_cadastro_enviar.setToolTip(QCoreApplication.translate("MainWindow", u"Enviar Cadastro", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_cadastro_enviar.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Botao de envio do cadastro e documentos relacionados", None))
#endif // QT_CONFIG(accessibility)
        self.btn_cadastro_enviar.setText(QCoreApplication.translate("MainWindow", u"Enviar Cadastro", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Se desejar vincular o documento a algum cliente j\u00e1 cadastrado informe o CPF ", None))
#if QT_CONFIG(tooltip)
        self.txt_pesquisa_cliente.setToolTip(QCoreApplication.translate("MainWindow", u"Para vincular o documento a um Cliente", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_pesquisa_cliente.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo de texto para informar o CPF caso queira vincular o documento a um cliente cadastrado", None))
#endif // QT_CONFIG(accessibility)
        self.txt_pesquisa_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF de  Cliente j\u00e1 cadastrado", None))
        self.tipo_documento.setItemText(0, QCoreApplication.translate("MainWindow", u"Escolha o tipo do documento", None))
        self.tipo_documento.setItemText(1, QCoreApplication.translate("MainWindow", u"RG", None))
        self.tipo_documento.setItemText(2, QCoreApplication.translate("MainWindow", u"CPF", None))
        self.tipo_documento.setItemText(3, QCoreApplication.translate("MainWindow", u"CNH", None))
        self.tipo_documento.setItemText(4, QCoreApplication.translate("MainWindow", u"TEXTO", None))
        self.tipo_documento.setItemText(5, QCoreApplication.translate("MainWindow", u"CONTRATO", None))
        self.tipo_documento.setItemText(6, QCoreApplication.translate("MainWindow", u"COMPROVANTE DE ENDERE\u00c7O", None))

#if QT_CONFIG(tooltip)
        self.tipo_documento.setToolTip(QCoreApplication.translate("MainWindow", u"Tipo do Documento", None))
#endif // QT_CONFIG(tooltip)
        self.tipo_documento.setCurrentText(QCoreApplication.translate("MainWindow", u"Escolha o tipo do documento", None))
#if QT_CONFIG(tooltip)
        self.btn_arquivo_documento.setToolTip(QCoreApplication.translate("MainWindow", u"Escolher um Documento", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_arquivo_documento.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Botao para selecionar um arquivo para extrair dados", None))
#endif // QT_CONFIG(accessibility)
        self.btn_arquivo_documento.setText(QCoreApplication.translate("MainWindow", u"Escolher um Arquivo", None))
#if QT_CONFIG(tooltip)
        self.btn_remover_doc.setToolTip(QCoreApplication.translate("MainWindow", u"Limpar sele\u00e7\u00e3o", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_remover_doc.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Botao responsavel por limpar os campos da pagina de envio de documentos", None))
#endif // QT_CONFIG(accessibility)
        self.btn_remover_doc.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Arquivo Selecionado", None))
#if QT_CONFIG(tooltip)
        self.lista_envio_documento.setToolTip(QCoreApplication.translate("MainWindow", u"Documento selecionado", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.lista_envio_documento.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo onde aparece o caminho do documento selecionado", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(tooltip)
        self.amostra_imagem.setToolTip(QCoreApplication.translate("MainWindow", u"Amostra de imagem do documento selecionado", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.amostra_imagem.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo onde aparece a miniatura do arquivo", None))
#endif // QT_CONFIG(accessibility)
        self.amostra_imagem.setText(QCoreApplication.translate("MainWindow", u"Amostra de Imagem", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Confira os dados extra\u00eddos antes de enviar", None))
#if QT_CONFIG(tooltip)
        self.txt_dados_documento.setToolTip(QCoreApplication.translate("MainWindow", u"Texto Extraido", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_dados_documento.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo de texto onde aparece o texto extraido", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(tooltip)
        self.btn_enviar_arquivo.setToolTip(QCoreApplication.translate("MainWindow", u"Enviar Documento", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_enviar_arquivo.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Botao de enviar documento", None))
#endif // QT_CONFIG(accessibility)
        self.btn_enviar_arquivo.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        ___qtablewidgetitem = self.tabela_historico_cadastros.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem1 = self.tabela_historico_cadastros.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtablewidgetitem2 = self.tabela_historico_cadastros.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Data de Cadastro", None));

        __sortingEnabled = self.tabela_historico_cadastros.isSortingEnabled()
        self.tabela_historico_cadastros.setSortingEnabled(False)
        self.tabela_historico_cadastros.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Hist\u00f3rico de Cadastros de Clientes", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Hist\u00f3rico de Cadastros", None))
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem3 = self.tabela_historico_documentos.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem4 = self.tabela_historico_documentos.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Titulo", None));
        ___qtablewidgetitem5 = self.tabela_historico_documentos.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtablewidgetitem6 = self.tabela_historico_documentos.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtablewidgetitem7 = self.tabela_historico_documentos.horizontalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Data de Envio", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Hist\u00f3rico de Envio de Documentos", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Hist\u00f3rico de Envio de Documentos", None))
#endif // QT_CONFIG(tooltip)
        self.txt_rodape.setText(QCoreApplication.translate("MainWindow", u"\u00a9 RuralConnect", None))
    # retranslateUi

