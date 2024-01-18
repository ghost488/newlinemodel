# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modelplus.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_ModelPlus(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(502, 457)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 380, 75, 24))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(260, 380, 75, 24))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(250, 100, 186, 214))
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_5.addWidget(self.label_5)

        self.calendarWidget = QCalendarWidget(self.widget)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.verticalLayout_5.addWidget(self.calendarWidget)

        self.widget1 = QWidget(Form)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(70, 90, 137, 232))
        self.verticalLayout_6 = QVBoxLayout(self.widget1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget1)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.widget1)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)


        self.verticalLayout_6.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.widget1)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.widget1)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_3.addWidget(self.lineEdit_3)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4, 0, Qt.AlignLeft)

        self.lineEdit_4 = QLineEdit(self.widget1)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_4.addWidget(self.lineEdit_4, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.comboBox = QComboBox(self.widget1)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_6.addWidget(self.comboBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\ucd94\uac00", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\ucde8\uc18c", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"OP\ub0a0\uc9dc", None))
        self.label.setText(QCoreApplication.translate("Form", u"\uc774\ub984", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\uc804\ud654\ubc88\ud638", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\uc0c1\ub2f4\ud300\uc7a5", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\uc9d1\ub3c4\uc758", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\ubcf5\ud569\uc218\uc220 \ucf00\uc774\uc2a4", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"\ub208 \uc131\ud615", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"\ucf54 \uc131\ud615", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"\uc548\uba74\uc724\uacfd", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Form", u"\uc9c0\ubc29\uc774\uc2dd", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Form", u"\uac00\uc2b4 \uc131\ud615", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Form", u"\uc785\uaf2c\ub9ac \uc131\ud615", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Form", u"\ubcf4\uc870\uac1c \uc131\ud615", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("Form", u"\ud398\uc774\uc2a4 \ub9ac\ud504\ud305", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("Form", u"\uc544\ud050 \ub9ac\ud504\ud2b8, \uc2ec\ubd80\ubcfc", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("Form", u"\uc5ec\uc720\uc99d", None))

    # retranslateUi

