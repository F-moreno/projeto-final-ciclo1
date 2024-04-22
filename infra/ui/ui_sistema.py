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
    QTextEdit, QToolBox, QVBoxLayout, QWidget)
from infra.ui import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1145, 696)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu = QFrame(self.centralwidget)
        self.menu.setObjectName(u"menu")
        self.menu.setMinimumSize(QSize(0, 0))
        self.menu.setMaximumSize(QSize(0, 16777215))
        self.menu.setStyleSheet(u"QFrame {\n"
"background-color: qlineargradient(spread:pad, x1:0.465, y1:0.481682, x2:0, y2:0, stop:0.147727 rgba(0, 164, 218, 255), stop:0.931818 rgba(0, 219, 255, 255));\n"
"}")
        self.menu.setFrameShape(QFrame.StyledPanel)
        self.menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.menu)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Arial,sans-serif"])
        font.setPointSize(15)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"	color: rgb(255, 255, 255);\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 15pt;\n"
"	font-weight:600;\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(self.menu)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toolBox = QToolBox(self.frame)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMinimumSize(QSize(220, 0))
        self.toolBox.setLayoutDirection(Qt.LeftToRight)
        self.toolBox.setAutoFillBackground(False)
        self.toolBox.setStyleSheet(u"QToolBox::tab {\n"
"	background-color: transparent;\n"
" 	border: none; \n"
"}\n"
"QToolBox{\n"
"background-color: transparent;\n"
"}")
        self.toolBox.setFrameShape(QFrame.NoFrame)
        self.toolBox.setFrameShadow(QFrame.Plain)
        self.toolBox.setLineWidth(1)
        self.toolBox.setMidLineWidth(0)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 220, 637))
        self.page.setStyleSheet(u"QWidget {\n"
"	background-color:transparent;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_home_menu = QPushButton(self.page)
        self.btn_home_menu.setObjectName(u"btn_home_menu")
        self.btn_home_menu.setMinimumSize(QSize(0, 40))
        self.btn_home_menu.setSizeIncrement(QSize(0, 0))
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
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-left-radius: 12px;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/homepage.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home_menu.setIcon(icon)
        self.btn_home_menu.setIconSize(QSize(22, 22))
        self.btn_home_menu.setAutoDefault(False)
        self.btn_home_menu.setFlat(False)

        self.verticalLayout_4.addWidget(self.btn_home_menu)

        self.btn_perfil_menu = QPushButton(self.page)
        self.btn_perfil_menu.setObjectName(u"btn_perfil_menu")
        self.btn_perfil_menu.setMinimumSize(QSize(0, 40))
        self.btn_perfil_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_perfil_menu.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-left-radius: 12px;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_perfil_menu.setIcon(icon1)
        self.btn_perfil_menu.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.btn_perfil_menu)

        self.btn_cadastrar_menu = QPushButton(self.page)
        self.btn_cadastrar_menu.setObjectName(u"btn_cadastrar_menu")
        self.btn_cadastrar_menu.setMinimumSize(QSize(0, 40))
        self.btn_cadastrar_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar_menu.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-left-radius: 12px;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"	color: rgb(0,0,0);\n"
"	\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/verify.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastrar_menu.setIcon(icon2)
        self.btn_cadastrar_menu.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.btn_cadastrar_menu)

        self.btn_enviar_menu = QPushButton(self.page)
        self.btn_enviar_menu.setObjectName(u"btn_enviar_menu")
        self.btn_enviar_menu.setMinimumSize(QSize(0, 40))
        self.btn_enviar_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_enviar_menu.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-left-radius: 12px;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/upload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_enviar_menu.setIcon(icon3)
        self.btn_enviar_menu.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.btn_enviar_menu)

        self.btn_historico_menu = QPushButton(self.page)
        self.btn_historico_menu.setObjectName(u"btn_historico_menu")
        self.btn_historico_menu.setMinimumSize(QSize(0, 40))
        self.btn_historico_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_historico_menu.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(96, 194, 255);\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-left-radius: 12px;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/historical.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_historico_menu.setIcon(icon4)
        self.btn_historico_menu.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.btn_historico_menu)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.btn_encerrar_menu = QPushButton(self.page)
        self.btn_encerrar_menu.setObjectName(u"btn_encerrar_menu")
        self.btn_encerrar_menu.setMinimumSize(QSize(0, 40))
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
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-left-radius: 12px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/out.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_encerrar_menu.setIcon(icon5)
        self.btn_encerrar_menu.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.btn_encerrar_menu)

        self.toolBox.addItem(self.page, u"")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.menu)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255,255,255);\n"
"	border: 0px;\n"
"	color: black;\n"
"}")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.hand_frame = QFrame(self.main_container)
        self.hand_frame.setObjectName(u"hand_frame")
        self.hand_frame.setStyleSheet(u"QFrame {\n"
"	background-color: qlineargradient(spread:pad, x1:0.465, y1:0.481682, x2:0, y2:0, stop:0.147727 rgba(0, 164, 218, 255), stop:0.931818 rgba(0, 219, 255, 255));\n"
"margin-left: 0px;\n"
"\n"
"}")
        self.hand_frame.setFrameShape(QFrame.StyledPanel)
        self.hand_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.hand_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_toogle = QPushButton(self.hand_frame)
        self.btn_toogle.setObjectName(u"btn_toogle")
        self.btn_toogle.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_toogle.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/option.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toogle.setIcon(icon6)
        self.btn_toogle.setIconSize(QSize(28, 28))

        self.horizontalLayout_2.addWidget(self.btn_toogle, 0, Qt.AlignLeft)

        self.label = QLabel(self.hand_frame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"	color: rgb(255, 255, 255);\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 15pt;\n"
"	font-weight:600;\n"
"}")

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.hand_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy1)
        self.main_frame.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"}")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.main_frame.setMidLineWidth(0)
        self.verticalLayout_14 = QVBoxLayout(self.main_frame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.Pages = QStackedWidget(self.main_frame)
        self.Pages.setObjectName(u"Pages")
        sizePolicy.setHeightForWidth(self.Pages.sizePolicy().hasHeightForWidth())
        self.Pages.setSizePolicy(sizePolicy)
        self.Pages.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"}")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_5 = QVBoxLayout(self.pg_home)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_8 = QFrame(self.pg_home)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_21 = QFrame(self.frame_8)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"}")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_21)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"}")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_22)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_12 = QLabel(self.frame_22)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"QLabel {\n"
