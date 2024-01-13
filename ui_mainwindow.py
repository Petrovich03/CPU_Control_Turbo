# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(347, 135)
        MainWindow.setMinimumSize(QSize(347, 135))
        MainWindow.setMaximumSize(QSize(347, 135))
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Times New Roman\";")
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.done = QPushButton(self.frame)
        self.done.setObjectName(u"done")
        self.done.setGeometry(QRect(20, 70, 291, 30))
        self.done.setMaximumSize(QSize(300, 30))
        self.done.setStyleSheet(u"background-color: rgb(231, 231, 231);\n"
"font: 700 12pt \"Times New Roman\";")
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 20, 264, 21))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.info_max = QLabel(self.layoutWidget)
        self.info_max.setObjectName(u"info_max")
        self.info_max.setStyleSheet(u"font: 700 12pt \"Times New Roman\";")

        self.horizontalLayout.addWidget(self.info_max)

        self.max_ghz = QLabel(self.layoutWidget)
        self.max_ghz.setObjectName(u"max_ghz")
        self.max_ghz.setStyleSheet(u"font: italic 12pt \"Times New Roman\";")

        self.horizontalLayout.addWidget(self.max_ghz)


        self.horizontalLayout_3.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CPU Control Turbo", None))
        self.done.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0431\u043b\u043e\u043a\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0447\u0430\u0441\u0442\u043e\u0442\u043e\u0439", None))
        self.info_max.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u043c\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u041c\u0413\u0446:", None))
        self.max_ghz.setText(QCoreApplication.translate("MainWindow", u"None", None))
    # retranslateUi

