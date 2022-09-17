from msilib.schema import Directory
import sys
from files import file
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox

class ui(QMainWindow):
    file = None

    def print(self, MainWindow):
        print("Hello World")
    
    def createNewFile(self):
        directory = QFileDialog.getSaveFileName(self, "New file", "c:\\", "Taga Files (*.taga)")[0] + ".taga"
        nameFile = directory.split(sep = "/")[-1]
        if directory == ".taga":
            QMessageBox.critical(self, "Error", "Please enter a directory", QMessageBox.Ok)
        else:
            newfile = file(directory, nameFile)
            newfile.saveFile()
            self.file = newfile
            self.plainTextseEdit.setPlainText("")
            self.plainTextseEdit.setEnabled(True)
            print("creating new file...")

    def openFile(self):
        try:
            directory = QFileDialog.getOpenFileName(self, "Open File", "c:\\", "Taga Files (*.taga)")[0]
            nameFile = directory.split(sep = "/")[-1]
            nameFileAux = nameFile.split(sep = ".")[0]
            openFile = file(directory, nameFileAux)
            openFile.readFile()
            text = openFile.getFileText()
            self.file = openFile
            self.plainTextseEdit.setPlainText(text)
            self.plainTextseEdit.setEnabled(True)
            print(directory, nameFileAux)
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "Please choose a file", QMessageBox.Ok)

    def writeFile(self):
        text = self.plainTextseEdit.toPlainText()
        print(text)
        self.file.writeFile(text)
        print("saving file...")

    def mousePressEvent(self, event):
        print("clicked mouse")

    def altTabVisible(self):
        if self.tabWidget.isVisible():
            self.tabWidget.setVisible(False)
        else:
            self.tabWidget.setVisible(True)

    def __init__(self):
        super().__init__()
        uic.loadUi("IDE/window.ui", self)
        self.tabWidget.setVisible(False)

        self.infoButton.clicked.connect(self.altTabVisible)
        self.actionNew_File.triggered.connect(self.createNewFile)
        self.actionSave_File.triggered.connect(self.writeFile)
        self.actionOpen_File.triggered.connect(self.openFile)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui1 = ui()
    ui1.show()
    sys.exit(app.exec_())