"	font-family: Arial, sans-serif;\n"
"	background-color: transparent;\n"
"	font-size: 14pt;\n"
"	color: rgb(0,0,0);\n"
"	border: 0px;\n"
"	font-weight:600;\n"
"}")

        self.verticalLayout_22.addWidget(self.label_12, 0, Qt.AlignHCenter)

        self.txt_nome_perfil_home = QLabel(self.frame_22)
        self.txt_nome_perfil_home.setObjectName(u"txt_nome_perfil_home")
        self.txt_nome_perfil_home.setStyleSheet(u"QLabel {\n"
"	font-family: Arial, sans-serif;\n"
"	background-color: transparent;\n"
"	font-size: 14pt;\n"
"	color: rgb(0,0,0);\n"
"	border: 0px;\n"
"	font-weight:600;\n"
"}")

        self.verticalLayout_22.addWidget(self.txt_nome_perfil_home, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.frame_21)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"}")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_4 = QLabel(self.frame_23)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"}")
        self.label_4.setPixmap(QPixmap(u":/icons/icons/cobra.png"))

        self.horizontalLayout_14.addWidget(self.label_4, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addWidget(self.frame_23)


        self.horizontalLayout_15.addWidget(self.frame_21)


        self.verticalLayout_5.addWidget(self.frame_8, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.Pages.addWidget(self.pg_home)
        self.pg_cadastrar = QWidget()
        self.pg_cadastrar.setObjectName(u"pg_cadastrar")
        self.pg_cadastrar.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.pg_cadastrar)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_9 = QFrame(self.pg_cadastrar)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_9)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel {\n"
"	font-family: Arial, sans-serif;\n"
"	background-color: transparent;\n"
"	font-size: 14pt;\n"
"	color: rgb(0,0,0);\n"
"	font-weight:600;\n"
"}")

        self.verticalLayout_16.addWidget(self.label_5, 0, Qt.AlignLeft)

        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy2)
        self.frame_12.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy1.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy1)
        self.frame_13.setMaximumSize(QSize(16777215, 16777215))
        self.frame_13.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(0, 164, 218, 0.2);\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-right-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_13)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(15, 15, 15, 15)
        self.btn_carregar_formulario = QPushButton(self.frame_13)
        self.btn_carregar_formulario.setObjectName(u"btn_carregar_formulario")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_carregar_formulario.sizePolicy().hasHeightForWidth())
        self.btn_carregar_formulario.setSizePolicy(sizePolicy3)
        self.btn_carregar_formulario.setMinimumSize(QSize(250, 30))
        self.btn_carregar_formulario.setMaximumSize(QSize(200, 16777215))
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
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/import.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_carregar_formulario.setIcon(icon7)

        self.verticalLayout_18.addWidget(self.btn_carregar_formulario, 0, Qt.AlignHCenter)

        self.btn_limpar_formulario = QPushButton(self.frame_13)
        self.btn_limpar_formulario.setObjectName(u"btn_limpar_formulario")
        self.btn_limpar_formulario.setMinimumSize(QSize(250, 30))
        self.btn_limpar_formulario.setMaximumSize(QSize(200, 16777215))
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
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_limpar_formulario.setIcon(icon8)

        self.verticalLayout_18.addWidget(self.btn_limpar_formulario, 0, Qt.AlignHCenter)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_11)

        self.label_6 = QLabel(self.frame_13)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	color: rgb(0,0,0);\n"
"}")

        self.verticalLayout_18.addWidget(self.label_6, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.txt_cadastro_nome = QLineEdit(self.frame_13)
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

        self.verticalLayout_18.addWidget(self.txt_cadastro_nome)

        self.txt_cadastro_cpf = QLineEdit(self.frame_13)
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

        self.verticalLayout_18.addWidget(self.txt_cadastro_cpf)

        self.txt_cadastro_rg = QLineEdit(self.frame_13)
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

        self.verticalLayout_18.addWidget(self.txt_cadastro_rg)

        self.txt_cadastro_filiacao = QLineEdit(self.frame_13)
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

        self.verticalLayout_18.addWidget(self.txt_cadastro_filiacao)

        self.txt_cadastro_endereco = QLineEdit(self.frame_13)
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

        self.verticalLayout_18.addWidget(self.txt_cadastro_endereco)

        self.txt_cadastro_nascimento = QLineEdit(self.frame_13)
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

        self.verticalLayout_18.addWidget(self.txt_cadastro_nascimento)

        self.txt_cadastro_cidade = QLineEdit(self.frame_13)
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

        self.verticalLayout_18.addWidget(self.txt_cadastro_cidade)

        self.txt_cadastro_estado = QLineEdit(self.frame_13)
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

        self.verticalLayout_18.addWidget(self.txt_cadastro_estado)

        self.txt_cadastro_telefone = QLineEdit(self.frame_13)
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

        self.verticalLayout_18.addWidget(self.txt_cadastro_telefone)

        self.txt_cadastro_email = QLineEdit(self.frame_13)
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

        self.verticalLayout_18.addWidget(self.txt_cadastro_email)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_10)


        self.horizontalLayout_9.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy1.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy1)
        self.frame_14.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"}")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_18 = QFrame(self.frame_14)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy1.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy1)
        self.frame_18.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(0, 164, 218, 0.2);\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-right-radius: 20px;\n"
