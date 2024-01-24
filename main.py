import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from mainwindow_ui import Ui_MainWindow
from modelplus_ui import Ui_ModelPlus
from firebase import getModels


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 시작시 모델 데이터를 백엔드에서 가지고 옴
        allModels = getModels()

        self.ui = Ui_MainWindow()
        # UI를 그린다
        self.ui.setupUi(self)

        # 리스트위젯에 모델 리스트를 넣는 함수
        self.ui.paintModels(allModels)

        self.ui.pushButton.clicked.connect(self.openModelPlusWindow)

        self.model_plus_window = None

    def openModelPlusWindow(self):
        # 이미 창이 열려있는 경우에는 보이도록 하고, 아닌 경우에는 새로 생성
        if not self.model_plus_window or not self.model_plus_window.isVisible():
            self.model_plus_window = ModelPlusWindow()

        self.model_plus_window.show()


class ModelPlusWindow(QMainWindow):
    def __init__(self):
        super(ModelPlusWindow, self).__init__()
        self.ui = Ui_ModelPlus()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
