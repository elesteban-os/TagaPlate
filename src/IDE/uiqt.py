from distutils.file_util import write_file
from msilib.schema import Directory
import sys
from files import file
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QListWidgetItem 
from LexYacc.analyzer import LexYacc

class ui(QMainWindow):
    file = None
    analyzer = LexYacc()

    def print(self, MainWindow):
        print("Hello World")

    def saveEnabled(self):
        self.actionSave_File.setEnabled(True)
        self.actionSave_as.setEnabled(True)
        self.runButton.setEnabled(True)
        self.infoButton.setEnabled(True)
        self.compileButton.setEnabled(True)
    
    def createNewFile(self):
        directory = QFileDialog.getSaveFileName(self, "New file", "c:\\", "tagaplate Files (*.tagaplate)")[0]
        nameFile = directory.split(sep = "/")[-1]
        if directory == "":
            QMessageBox.critical(self, "Error", "Please enter a directory", QMessageBox.Ok)
        else:
            newfile = file(directory, nameFile)
            newfile.saveFile()
            self.file = newfile
            self.plainTextseEdit.setPlainText("")
            self.plainTextseEdit.setEnabled(True)
            self.saveEnabled()
            print("creating new file...")

    def openFile(self):
        try:
            directory = QFileDialog.getOpenFileName(self, "Open File", "c:\\", "tagaplate Files (*.tagaplate)")[0]
            nameFile = directory.split(sep = "/")[-1]
            nameFileAux = nameFile.split(sep = ".")[0]
            openFile = file(directory, nameFileAux)
            openFile.readFile()
            text = openFile.getFileText()
            self.file = openFile
            self.plainTextseEdit.setPlainText(text)
            self.plainTextseEdit.setEnabled(True)
            self.saveEnabled()
            print(directory, nameFileAux)
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "Please choose a file", QMessageBox.Ok)

    def writeFile(self):
        text = self.plainTextseEdit.toPlainText()
        self.file.writeFile(text)
        print("saving file...")

    def saveFileAs(self):
        directory = QFileDialog.getSaveFileName(self, "New file", "c:\\", "tagaplate Files (*.tagaplate)")[0] + ".tagaplate"
        nameFile = directory.split(sep = "/")[-1]
        if directory == ".taga":
            QMessageBox.critical(self, "Error", "Please enter a directory", QMessageBox.Ok)
        else:
            newfile = file(directory, nameFile)
            self.file = newfile
            text = self.plainTextseEdit.toPlainText()
            self.file.saveFileAs(text)


    def mousePressEvent(self, event):
        print("clicked mouse")

    def cursorText(self):
        cursor = self.plainTextseEdit.textCursor()
        line = cursor.blockNumber() + 1
        column = cursor.columnNumber() + 1
        self.label.setText("Line: " + str(line) + ", Column: " + str(column))

    def altTabVisible(self):
        if self.tabWidget.isVisible():
            self.tabWidget.setVisible(False)
        else:
            self.tabWidget.setVisible(True)

    def compile(self):
        self.problemsList.clear()
        self.writeFile()
        self.file.readFile()
        text = str(self.plainTextseEdit.toPlainText())
    
        self.analyzer.doYacc(text)
        errorList = self.analyzer.getErrorsList()
        if len(errorList) > 0:
            for error in errorList:
                self.appendToErrorList(error)
                print(error)
        else:
            print("compile")


    def appendToErrorList(self, error):
        item = QListWidgetItem(QtGui.QIcon("src/IDE/warning.png"), error) 
        self.problemsList.addItem(item)

    def __init__(self):
        super().__init__()
        uic.loadUi("src/IDE/window.ui", self)
        self.tabWidget.setVisible(False)

        self.infoButton.clicked.connect(self.altTabVisible)
        self.actionNew_File.triggered.connect(self.createNewFile)
        self.actionSave_File.triggered.connect(self.writeFile)
        self.actionOpen_File.triggered.connect(self.openFile)
        self.actionSave_as.triggered.connect(self.saveFileAs)
        self.plainTextseEdit.cursorPositionChanged.connect(self.cursorText)
        self.compileButton.clicked.connect(self.compile)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui1 = ui()
    ui1.show()
    sys.exit(app.exec_())