"}")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_18)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.btn_carregar_documentos = QPushButton(self.frame_18)
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
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_carregar_documentos.setIcon(icon9)

        self.verticalLayout_21.addWidget(self.btn_carregar_documentos)

        self.btn_remover_lista_cadastro = QPushButton(self.frame_18)
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
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_remover_lista_cadastro.setIcon(icon10)
        self.btn_remover_lista_cadastro.setIconSize(QSize(13, 13))

        self.verticalLayout_21.addWidget(self.btn_remover_lista_cadastro)

        self.btn_limpar_lista_cadastro = QPushButton(self.frame_18)
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
"	border-bottom-right-radius: 10px;\n"
"	border-top-left-radius: 10px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.btn_limpar_lista_cadastro.setIcon(icon8)

        self.verticalLayout_21.addWidget(self.btn_limpar_lista_cadastro)

        self.lista_documentos_cadastro = QListWidget(self.frame_18)
        self.lista_documentos_cadastro.setObjectName(u"lista_documentos_cadastro")
        self.lista_documentos_cadastro.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.lista_documentos_cadastro.sizePolicy().hasHeightForWidth())
        self.lista_documentos_cadastro.setSizePolicy(sizePolicy1)
        self.lista_documentos_cadastro.setMinimumSize(QSize(0, 0))
        self.lista_documentos_cadastro.setMaximumSize(QSize(250, 250))
        self.lista_documentos_cadastro.setStyleSheet(u"QListWidget{\n"
"	background-color: white;\n"
"	color: rgb(0,0,0);\n"
"	border-radius: 0px;\n"
"	border: 1px solid black;\n"
"	Qt::SelectOnDrag;\n"
"}")
        self.lista_documentos_cadastro.setDragEnabled(False)
        self.lista_documentos_cadastro.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.lista_documentos_cadastro.setViewMode(QListView.ListMode)

        self.verticalLayout_21.addWidget(self.lista_documentos_cadastro)

        self.miniatura_documento = QLabel(self.frame_18)
        self.miniatura_documento.setObjectName(u"miniatura_documento")
        sizePolicy1.setHeightForWidth(self.miniatura_documento.sizePolicy().hasHeightForWidth())
        self.miniatura_documento.setSizePolicy(sizePolicy1)
        self.miniatura_documento.setMinimumSize(QSize(250, 250))
        self.miniatura_documento.setMaximumSize(QSize(250, 250))
        self.miniatura_documento.setLayoutDirection(Qt.LeftToRight)
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

        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy1.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy1)
        self.frame_19.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"}")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btn_cadastro_enviar = QPushButton(self.frame_19)
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
        self.btn_cadastro_enviar.setIcon(icon3)

        self.horizontalLayout_13.addWidget(self.btn_cadastro_enviar)


        self.verticalLayout_21.addWidget(self.frame_19)


        self.horizontalLayout_12.addWidget(self.frame_18)


        self.horizontalLayout_9.addWidget(self.frame_14)


        self.verticalLayout_16.addWidget(self.frame_12)


        self.verticalLayout_6.addWidget(self.frame_9)

        self.Pages.addWidget(self.pg_cadastrar)
        self.pg_historico = QWidget()
        self.pg_historico.setObjectName(u"pg_historico")
        sizePolicy.setHeightForWidth(self.pg_historico.sizePolicy().hasHeightForWidth())
        self.pg_historico.setSizePolicy(sizePolicy)
        self.pg_historico.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.pg_historico)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tabWidget = QTabWidget(self.pg_historico)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy4)
        self.tabWidget.setCursor(QCursor(Qt.PointingHandCursor))
        self.tabWidget.setStyleSheet(u"QTabWidget {\n"
"	background-color: rgb(255,255,255);\n"
"	border: 0px;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.tabWidget.setElideMode(Qt.ElideMiddle)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_historico_cadastro = QWidget()
        self.tab_historico_cadastro.setObjectName(u"tab_historico_cadastro")
        self.tab_historico_cadastro.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.tab_historico_cadastro)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_10 = QFrame(self.tab_historico_cadastro)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.tabela_historico_cadastros = QTableWidget(self.frame_10)
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
        self.tabela_historico_cadastros.setObjectName(u"tabela_historico_cadastros")
        sizePolicy1.setHeightForWidth(self.tabela_historico_cadastros.sizePolicy().hasHeightForWidth())
        self.tabela_historico_cadastros.setSizePolicy(sizePolicy1)
        self.tabela_historico_cadastros.setStyleSheet(u"QHeaderView::section {\n"
"	background-color: rgb(148, 148, 148);\n"
"	color: rgb(255, 255, 255);\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color: rgb(252, 252, 252);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"\n"
"QTableWidget::verticalHeader() {\n"
"	visibility: visible;\n"
"}\n"
"QTableWidget {\n"
"	QHeaderView::sectionResizeMode(QHeaderView::Horizontal);\n"
"}")
        self.tabela_historico_cadastros.setTextElideMode(Qt.ElideMiddle)
        self.tabela_historico_cadastros.setRowCount(10)
        self.tabela_historico_cadastros.horizontalHeader().setCascadingSectionResizes(False)
        self.tabela_historico_cadastros.horizontalHeader().setDefaultSectionSize(250)
        self.tabela_historico_cadastros.horizontalHeader().setHighlightSections(True)
        self.tabela_historico_cadastros.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabela_historico_cadastros.horizontalHeader().setStretchLastSection(False)
        self.tabela_historico_cadastros.verticalHeader().setVisible(True)
        self.tabela_historico_cadastros.verticalHeader().setProperty("showSortIndicator", False)
        self.tabela_historico_cadastros.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_8.addWidget(self.tabela_historico_cadastros)


        self.horizontalLayout_5.addWidget(self.frame_10)

        self.tabWidget.addTab(self.tab_historico_cadastro, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"}")
        self.horizontalLayout_10 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_16 = QFrame(self.tab_2)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"}")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.tabela_historico_documentos = QTableWidget(self.frame_16)
        if (self.tabela_historico_documentos.columnCount() < 5):
            self.tabela_historico_documentos.setColumnCount(5)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabela_historico_documentos.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabela_historico_documentos.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabela_historico_documentos.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabela_historico_documentos.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabela_historico_documentos.setHorizontalHeaderItem(4, __qtablewidgetitem7)
        if (self.tabela_historico_documentos.rowCount() < 10):
            self.tabela_historico_documentos.setRowCount(10)
        self.tabela_historico_documentos.setObjectName(u"tabela_historico_documentos")
        self.tabela_historico_documentos.setStyleSheet(u"QHeaderView::section {\n"
"	background-color: rgb(148, 148, 148);\n"
"	color: rgb(255, 255, 255);\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color: rgb(252, 252, 252);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"\n"
"QTableWidget::verticalHeader() {\n"
"	visibility: visible;\n"
"}\n"
"QTableWidget {\n"
"	QHeaderView::sectionResizeMode(QHeaderView::Horizontal);\n"
"}")
        self.tabela_historico_documentos.setTextElideMode(Qt.ElideMiddle)
        self.tabela_historico_documentos.setShowGrid(True)
        self.tabela_historico_documentos.setGridStyle(Qt.SolidLine)
        self.tabela_historico_documentos.setRowCount(10)
        self.tabela_historico_documentos.horizontalHeader().setDefaultSectionSize(175)
        self.tabela_historico_documentos.horizontalHeader().setStretchLastSection(False)
        self.tabela_historico_documentos.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_11.addWidget(self.tabela_historico_documentos)


        self.horizontalLayout_10.addWidget(self.frame_16)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_7.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_historico)
        self.pg_enviar_doc = QWidget()
        self.pg_enviar_doc.setObjectName(u"pg_enviar_doc")
        self.pg_enviar_doc.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"}")
        self.verticalLayout_13 = QVBoxLayout(self.pg_enviar_doc)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_7 = QFrame(self.pg_enviar_doc)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_7)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_15 = QFrame(self.frame_7)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"}")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy1.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy1)
        self.frame_17.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(0, 164, 218, 0.2);\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-right-radius: 20px;\n"
