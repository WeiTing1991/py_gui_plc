# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(1200, 800)
        self.verticalLayout = QVBoxLayout(Main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.MainWindow = QWidget(Main)
        self.MainWindow.setObjectName(u"MainWindow")
        self.MainWindow.setMinimumSize(QSize(1106, 782))
        self.MainWindow.setAutoFillBackground(False)
        self.Container_1 = QWidget(self.MainWindow)
        self.Container_1.setObjectName(u"Container_1")
        self.Container_1.setGeometry(QRect(10, 10, 351, 71))
        self.Container_1.setAutoFillBackground(True)
        self.Container_1.setStyleSheet(u"#Container{\n"
"background-color rgb(255, 255, 255);\n"
"}")
        self.pushButton = QPushButton(self.Container_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 10, 111, 51))
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        icon = QIcon()
        icon.addFile(u":/icons/icon/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(20, 20))
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(True)
        self.Container_2 = QWidget(self.MainWindow)
        self.Container_2.setObjectName(u"Container_2")
        self.Container_2.setGeometry(QRect(10, 90, 351, 331))
        self.Container_2.setAutoFillBackground(True)
        self.Container_2.setStyleSheet(u"#Container{\n"
"background-color rgb(255, 255, 255);\n"
"}")
        self.pushButton_2 = QPushButton(self.Container_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(110, 10, 111, 51))
        self.pushButton_2.setAutoFillBackground(True)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon/upload-cloud.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(20, 20))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setFlat(True)
        self.pushButton_3 = QPushButton(self.Container_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(110, 270, 111, 51))
        self.pushButton_3.setAutoFillBackground(True)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icon/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(20, 20))
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setFlat(True)

        self.verticalLayout.addWidget(self.MainWindow)


        self.retranslateUi(Main)

        self.pushButton.setDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_3.setDefault(False)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Main", u"HOME", None))
        self.pushButton_2.setText(QCoreApplication.translate("Main", u"PLC", None))
        self.pushButton_3.setText(QCoreApplication.translate("Main", u"HELP", None))
    # retranslateUi

