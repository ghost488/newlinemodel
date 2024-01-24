# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modelplus.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QCalendarWidget,
    QComboBox,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
    QMessageBox,
)

from firebase import addModel
from datetime import datetime
import os


class Ui_ModelPlus(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(502, 457)

        # 확인 버튼 관련
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName("submitButton")
        self.pushButton.setGeometry(QRect(150, 380, 75, 24))
        self.pushButton.clicked.connect(self.getSubmit)

        # 취소 버튼 관련
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName("cancelButton")
        self.pushButton_2.setGeometry(QRect(260, 380, 75, 24))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setGeometry(QRect(250, 100, 186, 214))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")

        self.verticalLayout_5.addWidget(self.label_5)

        self.calendarWidget = QCalendarWidget(self.layoutWidget)
        self.calendarWidget.setObjectName("opDate")

        self.verticalLayout_5.addWidget(self.calendarWidget)

        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(70, 90, 137, 232))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName("label")

        self.verticalLayout.addWidget(self.label)

        self.nameValue = QLineEdit(self.layoutWidget1)
        self.nameValue.setObjectName("nameValue")

        self.verticalLayout.addWidget(self.nameValue)

        self.verticalLayout_6.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.numberValue = QLineEdit(self.layoutWidget1)
        self.numberValue.setObjectName("numberValue")

        self.verticalLayout_2.addWidget(self.numberValue)

        self.verticalLayout_6.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.councilValue = QLineEdit(self.layoutWidget1)
        self.councilValue.setObjectName("councilValue")

        self.verticalLayout_3.addWidget(self.councilValue)

        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")

        self.verticalLayout_4.addWidget(self.label_4, 0, Qt.AlignLeft)

        self.operatorValue = QLineEdit(self.layoutWidget1)
        self.operatorValue.setObjectName("operatorValue")

        self.verticalLayout_4.addWidget(
            self.operatorValue, 0, Qt.AlignHCenter | Qt.AlignTop
        )

        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.opCase = QComboBox(self.layoutWidget1)
        self.opCase.addItem("복합수술 케이스")
        self.opCase.addItem("")
        self.opCase.addItem("")
        self.opCase.addItem("")
        self.opCase.addItem("")
        self.opCase.addItem("")
        self.opCase.addItem("")
        self.opCase.addItem("")
        self.opCase.addItem("")
        self.opCase.addItem("")
        self.opCase.addItem("")
        self.opCase.setObjectName("opCase")
        self.opCase.setMinimumContentsLength(0)

        self.verticalLayout_6.addWidget(self.opCase)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(
            QCoreApplication.translate(
                "Form", "\ubaa8\ub378 \ucd94\uac00\ud558\uae30", None
            )
        )
        self.pushButton.setText(
            QCoreApplication.translate("Form", "\ucd94\uac00", None)
        )
        self.pushButton_2.setText(
            QCoreApplication.translate("Form", "\ucde8\uc18c", None)
        )
        self.label_5.setText(QCoreApplication.translate("Form", "OP\ub0a0\uc9dc", None))
        self.label.setText(QCoreApplication.translate("Form", "\uc774\ub984", None))
        self.label_2.setText(
            QCoreApplication.translate("Form", "\uc804\ud654\ubc88\ud638", None)
        )
        self.label_3.setText(
            QCoreApplication.translate("Form", "\uc0c1\ub2f4\ud300\uc7a5", None)
        )
        self.label_4.setText(
            QCoreApplication.translate("Form", "\uc9d1\ub3c4\uc758", None)
        )
        self.opCase.setItemText(
            0,
            QCoreApplication.translate(
                "Form", "\ubcf5\ud569\uc218\uc220 \ucf00\uc774\uc2a4", None
            ),
        )
        self.opCase.setItemText(
            1, QCoreApplication.translate("Form", "\ub208 \uc131\ud615", None)
        )
        self.opCase.setItemText(
            2, QCoreApplication.translate("Form", "\ucf54 \uc131\ud615", None)
        )
        self.opCase.setItemText(
            3, QCoreApplication.translate("Form", "\uc548\uba74\uc724\uacfd", None)
        )
        self.opCase.setItemText(
            4, QCoreApplication.translate("Form", "\uc9c0\ubc29\uc774\uc2dd", None)
        )
        self.opCase.setItemText(
            5, QCoreApplication.translate("Form", "\uac00\uc2b4 \uc131\ud615", None)
        )
        self.opCase.setItemText(
            6,
            QCoreApplication.translate("Form", "\uc785\uaf2c\ub9ac \uc131\ud615", None),
        )
        self.opCase.setItemText(
            7,
            QCoreApplication.translate("Form", "\ubcf4\uc870\uac1c \uc131\ud615", None),
        )
        self.opCase.setItemText(
            8,
            QCoreApplication.translate(
                "Form", "\ud398\uc774\uc2a4 \ub9ac\ud504\ud305", None
            ),
        )
        self.opCase.setItemText(
            9,
            QCoreApplication.translate(
                "Form", "\uc544\ud050 \ub9ac\ud504\ud2b8, \uc2ec\ubd80\ubcfc", None
            ),
        )
        self.opCase.setItemText(
            10, QCoreApplication.translate("Form", "\uc5ec\uc720\uc99d", None)
        )

    # retranslateUi

    # 모델 폴더들을 만드는 함수
    def addFolder(self, name, number, operation):
        try:
            basePath = "C:/test/"

            def make_directory(*paths):
                for path in paths:
                    os.makedirs(path, exist_ok=True)

            # 임상 사진 폴더
            path = f"{basePath}{name}({number})/{name}(전){operation}"
            path2 = f"{basePath}{name}({number})/{name}(후){operation}"

            # 셀프 카메라 폴더
            cameraPath = f"{basePath}{name}({number})/셀프 카메라/수술 전"
            cameraPath2 = f"{basePath}{name}({number})/셀프 카메라/회복기간"
            cameraPath3 = f"{basePath}{name}({number})/셀프 카메라/수술 후"

            make_directory(path, path2, cameraPath, cameraPath2, cameraPath3)

        except FileExistsError:
            print("폴더가 이미 존재합니다.")
        except Exception as e:
            print(f"오류가 발생: {e}")

    # 클릭시 제출 함수
    def getSubmit(self):
        nameValue = self.nameValue.text()
        numberValue = self.numberValue.text()
        councilValue = self.councilValue.text()
        operatorValue = self.operatorValue.text()
        operationValue = self.opCase.currentText()
        opDate = self.calendarWidget.selectedDate()
        opDate_datetime = datetime(opDate.year(), opDate.month(), opDate.day())

        data = {
            "name": nameValue,
            "number": numberValue,
            "council": councilValue,
            "operator": operatorValue,
            "operation": operationValue,
            "opDate": opDate_datetime,
        }

        if all(
            [
                nameValue,
                numberValue,
                councilValue,
                operatorValue,
                operationValue,
                opDate,
            ]
        ):
            # addModel(data)
            self.addFolder(nameValue, numberValue, operationValue)
            self.windowClose()

    def windowClose(self):
        app = QApplication.instance()
        app.activeWindow().close()
