# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'apple_launcher.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTextEdit,
    QVBoxLayout, QWidget)
import img

class Ui_AppleLauncher(object):
    def setupUi(self, AppleLauncher):
        if not AppleLauncher.objectName():
            AppleLauncher.setObjectName(u"AppleLauncher")
        AppleLauncher.resize(1200, 700)
        AppleLauncher.setMinimumSize(QSize(1200, 250))
        AppleLauncher.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Arial"])
        AppleLauncher.setFont(font)
        icon = QIcon()
        icon.addFile(u"images/apple.png", QSize(), QIcon.Normal, QIcon.Off)
        AppleLauncher.setWindowIcon(icon)
        AppleLauncher.setStyleSheet(u"background-color: #f1f0eb\n"
"")
        self.centralwidget = QWidget(AppleLauncher)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 60))
        self.frame.setMaximumSize(QSize(16777215, 60))
        self.frame.setStyleSheet(u"QFrame {\n"
"border-bottom: 2px solid black;\n"
"color: #5b5a55;\n"
"border-radius: 30px;\n"
"border: none\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_main = QPushButton(self.frame)
        self.btn_main.setObjectName(u"btn_main")
        self.btn_main.setMinimumSize(QSize(165, 0))
        self.btn_main.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_main.setStyleSheet(u"QPushButton {\n"
"background-color: transparent;\n"
"font-size: 26px;\n"
"font-weight: bold;\n"
"color: #5b5a55;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: rgba(91,90,85, 90);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"color: rgba(91,90,85, 90);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/my images/images/apple.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_main.setIcon(icon1)
        self.btn_main.setIconSize(QSize(42, 42))

        self.horizontalLayout.addWidget(self.btn_main)

        self.btn_manual = QPushButton(self.frame)
        self.btn_manual.setObjectName(u"btn_manual")
        self.btn_manual.setMinimumSize(QSize(165, 0))
        self.btn_manual.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_manual.setStyleSheet(u"QPushButton {\n"
"background-color: transparent;\n"
"font-size: 26px;\n"
"font-weight: bold;\n"
"color: #5b5a55;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: rgba(91,90,85, 90);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"color: rgba(91,90,85, 90);\n"
"}")
        self.btn_manual.setIconSize(QSize(42, 42))

        self.horizontalLayout.addWidget(self.btn_manual)

        self.search_fio = QLineEdit(self.frame)
        self.search_fio.setObjectName(u"search_fio")
        self.search_fio.setMinimumSize(QSize(250, 0))
        self.search_fio.setMaximumSize(QSize(300, 16777215))
        self.search_fio.setStyleSheet(u"color: #5b5a55;\n"
"border: none;\n"
"font-size: 26px;\n"
"font-weight: bold;\n"
"border-bottom:2px solid #5b5a55;\n"
"padding-left: 0px")
        self.search_fio.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.search_fio.setMaxLength(100)
        self.search_fio.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.search_fio.setPlaceholderText(u"Поиск по ФИО")

        self.horizontalLayout.addWidget(self.search_fio)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_exit = QPushButton(self.frame)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMinimumSize(QSize(110, 0))
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setStyleSheet(u"QPushButton {\n"
"background-color: #afd275;\n"
"font-size: 26px;\n"
"font-weight: bold;\n"
"color: white;\n"
"border: none;\n"
"border-radius: 10px;\n"
"padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(157, 188, 105);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_exit)


        self.verticalLayout.addWidget(self.frame)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 1))
        self.line.setStyleSheet(u"background-color: #f16a6d;")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_14 = QHBoxLayout(self.page_3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_9 = QFrame(self.page_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(300, 60))
        self.frame_9.setMaximumSize(QSize(16777215, 60))
        self.frame_9.setStyleSheet(u"QFrame {\n"
"background-color:rgba(0, 0, 0, 0.07);\n"
"border: none;\n"
"}")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.btn_ln = QPushButton(self.frame_9)
        self.btn_ln.setObjectName(u"btn_ln")
        self.btn_ln.setMinimumSize(QSize(251, 0))
        self.btn_ln.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setUnderline(True)
        self.btn_ln.setFont(font1)
        self.btn_ln.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ln.setStyleSheet(u"QPushButton {\n"
"background-color: transparent;\n"
"padding: 4px;\n"
"font-size: 26px;\n"
"border: none;\n"
"border-right: 2px solid #5b5a55;\n"
"color: #5b5a55;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #919089;\n"
"}")

        self.horizontalLayout_12.addWidget(self.btn_ln)

        self.btn_fn = QPushButton(self.frame_9)
        self.btn_fn.setObjectName(u"btn_fn")
        self.btn_fn.setMinimumSize(QSize(251, 0))
        self.btn_fn.setMaximumSize(QSize(16777215, 16777215))
        self.btn_fn.setFont(font1)
        self.btn_fn.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_fn.setStyleSheet(u"QPushButton {\n"
"background-color: transparent;\n"
"padding: 4px;\n"
"font-size: 26px;\n"
"border: none;\n"
"border-right: 2px solid #5b5a55;\n"
"color: #5b5a55;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #919089;\n"
"}")

        self.horizontalLayout_12.addWidget(self.btn_fn)

        self.btn_acr = QPushButton(self.frame_9)
        self.btn_acr.setObjectName(u"btn_acr")
        self.btn_acr.setMinimumSize(QSize(251, 0))
        self.btn_acr.setMaximumSize(QSize(16777215, 16777215))
        self.btn_acr.setFont(font1)
        self.btn_acr.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_acr.setStyleSheet(u"QPushButton {\n"
"padding: 4px;\n"
"font-size: 26px;\n"
"border: none;\n"
"border-right: 2px solid #5b5a55;\n"
"background-color: transparent;\n"
"color: #5b5a55;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #919089;\n"
"}")

        self.horizontalLayout_12.addWidget(self.btn_acr)

        self.btn_age = QPushButton(self.frame_9)
        self.btn_age.setObjectName(u"btn_age")
        self.btn_age.setMinimumSize(QSize(250, 0))
        self.btn_age.setMaximumSize(QSize(16777215, 16777215))
        self.btn_age.setFont(font1)
        self.btn_age.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_age.setStyleSheet(u"QPushButton {\n"
"background-color: transparent;\n"
"padding: 4px;\n"
"font-size: 26px;\n"
"border-radius: 20px;\n"
"color: #5b5a55;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #919089;\n"
"}")

        self.horizontalLayout_12.addWidget(self.btn_age)


        self.verticalLayout_8.addWidget(self.frame_9)

        self.scrollArea_2 = QScrollArea(self.page_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(800, 0))
        self.scrollArea_2.setStyleSheet(u"QWidget {\n"
"	background-color:rgba(0, 0, 0, 0.05);\n"
"	border: none;\n"
"	font-size: 20px;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"    {\n"
"        background-color: transparent;\n"
"        width: 15px;\n"
"        margin: 15px 3px 15px 3px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:vertical\n"
"    {\n"
"       background-color: rgba(71,74,79, 70);\n"
"        min-height: 5px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        background-color: transparent;\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        background-color: transparent;\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollB"
                        "ar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"    {\n"
"        background-color: transparent;\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"    {\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"    {\n"
"        background-color: transparent;\n"
"    }\n"
"\n"
"    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"    {\n"
"        background-color: transparent;\n"
"    }")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1178, 539))
        self.scrollAreaWidgetContents_2.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_3 = QSpacerItem(20, 452, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_8.addWidget(self.scrollArea_2)


        self.horizontalLayout_14.addLayout(self.verticalLayout_8)

        self.stackedWidget.addWidget(self.page_3)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_7 = QHBoxLayout(self.page)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_4 = QFrame(self.page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(300, 60))
        self.frame_4.setMaximumSize(QSize(370, 60))
        self.frame_4.setStyleSheet(u"QFrame {\n"
"background-color: #afd275;\n"
"border: none;\n"
"border-radius: 10px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size: 26px;\n"
"font-weight: bold;\n"
"color: #f1f0eb;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(300, 200))
        self.frame_2.setMaximumSize(QSize(370, 200))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"background-color: #f1f0eb;\n"
"border: 2px solid #afd275;\n"
"border-radius: 10px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_info_ln = QLabel(self.frame_2)
        self.label_info_ln.setObjectName(u"label_info_ln")
        self.label_info_ln.setStyleSheet(u"font-size: 22px;\n"
"font-weight: bold;\n"
"color: #5b5a55;\n"
"border: none;\n"
"padding-left: 30px;")
        self.label_info_ln.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_info_ln)

        self.label_info_fn = QLabel(self.frame_2)
        self.label_info_fn.setObjectName(u"label_info_fn")
        self.label_info_fn.setStyleSheet(u"font-size: 22px;\n"
"font-weight: bold;\n"
"color: #5b5a55;\n"
"border: none;\n"
"padding-left: 30px;")
        self.label_info_fn.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_info_fn)

        self.label_info_acr = QLabel(self.frame_2)
        self.label_info_acr.setObjectName(u"label_info_acr")
        self.label_info_acr.setStyleSheet(u"font-size: 22px;\n"
"font-weight: bold;\n"
"color: #5b5a55;\n"
"border: none;\n"
"padding-left: 30px;")
        self.label_info_acr.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_info_acr)

        self.label_info_age = QLabel(self.frame_2)
        self.label_info_age.setObjectName(u"label_info_age")
        self.label_info_age.setStyleSheet(u"font-size: 22px;\n"
"font-weight: bold;\n"
"color: #5b5a55;\n"
"border: none;\n"
"padding-left: 30px;")
        self.label_info_age.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_info_age)

        self.label_info_bs = QLabel(self.frame_2)
        self.label_info_bs.setObjectName(u"label_info_bs")
        self.label_info_bs.setStyleSheet(u"font-size: 22px;\n"
"font-weight: bold;\n"
"color: #5b5a55;\n"
"border: none;\n"
"padding-left: 30px;")
        self.label_info_bs.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_info_bs)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame_5 = QFrame(self.page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(300, 60))
        self.frame_5.setMaximumSize(QSize(370, 60))
        self.frame_5.setStyleSheet(u"QFrame {\n"
"background-color: #afd275;\n"
"border: none;\n"
"border-radius: 10px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font-size: 26px;\n"
"font-weight: bold;\n"
"color: #f1f0eb;")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_7)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(300, 200))
        self.frame_6.setMaximumSize(QSize(370, 200))
        self.frame_6.setStyleSheet(u"QFrame {\n"
"background-color: #f1f0eb;\n"
"border: 2px solid #afd275;\n"
"border-radius: 10px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font-size: 22px;\n"
"font-weight: bold;\n"
"color: #5b5a55;\n"
"border: none;\n"
"margin-left: 15px;")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_8)

        self.lineEdit = QLineEdit(self.frame_6)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(50, 16777215))
        self.lineEdit.setStyleSheet(u"color: #5b5a55;\n"
"border: none;\n"
"font-size: 22px;\n"
"font-weight: bold;\n"
"border:2px solid #5b5a55;\n"
"border-radius: 10px")
        self.lineEdit.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhNoTextHandles)
        self.lineEdit.setMaxLength(2)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font-size: 22px;\n"
