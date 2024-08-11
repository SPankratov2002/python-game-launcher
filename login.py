# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import img


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(350, 550)
        MainWindow.setMinimumSize(QSize(350, 550))
        MainWindow.setMaximumSize(QSize(350, 550))
        icon = QIcon()
        icon.addFile(u":/my images/images/apple.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: #f1f0eb\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 200))
        self.label.setMaximumSize(QSize(200, 200))
        self.label.setPixmap(QPixmap(u":/my images/images/apple.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_9 = QLabel(self.page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font-size: 22px;\n"
"font-weight: bold;\n"
"color: #5b5a55;\n"
"border: none;")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_9)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.btn_login = QPushButton(self.page)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMinimumSize(QSize(120, 0))
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton {\n"
"padding: 4px;\n"
"background-color: #acd263;\n"
"font-size: 26px;\n"
"font-weight: bold;\n"
"border-radius: 20px;\n"
"color: #f1f0eb;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: rgba(255,255,255, 90);\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_login)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.btn_login_2 = QPushButton(self.page)
        self.btn_login_2.setObjectName(u"btn_login_2")
        self.btn_login_2.setMinimumSize(QSize(120, 0))
        self.btn_login_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login_2.setStyleSheet(u"QPushButton {\n"
"padding: 4px;\n"
"font-size: 20px;\n"
"color: #5b5a55;\n"
"border: none;\n"
"text-decoration: underline;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #919089;\n"
"}")

        self.verticalLayout.addWidget(self.btn_login_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 50, -1, 10)
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_11)

        self.frame_4 = QFrame(self.page_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(250, 60))
        self.frame_4.setMaximumSize(QSize(250, 60))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.last_name = QLineEdit(self.frame_4)
        self.last_name.setObjectName(u"last_name")
        self.last_name.setGeometry(QRect(0, 20, 250, 40))
        self.last_name.setMinimumSize(QSize(250, 40))
        self.last_name.setMaximumSize(QSize(250, 16777215))
        self.last_name.setStyleSheet(u"color: #5b5a55;\n"
"font-size: 22px;\n"
"font-weight: bold;\n"
"border:2px solid #5b5a55;\n"
"border-radius: 20px")
        self.last_name.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.last_name.setMaxLength(100)
        self.last_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.last_name.setPlaceholderText(u"\u0418\u0432\u0430\u043d\u043e\u0432")
        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 0, 121, 30))
        self.label_12.setStyleSheet(u"font-size: 22px;\n"
"font-weight: bold;\n"
"color: #5b5a55;\n"
"border: none;")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.frame_4)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_12)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 10)
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_13)

        self.frame_5 = QFrame(self.page_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(250, 60))
        self.frame_5.setMaximumSize(QSize(250, 60))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.first_name = QLineEdit(self.frame_5)
        self.first_name.setObjectName(u"first_name")
        self.first_name.setGeometry(QRect(0, 20, 250, 40))
        self.first_name.setMinimumSize(QSize(250, 40))
        self.first_name.setMaximumSize(QSize(250, 16777215))
        self.first_name.setStyleSheet(u"color: #5b5a55;\n"
"border: none;\n"
"font-size: 22px;\n"
"font-weight: bold;\n"
"border:2px solid #5b5a55;\n"
"border-radius: 20px")
        self.first_name.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.first_name.setMaxLength(100)
        self.first_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.first_name.setPlaceholderText(u"\u0418\u0432\u0430\u043d")
        self.label_14 = QLabel(self.frame_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 0, 121, 30))
        self.label_14.setStyleSheet(u"font-size: 22px;\n"
"font-weight: bold;\n"
"color: #5b5a55;\n"
"border: none;")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.frame_5)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_14)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 10)
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_15)

        self.frame_6 = QFrame(self.page_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(250, 60))
        self.frame_6.setMaximumSize(QSize(250, 60))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.acronim = QLineEdit(self.frame_6)
        self.acronim.setObjectName(u"acronim")
        self.acronim.setGeometry(QRect(0, 20, 250, 40))
        self.acronim.setMinimumSize(QSize(250, 40))
        self.acronim.setMaximumSize(QSize(250, 16777215))
        self.acronim.setStyleSheet(u"color: #5b5a55;\n"
"border: none;\n"
"font-size: 22px;\n"
"font-weight: bold;\n"
"border:2px solid #5b5a55;\n"
"border-radius: 20px")
        self.acronim.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.acronim.setMaxLength(100)
        self.acronim.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.acronim.setPlaceholderText(u"\u0418\u0432\u0430\u043d\u043e\u0432\u0438\u0447")
        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 0, 121, 30))
        self.label_15.setStyleSheet(u"font-size: 22px;\n"
"font-weight: bold;\n"
"color: #5b5a55;\n"
"border: none;")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.frame_6)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_16)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 50)
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_17)

        self.frame_7 = QFrame(self.page_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(250, 60))
        self.frame_7.setMaximumSize(QSize(250, 60))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.date = QLineEdit(self.frame_7)
        self.date.setObjectName(u"date")
        self.date.setGeometry(QRect(0, 20, 250, 40))
        self.date.setMinimumSize(QSize(250, 40))
        self.date.setMaximumSize(QSize(250, 16777215))
        self.date.setStyleSheet(u"color: #5b5a55;\n"
"border: none;\n"
"font-size: 22px;\n"
"font-weight: bold;\n"
"border:2px solid #5b5a55;\n"
"border-radius: 20px")
        self.date.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.date.setMaxLength(100)
        self.date.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.date.setPlaceholderText(u"16.11.1991")
        self.label_16 = QLabel(self.frame_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 0, 181, 30))
        self.label_16.setStyleSheet(u"font-size: 22px;\n"
"font-weight: bold;\n"
"color: #5b5a55;\n"
"border: none;")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.frame_7)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_18)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.btn_create = QPushButton(self.page_2)
        self.btn_create.setObjectName(u"btn_create")
        self.btn_create.setMinimumSize(QSize(120, 0))
        self.btn_create.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_create.setStyleSheet(u"QPushButton {\n"
"padding: 4px;\n"
"background-color: #acd263;\n"
"font-size: 26px;\n"
"font-weight: bold;\n"
"border-radius: 20px;\n"
"color: #f1f0eb;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: rgba(255,255,255, 90);\n"
"}")

        self.horizontalLayout_10.addWidget(self.btn_create)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.btn_cancel = QPushButton(self.page_2)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setMinimumSize(QSize(120, 0))
        self.btn_cancel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancel.setStyleSheet(u"QPushButton {\n"
"padding: 4px;\n"
"background-color: #f16a6d;\n"
"font-size: 26px;\n"
"font-weight: bold;\n"
"border-radius: 20px;\n"
"color: #f1f0eb;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: rgba(255,255,255, 90);\n"
"}")

        self.horizontalLayout_10.addWidget(self.btn_cancel)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.label_10 = QLabel(self.page_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 50))
        self.label_10.setStyleSheet(u"font-size: 16px;\n"
"color: #5b5a55;\n"
"border: none;")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_10)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
        self.label.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c!", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.btn_login_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u043e\u0433\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.last_name.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.first_name.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.acronim.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.date.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.btn_create.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.btn_cancel.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u043f\u043e\u0441\u043b\u0435 \u0432\u043d\u0435\u0441\u0435\u043d\u0438\u044f \u043c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

