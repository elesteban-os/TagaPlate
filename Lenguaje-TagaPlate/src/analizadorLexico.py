import ply.lex as lex
import re
import codecs
import os
import sys

tokens = ['PPROC', 'ID', 'PROC', 'CALL', 'NEW', 'NUMDT', 'BOOLDT', 'VALUES', 'ALTERB', 'ALTER',
        'MOVERIGHT', 'MOVELEFT', 'HAMMER', 'STOP', 'ISTRUE', 'REPEAT', 'BREAK', 'UNTIL', 'WHILE', 'CASEWHEN',
        'THEN', 'ELSE', 'CASE', 'WHEN', 'PRINTVALUES', 'NUMVALUE', 'BOOLVALUE', 'TEXT', 'ADDOP','SUBOP',
        'MULOP', 'DIVOP', 'NORTH', 'SOUTH', 'EAST', 'WEST', 'EEOP', 'NEOP', 'GETOP','LETOP',
        'GTOP', 'LTOP', 'COMMENT', 'LPAR', 'RPAR', 'SEMMICOLOM', 'COMMA']


def t_PPROC(t):
    r'@Principal'
    return t

t_ID = r'@[\w#]{3,10}'
t_PROC = r'Proc'
t_CALL = r'CALL'
t_NEW = r'New' 
t_NUMDT = r'Num'
t_BOOLDT = r'Bool'
t_VALUES = r'Values'
t_ALTERB = r'AlterB'
t_ALTER = r'Alter'

t_MOVERIGHT = r'MoveRight'
t_MOVELEFT = r'MoveLeft'
t_HAMMER = r'Hammer'
t_STOP = r'Stop'
t_ISTRUE = r'IsTrue'
t_REPEAT = r'Repeat'
t_BREAK = r'Break'
t_UNTIL = r'Until'
t_WHILE = r'While'
t_CASEWHEN = r'CaseWhen'

t_THEN = r'Then'
t_ELSE = r'Else'
t_CASE = r'Case'
t_WHEN = r'When'
t_PRINTVALUES = r'PrintValues'
t_NUMVALUE = r'\d+'
t_BOOLVALUE = r'True|False'
t_TEXT = r'".+"'
t_ADDOP = r'ADD'
t_SUBOP = r'SUB'

t_MULOP = r'MUL'
t_DIVOP = r'DIV'
t_NORTH = r'N'
t_SOUTH = r'S'
t_EAST = r'E'
t_WEST = r'O'
t_EEOP = r'=='
t_NEOP = r'<>'
t_GETOP = r'>='
t_LETOP = r'<='

t_GTOP = r'>'
t_LTOP = r'<'
t_LPAR = r'\('
t_RPAR = r'\)'
t_SEMMICOLOM = r';'
t_COMMA = r','

def t_COMMENT(t):
    r'--.*'
    if (t.lexer.lineno == 1):
        return t
    else:
        pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_SPACE(t):
    r'\s'
    pass   

def t_error(t):
    print("Caracter ilegal '%s'" %t.value[0])
    t.lexer.skip(1)

analizador = lex.lex()