"font-weight: bold;\n"
"color: #5b5a55;\n"
"border: none;\n"
"margin-left: 15px;")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_11)

        self.lineEdit_2 = QLineEdit(self.frame_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_2.setStyleSheet(u"color: #5b5a55;\n"
"border: none;\n"
"font-size: 22px;\n"
"font-weight: bold;\n"
"border:2px solid #5b5a55;\n"
"border-radius: 10px")
        self.lineEdit_2.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhNoTextHandles)
        self.lineEdit_2.setMaxLength(2)
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.lineEdit_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.btn_start = QPushButton(self.frame_6)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setMinimumSize(QSize(95, 0))
        self.btn_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_start.setStyleSheet(u"QPushButton {\n"
"padding: 4px;\n"
"background-color: #f16a6d;\n"
"font-size: 26px;\n"
"font-weight: bold;\n"
"border-radius: 10px;\n"
"color: #f1f0eb;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: rgba(255,255,255, 90);\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_start)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.frame_8 = QFrame(self.page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(200, 50))
        self.frame_8.setMaximumSize(QSize(370, 16777215))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.btn_export_table = QPushButton(self.frame_8)
        self.btn_export_table.setObjectName(u"btn_export_table")
        self.btn_export_table.setMinimumSize(QSize(95, 35))
        self.btn_export_table.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export_table.setStyleSheet(u"QPushButton {\n"
"padding: 4px;\n"
"background-color:#afd275;\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"border-radius: 10px;\n"
"color: #f1f0eb;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: rgba(255,255,255, 90);\n"
"}")

        self.horizontalLayout_10.addWidget(self.btn_export_table)

        self.btn_refresh = QPushButton(self.frame_8)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setMinimumSize(QSize(95, 35))
        self.btn_refresh.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_refresh.setStyleSheet(u"QPushButton {\n"
"padding: 4px;\n"
"background-color: #afd275;\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"border-radius: 10px;\n"
"color: #f1f0eb;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: rgba(255,255,255, 90);\n"
"}")

        self.horizontalLayout_10.addWidget(self.btn_refresh)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)

        self.btn_delete_user = QPushButton(self.frame_8)
        self.btn_delete_user.setObjectName(u"btn_delete_user")
        self.btn_delete_user.setMinimumSize(QSize(95, 35))
        self.btn_delete_user.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete_user.setStyleSheet(u"QPushButton {\n"
"padding: 4px;\n"
"background-color: #f16a6d;\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"border-radius: 10px;\n"
"color: #f1f0eb;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: rgba(255,255,255, 90);\n"
"}")

        self.horizontalLayout_10.addWidget(self.btn_delete_user)


        self.verticalLayout_4.addWidget(self.frame_8)


        self.horizontalLayout_7.addLayout(self.verticalLayout_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_7 = QFrame(self.page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(300, 60))
        self.frame_7.setMaximumSize(QSize(16777215, 60))
        self.frame_7.setStyleSheet(u"QFrame {\n"
"background-color:rgba(0, 0, 0, 0.08);\n"
"	border: none;;\n"
"}")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_score = QPushButton(self.frame_7)
        self.btn_score.setObjectName(u"btn_score")
        self.btn_score.setMinimumSize(QSize(150, 0))
        self.btn_score.setMaximumSize(QSize(16777215, 16777215))
        self.btn_score.setFont(font1)
        self.btn_score.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_score.setStyleSheet(u"QPushButton {\n"
"padding: 4px;\n"
"font-size: 26px;\n"
"background-color: transparent;\n"
"color: #5b5a55;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #919089;\n"
"}")

        self.horizontalLayout_11.addWidget(self.btn_score)

        self.btn_ftime = QPushButton(self.frame_7)
        self.btn_ftime.setObjectName(u"btn_ftime")
        self.btn_ftime.setMinimumSize(QSize(150, 0))
        self.btn_ftime.setMaximumSize(QSize(16777215, 16777215))
        self.btn_ftime.setFont(font1)
        self.btn_ftime.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ftime.setStyleSheet(u"QPushButton {\n"
"padding: 4px;\n"
"font-size: 26px;\n"
"background-color: transparent;\n"
"color: #5b5a55;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #919089;\n"
"}")

        self.horizontalLayout_11.addWidget(self.btn_ftime)

        self.btn_mtime = QPushButton(self.frame_7)
        self.btn_mtime.setObjectName(u"btn_mtime")
        self.btn_mtime.setMinimumSize(QSize(150, 0))
        self.btn_mtime.setMaximumSize(QSize(16777215, 16777215))
        self.btn_mtime.setFont(font1)
        self.btn_mtime.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_mtime.setStyleSheet(u"QPushButton {\n"
"padding: 4px;\n"
"font-size: 26px;\n"
"background-color: transparent;\n"
"color: #5b5a55;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #919089;\n"
"}")

        self.horizontalLayout_11.addWidget(self.btn_mtime)

        self.btn_data_score = QPushButton(self.frame_7)
        self.btn_data_score.setObjectName(u"btn_data_score")
        self.btn_data_score.setMinimumSize(QSize(150, 0))
        self.btn_data_score.setMaximumSize(QSize(16777215, 16777215))
        self.btn_data_score.setFont(font1)
        self.btn_data_score.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_data_score.setStyleSheet(u"QPushButton {\n"
"padding: 4px;\n"
"background-color: transparent;\n"
"font-size: 26px;\n"
"color: #5b5a55;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #919089;\n"
"}")

        self.horizontalLayout_11.addWidget(self.btn_data_score)


        self.verticalLayout_7.addWidget(self.frame_7)

        self.scrollArea = QScrollArea(self.page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(800, 0))
        self.scrollArea.setStyleSheet(u"QWidget {\n"
"	font-size: 20px;\n"
"	background-color:rgba(0, 0, 0, 0.05);\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"    {\n"
"        background-color: transparent;\n"
"        width: 15px;\n"
"        margin: 15px 3px 15px 3px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:vertical\n"
"    {\n"
"       background-color: rgba(71,74,79, 70);\n"
"        min-height: 5px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        background-color: transparent;\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        background-color: transparent;\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollB"
                        "ar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"    {\n"
"        background-color: transparent;\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"    {\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"    {\n"
"        background-color: transparent;\n"
"    }\n"
"\n"
"    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"    {\n"
"        background-color: transparent;\n"
"    }")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 800, 543))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_7.addWidget(self.scrollArea)


        self.horizontalLayout_7.addLayout(self.verticalLayout_7)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_5 = QVBoxLayout(self.page_2)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, 20, 20, 20)
        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font-size: 22px;\n"
"font-weight: bold;\n"
"color: #5b5a55;\n"
"border: none;")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(550, 320))
        self.label.setMaximumSize(QSize(550, 320))
        self.label.setStyleSheet(u"border: 4px solid #afd275")
        self.label.setPixmap(QPixmap(u":/my images/images/image1.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)

        self.horizontalLayout_8.addWidget(self.label)

        self.label_10 = QLabel(self.page_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(550, 320))
        self.label_10.setMaximumSize(QSize(550, 320))
        self.label_10.setStyleSheet(u"border: 4px solid #afd275")
        self.label_10.setPixmap(QPixmap(u":/my images/images/image2.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setWordWrap(False)

        self.horizontalLayout_8.addWidget(self.label_10)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.textEdit = QTextEdit(self.page_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"font-size: 22px;\n"
"font-weight: bold;\n"
"color: #5b5a55;\n"
"border: none;")
        self.textEdit.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.textEdit)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame_3)

        AppleLauncher.setCentralWidget(self.centralwidget)

        self.retranslateUi(AppleLauncher)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AppleLauncher)
    # setupUi

    def retranslateUi(self, AppleLauncher):
        AppleLauncher.setWindowTitle(QCoreApplication.translate("AppleLauncher", u"Apple Garden", None))
        self.btn_main.setText(QCoreApplication.translate("AppleLauncher", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.btn_manual.setText(QCoreApplication.translate("AppleLauncher", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f", None))
        self.search_fio.setText("")
        self.btn_exit.setText(QCoreApplication.translate("AppleLauncher", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.btn_ln.setText(QCoreApplication.translate("AppleLauncher", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.btn_fn.setText(QCoreApplication.translate("AppleLauncher", u"\u0418\u043c\u044f", None))
        self.btn_acr.setText(QCoreApplication.translate("AppleLauncher", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.btn_age.setText(QCoreApplication.translate("AppleLauncher", u"\u0412\u043e\u0437\u0440\u0430\u0441\u0442", None))
        self.label_2.setText(QCoreApplication.translate("AppleLauncher", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0435", None))
        self.label_info_ln.setText(QCoreApplication.translate("AppleLauncher", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f:", None))
        self.label_info_fn.setText(QCoreApplication.translate("AppleLauncher", u"\u0418\u043c\u044f:", None))
        self.label_info_acr.setText(QCoreApplication.translate("AppleLauncher", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e:", None))
        self.label_info_age.setText(QCoreApplication.translate("AppleLauncher", u"\u0412\u043e\u0437\u0440\u0430\u0441\u0442:", None))
        self.label_info_bs.setText(QCoreApplication.translate("AppleLauncher", u"\u0420\u0435\u043a\u043e\u0440\u0434: 0 \u0431\u0430\u043b\u043b\u043e\u0432", None))
        self.label_7.setText(QCoreApplication.translate("AppleLauncher", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0438 \u0437\u0430\u043f\u0443\u0441\u043a", None))
        self.label_8.setText(QCoreApplication.translate("AppleLauncher", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0443\u0440\u043e\u0432\u043d\u0435\u0439: ", None))
        self.lineEdit.setText(QCoreApplication.translate("AppleLauncher", u"10", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("AppleLauncher", u" 10", None))
        self.label_11.setText(QCoreApplication.translate("AppleLauncher", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c (5-15\u043a\u043c/\u0447 ):", None))
        self.lineEdit_2.setText(QCoreApplication.translate("AppleLauncher", u"5", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("AppleLauncher", u"5", None))
        self.btn_start.setText(QCoreApplication.translate("AppleLauncher", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.btn_export_table.setText(QCoreApplication.translate("AppleLauncher", u"\u0412\u044b\u0432\u043e\u0434", None))
        self.btn_refresh.setText(QCoreApplication.translate("AppleLauncher", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.btn_delete_user.setText(QCoreApplication.translate("AppleLauncher", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btn_score.setText(QCoreApplication.translate("AppleLauncher", u"\u0421\u0447\u0451\u0442", None))
        self.btn_ftime.setText(QCoreApplication.translate("AppleLauncher", u"\u0412\u0440\u0435\u043c\u044f", None))
        self.btn_mtime.setText(QCoreApplication.translate("AppleLauncher", u"\u0421\u0440\u0435\u0434. \u0432\u0440\u0435\u043c\u044f", None))
        self.btn_data_score.setText(QCoreApplication.translate("AppleLauncher", u"\u0414\u0430\u0442\u0430", None))
        self.label_9.setText(QCoreApplication.translate("AppleLauncher", u"\u0412\u0430\u0448\u0430 \u0437\u0430\u0434\u0430\u0447\u0430, \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u044f \u0440\u0443\u043b\u0435\u0432\u043e\u0435 \u043a\u043e\u043b\u0435\u0441\u043e, \u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u044c \u0432\u0434\u043e\u043b\u044c \u0434\u043e\u0440\u043e\u0433\u0438 \u043f\u043e \u0444\u0440\u0443\u043a\u0442\u043e\u0432\u043e\u043c\u0443 \u0441\u0430\u0434\u0443.", None))
        self.label.setText("")
        self.label_10.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("AppleLauncher", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:22px; font-weight:700; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22px;\">\u041f\u0440\u0438 \u043f\u043e\u044f\u0432\u043b\u0435\u043d\u0438\u0438 \u043d\u0430 \u0434\u0435\u0440\u0435\u0432\u0435 \u0441\u043b\u0435\u0432\u0430 \u0438\u043b\u0438 \u0441\u043f\u0440\u0430\u0432\u0430 \u043e\u0442 \u0434\u043e\u0440\u043e\u0433\u0438 \u044f\u0431\u043b\u043e\u043a, \u0438\u043c\u0435\u044e\u0449\u0438\u0445 \u0440\u0430\u0437"
                        "\u043d\u044b\u0439 \u0443\u0432\u0435\u0442 (\u043a\u0440\u0430\u0441\u043d\u044b\u0439, \u0436\u0451\u043b\u0442\u044b\u0439 \u0438\u043b\u0438 \u0437\u0435\u043b\u0451\u043d\u043d\u044b\u0439), \u0441\u043b\u0435\u0434\u0443\u0435\u0442 \u043a\u0430\u043a \u043c\u043e\u0436\u043d\u043e \u0431\u044b\u0441\u0442\u0440\u0435\u0435 \u0441\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0432\u0441\u0435 \u044f\u0431\u043b\u043e\u043a\u0438 \u0437\u0435\u043b\u0435\u043d\u043e\u0433\u043e \u0438 \u043a\u0440\u0430\u0441\u043d\u043e\u0433\u043e \u0446\u0432\u0435\u0442\u0430, \u0436\u0435\u043b\u0442\u044b\u0435 \u043f\u0440\u043e\u043f\u0443\u0441\u0442\u0438\u0442\u044c. \u041f\u0440\u0438 \u043f\u043e\u044f\u0432\u043b\u0435\u043d\u0438\u0438 \u043e\u0442\u0432\u0435\u0442\u0430 \u0441 \u0443\u043a\u0430\u0437\u0430\u043d\u0438\u0435\u043c \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0430 \u0437\u0435\u043b\u0435\u043d\u043d\u044b\u0445 \u0438\u043b\u0438 \u043a\u0440\u0430\u0441\u043d\u044b\u0445 \u044f"
                        "\u0431\u043b\u043e\u043a \u0441\u043b\u0435\u0434\u0443\u0435\u0442 \u043a\u0430\u043a \u043c\u043e\u0436\u043d\u043e \u0431\u044b\u0441\u0442\u0440\u0435\u0435 \u043d\u0430\u0436\u0430\u0442\u044c \u043f\u0440\u0430\u0432\u044b\u0439 \u043b\u0435\u043f\u0435\u0441\u0442\u043e\u043a \u0440\u0443\u043b\u044f \u00ab\u0412\u0435\u0440\u043d\u043e\u00bb, \u0435\u0441\u043b\u0438 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u044f\u0431\u043b\u043e\u043a \u0443\u043a\u0430\u0437\u0430\u043d\u043e \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e, \u0438\u043d\u0430\u0447\u0435 - \u043d\u0430\u0436\u0438\u043c\u0430\u0442\u044c \u043b\u0435\u0432\u044b\u0439 \u043b\u0435\u043f\u0435\u0441\u0442\u043e\u043a \u0440\u0443\u043b\u044f \u00ab\u041d\u0435\u0432\u0435\u0440\u043d\u043e\u00bb.</span></p></body></html>", None))
    # retranslateUi

    def create_table_users(self):
        self.rows = QFrame(self.scrollAreaWidgetContents_2)
        self.rows.setObjectName(u"frame_10")
        self.rows.setMinimumSize(QSize(300, 60))
        self.rows.setMaximumSize(QSize(16777215, 60))
        self.rows.setCursor(QCursor(Qt.PointingHandCursor))
        self.rows.setStyleSheet(u"QFrame {\n"
                                        "background-color:rgba(0, 0, 0, 0.05);\n"
                                        "border: none;\n"
                                        "}\n"
                                        "\n"
                                        "QFrame:hover {\n"
                                        "background-color: #afd275;\n"
                                        "}")
        self.rows.setFrameShape(QFrame.Shape.StyledPanel)
        self.rows.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.rows)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_last_name = QLabel(self.rows)
        self.label_last_name.setObjectName(u"label_last_name")
        self.label_last_name.setMinimumSize(QSize(250, 0))
        self.label_last_name.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setBold(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        self.label_last_name.setFont(font2)
        self.label_last_name.setStyleSheet(u"font-size: 22px;\n"
                                               "color: #5b5a55;\n"
                                               "border: none;\n"
                                               "background-color: transparent;")
        self.label_last_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_13.addWidget(self.label_last_name)

        self.label_first_name = QLabel(self.rows)
        self.label_first_name.setObjectName(u"label_first_name")
        self.label_first_name.setMinimumSize(QSize(250, 0))
        self.label_first_name.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setBold(False)
        self.label_first_name.setFont(font3)
        self.label_first_name.setStyleSheet(u"font-size: 22px;\n"
                                                "color: #5b5a55;\n"
                                                "border: none;\n"
                                                "background-color: transparent;")
        self.label_first_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_13.addWidget(self.label_first_name)

        self.label_acronim = QLabel(self.rows)
        self.label_acronim.setObjectName(u"label_acronim")
        self.label_acronim.setMinimumSize(QSize(250, 0))
        self.label_acronim.setMaximumSize(QSize(16777215, 16777215))
        self.label_acronim.setFont(font3)
        self.label_acronim.setStyleSheet(u"font-size: 22px;\n"
                                             "background-color: transparent;\n"
                                             "color: #5b5a55;\n"
                                             "border: none;\n")

        self.label_acronim.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_13.addWidget(self.label_acronim)

        self.label_age = QLabel(self.rows)
        self.label_age.setObjectName(u"label_age")
        self.label_age.setMinimumSize(QSize(250, 0))
        self.label_age.setMaximumSize(QSize(16777215, 16777215))
        self.label_age.setStyleSheet(u"font-size: 22px;\n"
                                         "color: #5b5a55;\n"
                                         "border: none;\n"
                                         "background-color: transparent;\n"
                                         "")
        self.label_age.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_13.addWidget(self.label_age)

        self.label_id = QLabel(self.rows)
        self.label_id.setObjectName(u"label_age")
        self.label_id.setMinimumSize(QSize(0, 0))
        self.label_id.setMaximumSize(QSize(0, 0))
        self.label_id.setStyleSheet(u"color: transparent;\n"
                                     "background-color: transparent;\n"
                                     "")
        self.label_id.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_13.addWidget(self.label_id)

        return self.rows, self.label_last_name, self.label_first_name, self.label_acronim, self.label_age, self.label_id

    def create_table_results(self):
        self.rows_2 = QFrame(self.scrollAreaWidgetContents)
        self.rows_2.setObjectName(u"frame_8")
        self.rows_2.setMinimumSize(QSize(300, 60))
        self.rows_2.setMaximumSize(QSize(16777215, 60))
        self.rows_2.setStyleSheet(u"QFrame {\n"
                                       "background-color:rgba(0, 0, 0, 0.05);\n"
                                        "border: none;\n"
                                       "}")
        self.rows_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.rows_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.rows_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_score = QLabel(self.rows_2)
        self.label_score.setObjectName(u"label_score")
        self.label_score.setMinimumSize(QSize(150, 0))
        self.label_score.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setBold(True)
        font4.setUnderline(False)
        font4.setStrikeOut(False)
        self.label_score.setFont(font4)
        self.label_score.setStyleSheet(u"font-size: 24px;\n"
                                           "color: #5b5a55;\n"
                                         "border: none;\n"
                                         "background-color: transparent;\n")
        self.label_score.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_score)

        self.label_ftime = QLabel(self.rows_2)
        self.label_ftime.setObjectName(u"label_ftime")
        self.label_ftime.setMinimumSize(QSize(150, 0))
        self.label_ftime.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setBold(True)
        self.label_ftime.setFont(font5)
        self.label_ftime.setStyleSheet(u"font-size: 24px;\n"
                                           "color: #5b5a55;\n"
                                         "border: none;\n"
                                         "background-color: transparent;\n")
        self.label_ftime.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_ftime)

        self.label_mtime = QLabel(self.rows_2)
        self.label_mtime.setObjectName(u"label_mtime")
        self.label_mtime.setMinimumSize(QSize(150, 0))
        self.label_mtime.setMaximumSize(QSize(16777215, 16777215))
        self.label_mtime.setFont(font5)
        self.label_mtime.setStyleSheet(u"font-size: 24px;\n"
                                           "color: #5b5a55;\n"
                                         "border: none;\n"
                                         "background-color: transparent;\n")
        self.label_mtime.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_mtime)

        self.label_data_result = QLabel(self.rows_2)
        self.label_data_result.setObjectName(u"label_16")
        self.label_data_result.setMinimumSize(QSize(150, 0))
        self.label_data_result.setMaximumSize(QSize(16777215, 16777215))
        self.label_data_result.setStyleSheet(u"font-size: 24px;\n"
                                        "color: #5b5a55;\n"
                                         "border: none;\n"
                                         "background-color: transparent;\n")
        self.label_data_result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_data_result)

        return self.rows_2, self.label_score, self.label_ftime, self.label_mtime, self.label_data_result