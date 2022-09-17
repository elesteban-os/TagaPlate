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

    def saveFile(self, text):
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

'''prueba = file("IDE/ex.txt", "ex.txt")
prueba.readFile()
print(prueba.getFileText())'''

prueba3 = file("IDE/ex2.txt", "ex2.txt")
prueba3.writeFile("""Texto texto    texto                     jdsfijsidfjisajfoisdjfiaiofjsado

                    texto xdd dsfjsoadfkadfkosdafkosdiafk """)
