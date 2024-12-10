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
    QHeaderView, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(797, 567)
        icon = QIcon()
        icon.addFile(u":/icons/images/logo.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
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
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(180, 50))
        font = QFont()
        font.setFamilies([u"\u65b9\u6b63\u7c97\u9ed1\u5b8b\u7b80\u4f53"])
        font.setPointSize(16)
        font.setBold(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"    border: none;  /* \u53bb\u6389\u8fb9\u6846 */\n"
"    background: transparent;  /* \u80cc\u666f\u900f\u660e */\n"
"	background-position: center;  /* \u56fe\u6807\u5c45\u4e2d\u663e\u793a */\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/\u8868\u683c.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButton_3, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setTabletTracking(False)
        self.stackedWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.stackedWidget.setStyleSheet(u"")
        self.stackedWidgetPage1 = QWidget()
        self.stackedWidgetPage1.setObjectName(u"stackedWidgetPage1")
        self.gridLayout_2 = QGridLayout(self.stackedWidgetPage1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(self.stackedWidgetPage1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QScrollBar:vertical\n"
"{\n"
"    width:8px;\n"
"    background:rgb(0,0,0,0%);\n"
"    margin:0px,0px,0px,0px;\n"
"    padding-top:12px;   /*\u4e0a\u9884\u7559\u4f4d\u7f6e*/\n"
"    padding-bottom:12px;    /*\u4e0b\u9884\u7559\u4f4d\u7f6e*/\n"
"}\n"
" \n"
"/*\u6eda\u52a8\u6761\u4e2d\u6ed1\u5757\u7684\u6837\u5f0f*/\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    width:8px;\n"
"    background:rgb(0,0,0,25%);\n"
"    border-radius:4px;\n"
"    min-height:20px;\n"
"}\n"
" \n"
"/*\u9f20\u6807\u89e6\u53ca\u6ed1\u5757\u6837\u5f0f*/\n"
"QScrollBar::handle:vertical:hover\n"
"{\n"
"    width:9px;\n"
"    background:rgb(0,0,0,50%);\n"
"    border-radius:4px;\n"
"    min-height:20;\n"
"}\n"
" \n"
"/*\u8bbe\u7f6e\u4e0b\u7bad\u5934*/\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    height:12px;\n"
"    width:10px;\n"
"    border-image:url(:/KeyManager/images/icon_pull-down.png);\n"
"    subcontrol-position:bottom;\n"
"}\n"
" \n"
"/*\u8bbe\u7f6e\u4e0a\u7bad\u5934*/\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    height:12px;\n"
""
                        "    width:10px;\n"
"    border-image:url(:/KeyManager/images/icon_pull-up.png);\n"
"    subcontrol-position:top;\n"
"}\n"
" \n"
"/*\u8bbe\u7f6e\u4e0b\u7bad\u5934:\u60ac\u6d6e\u72b6\u6001*/\n"
"QScrollBar::add-line:vertical:hover\n"
"{\n"
"    height:12px;\n"
"    width:10px;\n"
"    border-image:url(:/KeyManager/images/icon_pull-down2.png);\n"
"    subcontrol-position:bottom;\n"
"}\n"
" \n"
"/*\u8bbe\u7f6e\u4e0a\u7bad\u5934\uff1a\u60ac\u6d6e\u72b6\u6001*/\n"
"QScrollBar::sub-line:vertical:hover\n"
"{\n"
"    height:12px;\n"
"    width:10px;\n"
"    border-image:url(:/KeyManager/images/icon_pull-up2.png);\n"
"    subcontrol-position:top;\n"
"}\n"
" \n"
"/*\u5f53\u6eda\u52a8\u6761\u6eda\u52a8\u7684\u65f6\u5019\uff0c\u4e0a\u9762\u7684\u90e8\u5206\u548c\u4e0b\u9762\u7684\u90e8\u5206*/\n"
"QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical\n"
"{\n"
"    background:rgb(0,0,0,10%);\n"
"    border-radius:4px;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    height: 8px;  /* \u8bbe\u7f6e\u6eda\u52a8\u6761\u9ad8"
                        "\u5ea6 */\n"
"    background: rgb(0, 0, 0, 0%);  /* \u80cc\u666f\u900f\u660e */\n"
"    margin: 0px;  /* \u5916\u8fb9\u8ddd */\n"
"    padding-left: 12px;  /* \u5de6\u9884\u7559\u4f4d\u7f6e */\n"
"    padding-right: 12px;  /* \u53f3\u9884\u7559\u4f4d\u7f6e */\n"
"}\n"
"\n"
"/* \u6eda\u52a8\u6761\u4e2d\u6ed1\u5757\u7684\u6837\u5f0f */\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    height: 8px;  /* \u8bbe\u7f6e\u6ed1\u5757\u9ad8\u5ea6 */\n"
"    background: rgb(0, 0, 0, 25%);  /* \u6ed1\u5757\u80cc\u666f\u989c\u8272\u53ca\u900f\u660e\u5ea6 */\n"
"    border-radius: 4px;\n"
"    min-width: 20px;  /* \u6700\u5c0f\u5bbd\u5ea6 */\n"
"}\n"
"\n"
"/* \u9f20\u6807\u89e6\u53ca\u6ed1\u5757\u6837\u5f0f */\n"
"QScrollBar::handle:horizontal:hover\n"
"{\n"
"    height: 9px;  /* \u9f20\u6807\u60ac\u505c\u65f6\u6ed1\u5757\u9ad8\u5ea6\u53d8\u5316 */\n"
"    background: rgb(0, 0, 0, 50%);\n"
"    border-radius: 4px;\n"
"    min-width: 20px;\n"
"}\n"
"\n"
"/* \u8bbe\u7f6e\u53f3\u7bad\u5934 */\n"
"QScrollBar::add-line:horizontal\n"
""
                        "{\n"
"    width: 12px;\n"
"    height: 10px;\n"
"    border-image: url(:/KeyManager/images/icon_pull-right.png);  /* \u5bf9\u5e94\u53f3\u7bad\u5934\u56fe\u7247\uff0c\u9700\u786e\u4fdd\u8d44\u6e90\u8def\u5f84\u6b63\u786e */\n"
"    subcontrol-position: right;\n"
"}\n"
"\n"
"/* \u8bbe\u7f6e\u5de6\u7bad\u5934 */\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    width: 12px;\n"
"    height: 10px;\n"
"    border-image: url(:/KeyManager/images/icon_pull-left.png);  /* \u5bf9\u5e94\u5de6\u7bad\u5934\u56fe\u7247 */\n"
"    subcontrol-position: left;\n"
"}\n"
"\n"
"/* \u8bbe\u7f6e\u53f3\u7bad\u5934:\u60ac\u6d6e\u72b6\u6001 */\n"
"QScrollBar::add-line:horizontal:hover\n"
"{\n"
"    width: 12px;\n"
"    height: 10px;\n"
"    border-image: url(:/KeyManager/images/icon_pull-right2.png);\n"
"    subcontrol-position: right;\n"
"}\n"
"\n"
"/* \u8bbe\u7f6e\u5de6\u7bad\u5934\uff1a\u60ac\u6d6e\u72b6\u6001 */\n"
"QScrollBar::sub-line:horizontal:hover\n"
"{\n"
"    width: 12px;\n"
"    height: 10px;\n"
"    border-image: url(:/Key"
                        "Manager/images/icon_pull-left2.png);\n"
"    subcontrol-position: left;\n"
"}\n"
"\n"
"/* \u5f53\u6eda\u52a8\u6761\u6eda\u52a8\u7684\u65f6\u5019\uff0c\u5de6\u8fb9\u7684\u90e8\u5206\u548c\u53f3\u8fb9\u7684\u90e8\u5206 */\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: rgb(0, 0, 0, 10%);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox = QCheckBox(self.stackedWidgetPage1)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(111, 50))
        self.checkBox.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.stackedWidgetPage1)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setMinimumSize(QSize(111, 50))

        self.horizontalLayout.addWidget(self.checkBox_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_2 = QPushButton(self.stackedWidgetPage1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(81, 51))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"   QPushButton {\n"
"       border-width: 0px;\n"
"       border-style: none;\n"
"       border-color: transparent;\n"
"	   border-radius:8px;\n"
"	   color: rgb(255, 255, 255);\n"
"	   background-color: rgb(65, 168, 99);\n"
"   }")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.stackedWidgetPage1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(81, 51))
        self.pushButton.setStyleSheet(u"   QPushButton {\n"
"       border-width: 0px;\n"
"       border-style: none;\n"
"       border-color: transparent;\n"
"	   border-radius:8px;\n"
"	   color: rgb(255, 255, 255);\n"
"	   background-color: rgb(65, 168, 99);\n"
"   }")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.stackedWidgetPage2 = QWidget()
        self.stackedWidgetPage2.setObjectName(u"stackedWidgetPage2")
        self.gridLayout_3 = QGridLayout(self.stackedWidgetPage2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.stackedWidgetPage2)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(10)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.stackedWidgetPage2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 30))

        self.gridLayout_3.addWidget(self.pushButton_7, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.stackedWidgetPage2)
        self.stackedWidgetPage3 = QWidget()
        self.stackedWidgetPage3.setObjectName(u"stackedWidgetPage3")
        self.gridLayout_4 = QGridLayout(self.stackedWidgetPage3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_2 = QLabel(self.stackedWidgetPage3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.stackedWidgetPage3)
        self.stackedWidgetPage4 = QWidget()
        self.stackedWidgetPage4.setObjectName(u"stackedWidgetPage4")
        self.gridLayout_5 = QGridLayout(self.stackedWidgetPage4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_3 = QLabel(self.stackedWidgetPage4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.stackedWidgetPage4)

        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 6, 1)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(180, 50))
        font3 = QFont()
        font3.setFamilies([u"\u65b9\u6b63\u7c97\u9ed1\u5b8b\u7b80\u4f53"])
        font3.setPointSize(16)
        self.pushButton_5.setFont(font3)
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"    border: none;  /* \u53bb\u6389\u8fb9\u6846 */\n"
"    background: transparent;  /* \u80cc\u666f\u900f\u660e */\n"
"	background-position: center;  /* \u56fe\u6807\u5c45\u4e2d\u663e\u793a */\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/\u63d2\u4ef6.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButton_5, 1, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(180, 50))
        self.pushButton_4.setFont(font3)
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"    border: none;  /* \u53bb\u6389\u8fb9\u6846 */\n"
"    background: transparent;  /* \u80cc\u666f\u900f\u660e */\n"
"	background-position: center;  /* \u56fe\u6807\u5c45\u4e2d\u663e\u793a */\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/\u7cfb\u7edf.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(180, 50))
        self.pushButton_6.setFont(font3)
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"    border: none;  /* \u53bb\u6389\u8fb9\u6846 */\n"
"    background: transparent;  /* \u80cc\u666f\u900f\u660e */\n"
"	background-position: center;  /* \u56fe\u6807\u5c45\u4e2d\u663e\u793a */\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/\u8bbe\u7f6e.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButton_6, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 269, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 797, 33))
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

        self.stackedWidget.setCurrentIndex(0)


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
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u" \u8868\u683c", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u9010\u5355\u5143\u683c\u5904\u7406", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u6b21\u6027\u5904\u7406", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u529f\u80fd\u83dc\u5355", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e\u8868\u683c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236\u5b8c\u6574\u4fe1\u606f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5546\u5e97\u6b63\u5728\u5f00\u53d1\u4e2d...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u6b63\u5728\u5f00\u53d1\u4e2d...", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u" \u63d2\u4ef6", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u" \u7cfb\u7edf", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u" \u8bbe\u7f6e", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5de5\u5177", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u6863\u4e0e\u5e2e\u52a9", None))
    # retranslateUi

