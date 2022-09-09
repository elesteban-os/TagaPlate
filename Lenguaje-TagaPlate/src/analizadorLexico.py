import ply.lex as lex
import re
import codecs
import os
import sys

tokens = ['ID', 'COMMENT', 'PPROC', 'PROC', 'LPARENT', 'RPARENT', 'CALL', 'SEMMICOLOM', 'NEW', 'COMMA', 
        'DATATYPE', 'VALUE', 'VALUES', 'ALTER', 'OP', 'ALTERB', 'MOVERIGHT', 'MOVELEFT', 'HAMMER', 'DIRECTION', 
        'STOP', 'LOGICOP', 'ISTRUE', 'REPEAT', 'UNTIL', 'WHILE', 'CASEWHEN', 'THEN', 'ELSE', 'CASE', 'WHEN', 'PRINTVALUES']


def t_PPROC(t):
    r'@Principal'
    return t
    
def t_ID(t):
    r'@[\w#]{3,10}'    
    return t

def t_COMMENT(t):
    r'--.*'
    return t

def t_PROC(t):
    r'Proc'
    return t

def t_LPARENT(t):
    r'\('
    return t

def t_RPARENT(t):
    r'\)'
    return t

def t_CALL(t):
    r'CALL'
    return t

def t_SEMMICOLOM(t):
    r';'
    return t

def t_NEW(t):
    r'New'
    return t

def t_COMMA(t):
    r','
    return t

def t_DATATYPE(t):
    r'(Bool|Num|String)'
    return t

def t_VALUE(t):
    r'(True|False|\d+|".+")'
    return t

def t_VALUES(t):
    r'Values'
    return t

def t_ALTERB(t):
    r'AlterB'
    return t

def t_ALTER(t):
    r'Alter'
    return t

def t_OP(t):
    r'(ADD|SUB|MUL|DIV)'
    return t
   
def t_MOVERIGHT(t):
    r'MoveRight'
    return t
    
def t_MOVELEFT(t):
    r'MoveLeft'
    return t
    
def t_HAMMER(t):
    r'Hammer'
    return t
   
def t_STOP(t):
    r'Stop'
    return t
    
def t_LOGICOP(t):
    r'(>|<|==|<>|<=|>=)'
    return t
    
def t_ISTRUE(t):
    r'IsTrue'
    return t
    
def t_REPEAT(t):
    r'Repeat'
    return t
    
def t_UNTIL(t):
    r'Until'
    return t
    
def t_WHILE(t):
    r'While'
    return t
    
def t_CASEWHEN(t):
    r'CaseWhen'
    return t
    
def t_THEN(t):
    r'Then'
    return t
    
def t_ELSE(t):
    r'Else'
    return t
    
def t_CASE(t):
    r'Case'
    return t
    
def t_WHEN(t):
    r'When'
    return t
    
def t_PRINTVALUES(t):
    r'PrintValues'
    return t

def t_DIRECTION(t):
    r'(N|S|E|O)'
    return t

def t_error(t):
    print("Caracter ilegal '%s'" %t.value[0])
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_SPACE(t):
    r'\s'
    pass

directorio = '/Users/vmartinezandres/Desktop/Lenguaje-TagaPlate/'
archivo = 'prueba.tagaplate' #buscarFicheros(directorio)
test = directorio + archivo
fp = codecs.open(test, "r", "utf-8")
cadena = fp.read()
fp.close()

analizador = lex.lex()

analizador.input(cadena)

while True:
    tok = analizador.token()
    if not tok : break
    print(tok)
