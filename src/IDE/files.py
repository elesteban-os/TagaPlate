class file:
    fileText = ""
    fileUrl = ""
    fileName = ""

    def __init__(self, fileUrl, fileName):
        self.fileUrl = fileUrl
        self.fileName = fileName

    def readFile(self):
        f = open(self.fileUrl, 'r')
        self.filetext = f.read()
        f.close()
    
    def writeFile(self, newText):
        f = open(self.fileUrl, 'w')
        f.seek(0)
        f.write(newText)
        f.truncate()
        f.close()

    def saveFileAs(self, text):
        f = open(self.fileUrl, 'w')
        f.write(text)
        f.close()
    
    def saveFile(self):
        f = open(self.fileUrl, 'w')
        f.close()

    def setFileUrl(self, url):
        self.fileUrl = url

    def getFileText(self):
        return self.filetext
    
    def getFileUrl(self):
        return self.fileUrl