"}\n"
"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_17)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.tipo_documento = QComboBox(self.frame_17)
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

        self.verticalLayout_20.addWidget(self.tipo_documento)

        self.btn_arquivo_documento = QPushButton(self.frame_17)
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
        self.btn_arquivo_documento.setIcon(icon9)

        self.verticalLayout_20.addWidget(self.btn_arquivo_documento)

        self.btn_remover_doc = QPushButton(self.frame_17)
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
        self.btn_remover_doc.setIcon(icon8)

        self.verticalLayout_20.addWidget(self.btn_remover_doc)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_6)

        self.label_9 = QLabel(self.frame_17)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	color: rgb(0,0,0);\n"
"}")

        self.verticalLayout_20.addWidget(self.label_9, 0, Qt.AlignHCenter)

        self.lista_envio_documento = QListWidget(self.frame_17)
        self.lista_envio_documento.setObjectName(u"lista_envio_documento")
        sizePolicy1.setHeightForWidth(self.lista_envio_documento.sizePolicy().hasHeightForWidth())
        self.lista_envio_documento.setSizePolicy(sizePolicy1)
        self.lista_envio_documento.setMaximumSize(QSize(16777215, 100))
        self.lista_envio_documento.setStyleSheet(u"QListWidget{\n"
"	background-color: white;\n"
"	color: rgb(0,0,0);\n"
"	border-radius: 0px;\n"
"	border: 1px solid black;\n"
"}")
        self.lista_envio_documento.setDragEnabled(False)
        self.lista_envio_documento.setDragDropMode(QAbstractItemView.NoDragDrop)

        self.verticalLayout_20.addWidget(self.lista_envio_documento)

        self.amostra_imagem = QLabel(self.frame_17)
        self.amostra_imagem.setObjectName(u"amostra_imagem")
        self.amostra_imagem.setMinimumSize(QSize(250, 250))
        self.amostra_imagem.setMaximumSize(QSize(250, 250))
        self.amostra_imagem.setLayoutDirection(Qt.LeftToRight)
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

        self.verticalLayout_20.addWidget(self.amostra_imagem, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_9)


        self.horizontalLayout_7.addWidget(self.frame_17)

        self.frame_11 = QFrame(self.frame_15)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_11)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_8 = QLabel(self.frame_11)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 11pt;\n"
"	color: rgb(0,0,0);\n"
"}")

        self.verticalLayout_17.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.txt_dados_documento = QTextEdit(self.frame_11)
        self.txt_dados_documento.setObjectName(u"txt_dados_documento")
        self.txt_dados_documento.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border: 1px solid black;\n"
"	border-radius: 0px;\n"
"}\n"
"")

        self.verticalLayout_17.addWidget(self.txt_dados_documento)

        self.btn_enviar_arquivo = QPushButton(self.frame_11)
        self.btn_enviar_arquivo.setObjectName(u"btn_enviar_arquivo")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_enviar_arquivo.sizePolicy().hasHeightForWidth())
        self.btn_enviar_arquivo.setSizePolicy(sizePolicy5)
        self.btn_enviar_arquivo.setMinimumSize(QSize(250, 30))
        self.btn_enviar_arquivo.setMaximumSize(QSize(250, 16777215))
        self.btn_enviar_arquivo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_enviar_arquivo.setLayoutDirection(Qt.LeftToRight)
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
        self.btn_enviar_arquivo.setIcon(icon3)

        self.verticalLayout_17.addWidget(self.btn_enviar_arquivo, 0, Qt.AlignHCenter)


        self.horizontalLayout_7.addWidget(self.frame_11)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.gridLayout.addWidget(self.frame_15, 0, 0, 1, 2)


        self.verticalLayout_13.addWidget(self.frame_7)

        self.Pages.addWidget(self.pg_enviar_doc)
        self.pg_alteracao_perfil = QWidget()
        self.pg_alteracao_perfil.setObjectName(u"pg_alteracao_perfil")
        self.pg_alteracao_perfil.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.pg_alteracao_perfil)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_6 = QFrame(self.pg_alteracao_perfil)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setMinimumSize(QSize(500, 0))
        self.frame_6.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(0, 164, 218, 0.2);\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-right-radius: 20px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"QLabel {\n"
