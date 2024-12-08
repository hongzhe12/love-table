# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QHeaderView, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_process = QAction(MainWindow)
        self.action_process.setObjectName(u"action_process")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.action_5 = QAction(MainWindow)
        self.action_5.setObjectName(u"action_5")
        self.action_6 = QAction(MainWindow)
        self.action_6.setObjectName(u"action_6")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(111, 19))
        self.checkBox.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setMinimumSize(QSize(111, 19))

        self.horizontalLayout.addWidget(self.checkBox_2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu_2.addAction(self.action_process)
        self.menu_3.addAction(self.action_3)
        self.menu_3.addAction(self.action_4)
        self.menu_3.addAction(self.action_5)
        self.menu_3.addAction(self.action_6)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7231\u8868\u683c", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u6587\u4ef6", None))
        self.action_process.setText(QCoreApplication.translate("MainWindow", u"\u8f7d\u5165\u63d2\u4ef6", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u5165\u95e8\u6559\u7a0b", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u63d2\u4ef6\u4e2d\u5fc3", None))
        self.action_5.setText(QCoreApplication.translate("MainWindow", u"\u4ea4\u6d41\u7fa4", None))
        self.action_6.setText(QCoreApplication.translate("MainWindow", u"\u6700\u65b0\u8f6f\u4ef6\u4e0b\u8f7d", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u9010\u5355\u5143\u683c\u5904\u7406", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u6b21\u6027\u5904\u7406", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e\u8868\u683c", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5de5\u5177", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u6863\u4e0e\u5e2e\u52a9", None))
    # retranslateUi

