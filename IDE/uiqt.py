import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class ejemplo_GUI(QMainWindow):

    def print(self, MainWindow):
        print("Hello World")

    def altTabVisible(self):
        if self.tabWidget.isVisible():
            self.tabWidget.setVisible(False)
        else:
            self.tabWidget.setVisible(True)

    def __init__(self):
        super().__init__()
        uic.loadUi("window.ui", self)
        self.tabWidget.setVisible(False)

        self.infoButton.clicked.connect(self.altTabVisible)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = ejemplo_GUI()
    ui.show()
    sys.exit(app.exec_())