"	font-family: Arial, sans-serif;\n"
"	background-color: transparent;\n"
"	font-size: 14pt;\n"
"	color: rgb(0,0,0);\n"
"}")

        self.verticalLayout_12.addWidget(self.label_11)

        self.txt_perfil_alterar_nome = QLineEdit(self.frame_6)
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

        self.verticalLayout_12.addWidget(self.txt_perfil_alterar_nome)

        self.txt_perfil_alterar_email = QLineEdit(self.frame_6)
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

        self.verticalLayout_12.addWidget(self.txt_perfil_alterar_email)

        self.txt_perfil_alterar_telefone = QLineEdit(self.frame_6)
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

        self.verticalLayout_12.addWidget(self.txt_perfil_alterar_telefone)

        self.btn_salvar_alteracoes = QPushButton(self.frame_6)
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
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_salvar_alteracoes.setIcon(icon11)

        self.verticalLayout_12.addWidget(self.btn_salvar_alteracoes, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_3)


        self.verticalLayout_11.addWidget(self.frame_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.Pages.addWidget(self.pg_alteracao_perfil)
        self.pg_perfil = QWidget()
        self.pg_perfil.setObjectName(u"pg_perfil")
        self.pg_perfil.setStyleSheet(u"QWidget{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.pg_perfil)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_5 = QFrame(self.pg_perfil)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 14pt;\n"
"	color: rgb(0,0,0);\n"
"}")

        self.horizontalLayout_6.addWidget(self.label_7)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.pg_perfil)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QSize(300, 200))
        self.frame_4.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(0, 164, 218, 0.2);\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-right-radius: 20px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_5)

        self.txt_nome_perfil = QLabel(self.frame_4)
        self.txt_nome_perfil.setObjectName(u"txt_nome_perfil")
        sizePolicy.setHeightForWidth(self.txt_nome_perfil.sizePolicy().hasHeightForWidth())
        self.txt_nome_perfil.setSizePolicy(sizePolicy)
        self.txt_nome_perfil.setStyleSheet(u"QLabel{\n"
"	background-color:transparent;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 16px;\n"
"	color: rgb(0,0,0);\n"
"	text-align: center;\n"
"}")
        self.txt_nome_perfil.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.txt_nome_perfil, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.txt_email_perfil = QLabel(self.frame_4)
        self.txt_email_perfil.setObjectName(u"txt_email_perfil")
        sizePolicy.setHeightForWidth(self.txt_email_perfil.sizePolicy().hasHeightForWidth())
        self.txt_email_perfil.setSizePolicy(sizePolicy)
        self.txt_email_perfil.setStyleSheet(u"QLabel{\n"
"	background-color:transparent;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 12px;\n"
"	color: rgb(0,0,0);\n"
"	text-align: center;\n"
"}")
        self.txt_email_perfil.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_9.addWidget(self.txt_email_perfil, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.txt_telefone_perfil = QLabel(self.frame_4)
        self.txt_telefone_perfil.setObjectName(u"txt_telefone_perfil")
        sizePolicy.setHeightForWidth(self.txt_telefone_perfil.sizePolicy().hasHeightForWidth())
        self.txt_telefone_perfil.setSizePolicy(sizePolicy)
        self.txt_telefone_perfil.setStyleSheet(u"QLabel{\n"
"	background-color:transparent;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 12px;\n"
"	color: rgb(0,0,0);\n"
"	text-align: center;\n"
"}")
        self.txt_telefone_perfil.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_9.addWidget(self.txt_telefone_perfil, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_4)


        self.verticalLayout_8.addWidget(self.frame_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_3 = QFrame(self.pg_perfil)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.btn_alterar_dados = QPushButton(self.frame_3)
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
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_alterar_dados.setIcon(icon12)

        self.verticalLayout_10.addWidget(self.btn_alterar_dados, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.frame_3)

        self.Pages.addWidget(self.pg_perfil)

        self.verticalLayout_14.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border: 0px;\n"
"\n"
"}")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"	font-family: Arial, sans-serif;\n"
"	font-size: 8pt;\n"
"	color: rgb(0,0,0);\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(0)
        self.Pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(accessibility)
        self.menu.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("MainWindow", u"Nome da Empresa", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">RuralConnect</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_home_menu.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_home_menu.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Bot\u00e3o da P\u00e1gina Principal", None))
