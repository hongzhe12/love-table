# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'list.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(506, 488)
        self.pushButton_1 = QPushButton(Form)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(9, 9, 88, 88))
        self.pushButton_1.setMinimumSize(QSize(82, 82))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet(u"min-width : 80px; /* \u6700\u5c0f\u5bbd\u5ea6 */\n"
"min-height : 80px; /* \u6700\u5c0f\u9ad8\u5ea6 */\n"
"max-width : 200px; /* \u6700\u5927\u5bbd\u5ea6 */\n"
"max-height : 200px; /* \u6700\u5927\u9ad8\u5ea6 */\n"
"background-position: center;  /*\u5c45\u4e2d\u663e\u793a */\n"
"background->attachment:fixed;  /* \u56fa\u5b9a */\n"
"background-repeat: repeat-n; /* \u662f\u5426\u91cd\u590d repeat-y\u662f\u91cd\u590d*/\n"
"")
        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(80, 120, 361, 291))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5e38\u7528\u529f\u80fd", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"\u8f6c\u6362\u4e3a\u5927\u5199", None))
    # retranslateUi

