import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from mainwindow_ui import Ui_MainWindow
from modelplus_ui import Ui_ModelPlus


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
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
    