#endif // QT_CONFIG(accessibility)
        self.btn_home_menu.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.btn_perfil_menu.setToolTip(QCoreApplication.translate("MainWindow", u"Perfil", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_perfil_menu.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Bot\u00e3o da P\u00e1gina de Perfil", None))
#endif // QT_CONFIG(accessibility)
        self.btn_perfil_menu.setText(QCoreApplication.translate("MainWindow", u"Perfil", None))
#if QT_CONFIG(tooltip)
        self.btn_cadastrar_menu.setToolTip(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_cadastrar_menu.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Bot\u00e3o da P\u00e1gina de Cadastro", None))
#endif // QT_CONFIG(accessibility)
        self.btn_cadastrar_menu.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
#if QT_CONFIG(tooltip)
        self.btn_enviar_menu.setToolTip(QCoreApplication.translate("MainWindow", u"Enviar Documentos", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_enviar_menu.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Bot\u00e3o da P\u00e1gina de Envio de Documentos", None))
#endif // QT_CONFIG(accessibility)
        self.btn_enviar_menu.setText(QCoreApplication.translate("MainWindow", u"Enviar Documento", None))
#if QT_CONFIG(tooltip)
        self.btn_historico_menu.setToolTip(QCoreApplication.translate("MainWindow", u"Hist\u00f3rico", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_historico_menu.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Bot\u00e3o da P\u00e1gina de Hist\u00f3rico", None))
#endif // QT_CONFIG(accessibility)
        self.btn_historico_menu.setText(QCoreApplication.translate("MainWindow", u"Hist\u00f3rico", None))
#if QT_CONFIG(tooltip)
        self.btn_encerrar_menu.setToolTip(QCoreApplication.translate("MainWindow", u"Encerrar Sess\u00e3o", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_encerrar_menu.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Bot\u00e3o de Logout", None))
#endif // QT_CONFIG(accessibility)
        self.btn_encerrar_menu.setText(QCoreApplication.translate("MainWindow", u"Encerrar", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), "")
#if QT_CONFIG(tooltip)
        self.btn_toogle.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_toogle.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Bot\u00e3o do Menu", None))
#endif // QT_CONFIG(accessibility)
        self.btn_toogle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Cadastro de Clientes em \u00c1reas Remotas</span></p></body></html>", None))
#if QT_CONFIG(accessibility)
        self.Pages.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Tabela de Hist\u00f3rico de Cadastros", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.pg_home.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"P\u00e1gina Principal", None))
#endif // QT_CONFIG(accessibility)
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">Seja Bem Vindo(a)</span></p></body></html>", None))
        self.txt_nome_perfil_home.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; color:#000000;\">Usu\u00e1rio</span></p></body></html>", None))
        self.label_4.setText("")
#if QT_CONFIG(accessibility)
        self.pg_cadastrar.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"P\u00e1gina de Cadastro de Cliente", None))
#endif // QT_CONFIG(accessibility)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">P\u00e1gina de Cadastro de Cliente</span></p></body></html>", None))
#if QT_CONFIG(accessibility)
        self.frame_13.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo de Importa\u00e7\u00e3o e extra\u00e7\u00e3o de Dados de Formul\u00e1rio", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(tooltip)
        self.btn_carregar_formulario.setToolTip(QCoreApplication.translate("MainWindow", u"Importar Formul\u00e1rio", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_carregar_formulario.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Bot\u00e3o de Importar Formul\u00e1rio", None))
#endif // QT_CONFIG(accessibility)
        self.btn_carregar_formulario.setText(QCoreApplication.translate("MainWindow", u"Importar Formul\u00e1rio", None))
#if QT_CONFIG(tooltip)
        self.btn_limpar_formulario.setToolTip(QCoreApplication.translate("MainWindow", u"Limpar Formul\u00e1rio", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_limpar_formulario.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Bot\u00e3o de limpar campos do formul\u00e1rio", None))
#endif // QT_CONFIG(accessibility)
        self.btn_limpar_formulario.setText(QCoreApplication.translate("MainWindow", u"Limpar Formul\u00e1rio", None))
#if QT_CONFIG(accessibility)
        self.label_6.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Texto informativo que diz: Confira os dados importados do formul\u00e1rio", None))
#endif // QT_CONFIG(accessibility)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Confira os dados importados do formul\u00e1rio", None))
#if QT_CONFIG(tooltip)
        self.txt_cadastro_nome.setToolTip(QCoreApplication.translate("MainWindow", u"Nome", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_cadastro_nome.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo para preenchimento do Nome Completo do Cliente", None))
#endif // QT_CONFIG(accessibility)
        self.txt_cadastro_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Nome", None))
#if QT_CONFIG(tooltip)
        self.txt_cadastro_cpf.setToolTip(QCoreApplication.translate("MainWindow", u"CPF", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_cadastro_cpf.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo para preenchimento do CPF do Cliente", None))
#endif // QT_CONFIG(accessibility)
        self.txt_cadastro_cpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  CPF", None))
#if QT_CONFIG(tooltip)
        self.txt_cadastro_rg.setToolTip(QCoreApplication.translate("MainWindow", u"RG", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_cadastro_rg.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo para preenchimento do RG do Cliente", None))
#endif // QT_CONFIG(accessibility)
        self.txt_cadastro_rg.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  RG", None))
#if QT_CONFIG(tooltip)
        self.txt_cadastro_filiacao.setToolTip(QCoreApplication.translate("MainWindow", u"Filia\u00e7\u00e3o", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_cadastro_filiacao.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo para preenchimento da Filia\u00e7\u00e3o do Cliente", None))
#endif // QT_CONFIG(accessibility)
        self.txt_cadastro_filiacao.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Filia\u00e7\u00e3o", None))
#if QT_CONFIG(tooltip)
        self.txt_cadastro_endereco.setToolTip(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_cadastro_endereco.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo para preenchimento do Endere\u00e7o do Cliente", None))
#endif // QT_CONFIG(accessibility)
        self.txt_cadastro_endereco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Endere\u00e7o", None))
#if QT_CONFIG(tooltip)
        self.txt_cadastro_nascimento.setToolTip(QCoreApplication.translate("MainWindow", u"Data de Nascimento", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_cadastro_nascimento.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo para preenchimento da Data de Nascimento do Cliente", None))
#endif // QT_CONFIG(accessibility)
        self.txt_cadastro_nascimento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Data de Nascimento", None))
#if QT_CONFIG(tooltip)
        self.txt_cadastro_cidade.setToolTip(QCoreApplication.translate("MainWindow", u"Cidade", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_cadastro_cidade.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo para preenchimento da Cidade do Cliente", None))
#endif // QT_CONFIG(accessibility)
        self.txt_cadastro_cidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Cidade", None))
#if QT_CONFIG(tooltip)
        self.txt_cadastro_estado.setToolTip(QCoreApplication.translate("MainWindow", u"Estado", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_cadastro_estado.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo para preenchimento do Estado do Cliente", None))
#endif // QT_CONFIG(accessibility)
        self.txt_cadastro_estado.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Estado", None))
#if QT_CONFIG(tooltip)
        self.txt_cadastro_telefone.setToolTip(QCoreApplication.translate("MainWindow", u"Telefone", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_cadastro_telefone.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo para preenchimento do Telefone do Cliente", None))
#endif // QT_CONFIG(accessibility)
        self.txt_cadastro_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Telefone", None))
#if QT_CONFIG(tooltip)
        self.txt_cadastro_email.setToolTip(QCoreApplication.translate("MainWindow", u"Email", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_cadastro_email.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo para preenchimento do Email do Cliente", None))
#endif // QT_CONFIG(accessibility)
        self.txt_cadastro_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Email", None))
#if QT_CONFIG(tooltip)
        self.btn_carregar_documentos.setToolTip(QCoreApplication.translate("MainWindow", u"Selecionar Documento", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_carregar_documentos.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Bot\u00e3o de Selecionar Arquivo de Documento", None))
#endif // QT_CONFIG(accessibility)
        self.btn_carregar_documentos.setText(QCoreApplication.translate("MainWindow", u"Selecionar Documento", None))
#if QT_CONFIG(tooltip)
        self.btn_remover_lista_cadastro.setToolTip(QCoreApplication.translate("MainWindow", u"Remover Documento da Lista", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_remover_lista_cadastro.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Bot\u00e3o de Remover documento da lista", None))
#endif // QT_CONFIG(accessibility)
        self.btn_remover_lista_cadastro.setText(QCoreApplication.translate("MainWindow", u"Remover da Lista", None))
#if QT_CONFIG(tooltip)
        self.btn_limpar_lista_cadastro.setToolTip(QCoreApplication.translate("MainWindow", u"Limpar lista de Documentos", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_limpar_lista_cadastro.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Bot\u00e3o de limpar a lista de documentos", None))
#endif // QT_CONFIG(accessibility)
        self.btn_limpar_lista_cadastro.setText(QCoreApplication.translate("MainWindow", u"Limpar Lista", None))
#if QT_CONFIG(tooltip)
        self.lista_documentos_cadastro.setToolTip(QCoreApplication.translate("MainWindow", u"Aqui ir\u00e3o aparecer os documentos selecionados", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.lista_documentos_cadastro.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo de Exibi\u00e7\u00e3o da Lista de Documentos Selecionados", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(tooltip)
        self.miniatura_documento.setToolTip(QCoreApplication.translate("MainWindow", u"Aqui ir\u00e1 aparecer a miniatura do documento selecionado na lista", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.miniatura_documento.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo de exibi\u00e7\u00e3o de Miniatura de Documento", None))
#endif // QT_CONFIG(accessibility)
        self.miniatura_documento.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Amostra de imagem</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_cadastro_enviar.setToolTip(QCoreApplication.translate("MainWindow", u"Enviar Cadastro", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_cadastro_enviar.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Bot\u00e3o de Enviar Cadastro", None))
#endif // QT_CONFIG(accessibility)
        self.btn_cadastro_enviar.setText(QCoreApplication.translate("MainWindow", u"Enviar Cadastro", None))
#if QT_CONFIG(accessibility)
        self.pg_historico.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"P\u00e1gina de Hist\u00f3ricos", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.tabWidget.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Tabelas de HIst\u00f3rico de Envio de Cadastros e Documentos do Usu\u00e1rio da Sess\u00e3o", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(tooltip)
        self.tab_historico_cadastro.setToolTip(QCoreApplication.translate("MainWindow", u"Meu hist\u00f3rico de Cadastros", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.tab_historico_cadastro.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Tabela de Hist\u00f3rico de Cadastro feito pelo Usu\u00e1rio", None))
#endif // QT_CONFIG(accessibility)
        ___qtablewidgetitem = self.tabela_historico_cadastros.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem1 = self.tabela_historico_cadastros.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtablewidgetitem2 = self.tabela_historico_cadastros.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Data Cadastro", None));
#if QT_CONFIG(accessibility)
        self.tabela_historico_cadastros.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Tabela de Hist\u00f3rico de Cadastro feito pelo Usu\u00e1rio", None))
#endif // QT_CONFIG(accessibility)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_historico_cadastro), QCoreApplication.translate("MainWindow", u"Hist\u00f3rico de Cadastros", None))
#if QT_CONFIG(tooltip)
        self.tab_2.setToolTip(QCoreApplication.translate("MainWindow", u"Meu hist\u00f3rico de Documentos Enviados", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.tab_2.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Tabela de Hist\u00f3rico de Envio de Documentos feito pelo Usu\u00e1rio", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.frame_16.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Tabela de Hist\u00f3rico de Envio de Documentos feito pelo Usu\u00e1rio", None))
#endif // QT_CONFIG(accessibility)
        ___qtablewidgetitem3 = self.tabela_historico_documentos.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem4 = self.tabela_historico_documentos.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Titulo", None));
        ___qtablewidgetitem5 = self.tabela_historico_documentos.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtablewidgetitem6 = self.tabela_historico_documentos.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtablewidgetitem7 = self.tabela_historico_documentos.horizontalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Data Envio", None));
#if QT_CONFIG(accessibility)
        self.tabela_historico_documentos.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Tabela de Hist\u00f3rico de Envio de Documentos feito pelo Usu\u00e1rio", None))
#endif // QT_CONFIG(accessibility)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Hist\u00f3rico de Envio de Documentos", None))
#if QT_CONFIG(accessibility)
        self.pg_enviar_doc.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"P\u00e1gina para envio de documentos", None))
#endif // QT_CONFIG(accessibility)
        self.tipo_documento.setItemText(0, QCoreApplication.translate("MainWindow", u"Escolha o tipo de arquivo", None))
        self.tipo_documento.setItemText(1, QCoreApplication.translate("MainWindow", u"CPF", None))
        self.tipo_documento.setItemText(2, QCoreApplication.translate("MainWindow", u"RG", None))
        self.tipo_documento.setItemText(3, QCoreApplication.translate("MainWindow", u"CNH", None))
        self.tipo_documento.setItemText(4, QCoreApplication.translate("MainWindow", u"PASSAPORTE", None))

#if QT_CONFIG(tooltip)
        self.tipo_documento.setToolTip(QCoreApplication.translate("MainWindow", u"Escolha o tipo de arquivo", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.tipo_documento.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Op\u00e7\u00f5es de tipos de documentos", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(tooltip)
        self.btn_arquivo_documento.setToolTip(QCoreApplication.translate("MainWindow", u"Escolher um Arquivo", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_arquivo_documento.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Bot\u00e3o para escolher o documento", None))
#endif // QT_CONFIG(accessibility)
        self.btn_arquivo_documento.setText(QCoreApplication.translate("MainWindow", u"Escolher um Arquivo", None))
#if QT_CONFIG(tooltip)
        self.btn_remover_doc.setToolTip(QCoreApplication.translate("MainWindow", u"Limpar", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_remover_doc.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Bot\u00e3o para limpar", None))
#endif // QT_CONFIG(accessibility)
        self.btn_remover_doc.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Arquivo Selecionado", None))
#if QT_CONFIG(tooltip)
        self.lista_envio_documento.setToolTip(QCoreApplication.translate("MainWindow", u"Aqui aparecer\u00e1 o caminho do documento selecionado", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.lista_envio_documento.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo onde ser\u00e1 vis\u00edvel o caminho do documento selecionado", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(tooltip)
        self.amostra_imagem.setToolTip(QCoreApplication.translate("MainWindow", u"Aqui aparecer\u00e1 uma miniatura da imagem do documento selecionado", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.amostra_imagem.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Espa\u00e7o onde aparecer\u00e1 uma miniatura da imagem do documento selecionado", None))
#endif // QT_CONFIG(accessibility)
        self.amostra_imagem.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Amostra da Imagem</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Confira os dados extra\u00eddos antes de enviar", None))
#if QT_CONFIG(tooltip)
        self.txt_dados_documento.setToolTip(QCoreApplication.translate("MainWindow", u"Aqui ir\u00e1 aparecer os dados extra\u00eddos do documento selecionado", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_dados_documento.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo de texto para exibi\u00e7\u00e3o de dados extra\u00eddos do documento", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(tooltip)
        self.btn_enviar_arquivo.setToolTip(QCoreApplication.translate("MainWindow", u"Enviar Documento", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_enviar_arquivo.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Bot\u00e3o de enviar documento", None))
#endif // QT_CONFIG(accessibility)
        self.btn_enviar_arquivo.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
#if QT_CONFIG(accessibility)
        self.pg_alteracao_perfil.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"P\u00e1gina de Altera\u00e7\u00e3o de Perfil", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.label_11.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Texto que diz: Altere seus Dados", None))
#endif // QT_CONFIG(accessibility)
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#000000;\">Altere seus Dados</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.txt_perfil_alterar_nome.setToolTip(QCoreApplication.translate("MainWindow", u"Nome", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_perfil_alterar_nome.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo para altera\u00e7\u00e3o de Nome", None))
#endif // QT_CONFIG(accessibility)
        self.txt_perfil_alterar_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Nome", None))
#if QT_CONFIG(tooltip)
        self.txt_perfil_alterar_email.setToolTip(QCoreApplication.translate("MainWindow", u"Email", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_perfil_alterar_email.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo para altera\u00e7\u00e3o de Email", None))
#endif // QT_CONFIG(accessibility)
        self.txt_perfil_alterar_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Email", None))
#if QT_CONFIG(tooltip)
        self.txt_perfil_alterar_telefone.setToolTip(QCoreApplication.translate("MainWindow", u"Telefone", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_perfil_alterar_telefone.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo para altera\u00e7\u00e3o de telefone", None))
#endif // QT_CONFIG(accessibility)
        self.txt_perfil_alterar_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Telefone", None))
#if QT_CONFIG(tooltip)
        self.btn_salvar_alteracoes.setToolTip(QCoreApplication.translate("MainWindow", u"Salvar Altera\u00e7\u00f5es", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_salvar_alteracoes.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Bot\u00e3o que salva as altera\u00e7\u00f5es feita pelo usu\u00e1rio nos dados do seu perfil", None))
#endif // QT_CONFIG(accessibility)
        self.btn_salvar_alteracoes.setText(QCoreApplication.translate("MainWindow", u"Salvar Altera\u00e7\u00f5es", None))
#if QT_CONFIG(accessibility)
        self.pg_perfil.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"P\u00e1gina de Perfil do Usu\u00e1rio", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.label_7.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Texto que diz: Perfil", None))
#endif // QT_CONFIG(accessibility)
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#000000;\">Perfil</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.txt_nome_perfil.setToolTip(QCoreApplication.translate("MainWindow", u"Meu Nome", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_nome_perfil.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo de texto que aparecer\u00e1 o nome do Usu\u00e1rio", None))
#endif // QT_CONFIG(accessibility)
        self.txt_nome_perfil.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Nome do Usu\u00e1rio</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.txt_email_perfil.setToolTip(QCoreApplication.translate("MainWindow", u"Meu Email", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_email_perfil.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo de Texto que ter\u00e1 o email do Usu\u00e1rio", None))
#endif // QT_CONFIG(accessibility)
        self.txt_email_perfil.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Email do Usu\u00e1rio</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.txt_telefone_perfil.setToolTip(QCoreApplication.translate("MainWindow", u"Meu Telefone", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txt_telefone_perfil.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Campo de texto que aparecer\u00e1 o telefone do usu\u00e1rio", None))
#endif // QT_CONFIG(accessibility)
        self.txt_telefone_perfil.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Telefone do Usu\u00e1rio</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_alterar_dados.setToolTip(QCoreApplication.translate("MainWindow", u"Alterar meus Dados", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_alterar_dados.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"Bot\u00e3o para alterar dados do Usu\u00e1rio", None))
#endif // QT_CONFIG(accessibility)
        self.btn_alterar_dados.setText(QCoreApplication.translate("MainWindow", u"Alterar meus dados", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>&copy; RuralConnect</p></body></html>", None))
    # retranslateUi

