# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setGeometry(QRect(410, 50, 251, 321))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.listWidget_2 = QListWidget(self.layoutWidget)
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_2.setContextMenuPolicy(Qt.ActionsContextMenu)

        self.verticalLayout_2.addWidget(self.listWidget_2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QRect(310, 450, 131, 31))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QRect(310, 500, 131, 31))
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(130, 50, 251, 321))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName("label")

        self.verticalLayout.addWidget(self.label)

        self.listWidget = QListWidget(self.layoutWidget1)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setContextMenuPolicy(Qt.ActionsContextMenu)

        self.verticalLayout.addWidget(self.listWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "MainWindow", "\uc5f0\ub77d \ubabb\ud55c \ubaa8\ub378", None
            )
        )
        self.pushButton.setText(
            QCoreApplication.translate(
                "MainWindow", "\uc0c8 \ubaa8\ub378 \ucd94\uac00", None
            )
        )
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", "\ub2eb\uae30", None)
        )
        self.label.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\uc624\ub298 \uc5f0\ub77d\ud574\uc57c \ud560 \ubaa8\ub378",
                None,
            )
        )

    # retranslateUi

    def paintModels(self, models):
        for model in models:
            modelName = model.name
            modelnumber = model.number
            modelCouncil = model.council
            modelOperation = model.operation
            modelOperator = model.operator
            modelOpDate = model.opDate

            item_text = f"{modelName}({modelnumber})"
            item = QListWidgetItem(item_text)
            self.listWidget.addItem(item)
