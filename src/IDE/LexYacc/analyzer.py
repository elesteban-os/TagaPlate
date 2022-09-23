from functools import update_wrapper
from LexYacc.lexer1 import doLex, getLexErrorsList, lexer
from LexYacc.yacc import doYacc, getErrorsList1, updateLex
import ply.lex as lex

class LexYacc:
    lexErrors = []
    yaccErrors = []

    def __init__(self):
        print("LexYacc")
        self.updateLex()
        
    def doLex(self, text):
        self.lexErrors.clear()
        doLex(text)

    def doYacc(self, text):
        self.yaccErrors.clear()
        doYacc(text)

    def updateLex(self):
        global lexer
        updateLex(lexer)

    def getErrorsList(self):
        return getErrorsList1()
        
