import ply.yacc as yacc
import os
import codecs
import re
from analizadorLexico import tokens
from sys import stdin

# precedence = (
#     ('left', 'LPAR', 'RPAR'),
# )

# program
def p_program(p):
    '''program : COMMENT outsideInstruction PPROC instructionBlock SEMMICOLOM outsideInstruction'''
    print("program")

# outsideInstruction
def p_outsideInstruction1(p):
    '''outsideInstruction : attribute SEMMICOLOM outsideInstruction'''
    print("outsideInstruction1")

def p_outsideInstruction2(p):
    '''outsideInstruction : function SEMMICOLOM outsideInstruction'''
    print("outsideInstruction2")

def p_outsideInstruction3(p):
    '''outsideInstruction : empty'''
    print("outsideInstruction3")

# instructionBlock
def p_instructionBlock(p):
    '''instructionBlock : LPAR insideInstruction RPAR'''
    print("instructionBlock")

# attribute
def p_attribute1(p):
    '''attribute : NEW ID COMMA LPAR datatype COMMA value RPAR'''
    print("attribute1")

def p_attribute2(p):
    '''attribute : NEW ID COMMA LPAR datatype COMMA alterFunction RPAR'''
    print("attribute2")

def p_attribute3(p):
    '''attribute : NEW ID COMMA LPAR datatype COMMA returnBoolFunction RPAR'''
    print("attribute3")

def p_attribute4(p):
    '''attribute : NEW ID COMMA LPAR datatype COMMA ID RPAR'''
    print("attribute4")

# function
def p_function1(p):
    '''function : PROC ID instructionBlock'''
    print("function1")

def p_function2(p):
    '''function : innerFunction'''
    print("function2")

# insideInstruction
def p_insideInstruction1(p):
    '''insideInstruction : attribute SEMMICOLOM insideInstruction'''
    print("insideInstruction1")

def p_insideInstruction2(p):
    '''insideInstruction : innerFunction SEMMICOLOM insideInstruction'''
    print("insideInstruction2")

def p_insideInstruction3(p):
    '''insideInstruction : empty'''
    print("insideInstruction3")
    
# datatype
def p_datatype1(p):
    '''datatype : NUMDT'''
    print("datatype1")

def p_datatype2(p):
    '''datatype : BOOLDT'''
    print("datatype2")

# value
def p_value1(p):
    '''value : NUMVALUE'''
    print("value1")

def p_value2(p):
    '''value : BOOLVALUE'''
    print("value2")

# innerFunction
def p_innerFunction1(p):
    '''innerFunction : languageFunction'''
    print("innerFunction1")

def p_innerFunction2(p):
    '''innerFunction : tagadaFunction'''
    print("innerFunction2")

# languageFunction
def p_languageFunction1(p):
    '''languageFunction : alterFunction'''
    print("languageFunction1")

def p_languageFunction2(p):
    '''languageFunction : returnBoolFunction'''
    print("languageFunction2")

def p_languageFunction3(p):
    '''languageFunction : voidFunction'''
    print("languageFunction3")

# tagadaFunction
def p_tagadaFunction1(p):
    '''tagadaFunction : MOVERIGHT'''
    print("tagadaFunction1")

def p_tagadaFunction2(p):
    '''tagadaFunction : MOVELEFT'''
    print("tagadaFunction2")

def p_tagadaFunction3(p):
    '''tagadaFunction : STOP'''
    print("tagadaFunction3")

def p_tagadaFunction4(p):
    '''tagadaFunction : hammerFunction'''
    print("tagadaFunction4")

# alterFunction
def p_alterFunction1(p):
    '''alterFunction : ALTER LPAR ID COMMA numericalOperator COMMA NUMVALUE RPAR'''
    print("alterFunction1")

def p_alterFunction2(p):
    '''alterFunction : ALTER LPAR ID COMMA numericalOperator COMMA ID RPAR'''
    print("alterFunction2")

# returnBoolFunction
def p_returnBoolFunction1(p):
    '''returnBoolFunction : alterbFunction'''
    print("returnBoolFunction1")

def p_returnBoolFunction2(p):
    '''returnBoolFunction : istrueFunction'''
    print("returnBoolFunction2")

def p_returnBoolFunction3(p):
    '''returnBoolFunction : numericalConditionFunction'''
    print("returnBoolFunction3")

# voidFunction
def p_voidFunction1(p):
    '''voidFunction : callFunction'''
    print("voidFunction1")

def p_voidFunction2(p):
    '''voidFunction : valuesFunction'''
    print("voidFunction2")

def p_voidFunction3(p):
    '''voidFunction : iterativeFunction'''
    print("voidFunction3")

def p_voidFunction4(p):
    '''voidFunction : printFunction'''
    print("voidFunction4")

# hammerFunction
def p_hammerFunction(p):
    '''hammerFunction : HAMMER LPAR direction RPAR'''
    print("hammerFunction")

# numericalOperator
def p_numericalOperator1(p):
    '''numericalOperator : ADDOP'''
    print("numericalOperator1")

def p_numericalOperator2(p):
    '''numericalOperator : SUBOP'''
    print("numericalOperator2")

def p_numericalOperator3(p):
    '''numericalOperator : MULOP'''
    print("numericalOperator3")

def p_numericalOperator4(p):
    '''numericalOperator : DIVOP'''
    print("numericalOperator4")

# alterbFunction
def p_alterbFunction(p):
    '''alterbFunction : ALTERB LPAR ID RPAR'''
    print("alterbFunction")

# istrueFunction
def p_istrueFunction1(p):
    '''istrueFunction : ISTRUE LPAR BOOLVALUE RPAR'''
    print("istrueFunction1")

def p_istrueFunction2(p):
    '''istrueFunction : ISTRUE LPAR returnBoolFunction RPAR'''
    print("istrueFunction2")

def p_istrueFunction3(p):
    '''istrueFunction : ISTRUE LPAR ID RPAR'''
    print("istrueFunction3")

# numericalConditionFunction
def p_numericalConditionFunction1(p):
    '''numericalConditionFunction : NUMVALUE logicOperator NUMVALUE'''
    print("numericalConditionFunction1")

def p_numericalConditionFunction2(p):
    '''numericalConditionFunction : NUMVALUE logicOperator alterFunction'''
    print("numericalConditionFunction2")

def p_numericalConditionFunction3(p):
    '''numericalConditionFunction : NUMVALUE logicOperator ID'''
    print("numericalConditionFunction3")

def p_numericalConditionFunction4(p):
    '''numericalConditionFunction : alterFunction logicOperator NUMVALUE'''
    print("numericalConditionFunction4")

def p_numericalConditionFunction5(p):
    '''numericalConditionFunction : alterFunction logicOperator alterFunction'''
    print("numericalConditionFunction5")

def p_numericalConditionFunction6(p):
    '''numericalConditionFunction : alterFunction logicOperator ID'''
    print("numericalConditionFunction6")

def p_numericalConditionFunction7(p):
    '''numericalConditionFunction : ID logicOperator NUMVALUE'''
    print("numericalConditionFunction7")

def p_numericalConditionFunction8(p):
    '''numericalConditionFunction : ID logicOperator alterFunction'''
    print("numericalConditionFunction8")

def p_numericalConditionFunction9(p):
    '''numericalConditionFunction : ID logicOperator ID'''
    print("numericalConditionFunction9")

# callFunction
def p_callFunction(p):
    '''callFunction : CALL LPAR ID RPAR'''
    print("callFunction")

# valuesFunction
def p_valuesFunction1(p):
    '''valuesFunction : VALUES LPAR ID COMMA value RPAR'''
    print("valuesFunction1")

def p_valuesFunction2(p):
    '''valuesFunction : VALUES LPAR ID COMMA alterFunction RPAR'''
    print("valuesFunction2")

def p_valuesFunction3(p):
    '''valuesFunction : VALUES LPAR ID COMMA returnBoolFunction RPAR'''
    print("valuesFunction3")

def p_valuesFunction4(p):
    '''valuesFunction : VALUES LPAR ID COMMA ID RPAR'''
    print("valuesFunction4")

# iterativeFunction
def p_iterativeFunction1(p):
    '''iterativeFunction : repeatFunction'''
    print("iterativeFunction1")

def p_iterativeFunction2(p):
    '''iterativeFunction : untilFunction'''
    print("iterativeFunction2")

def p_iterativeFunction3(p):
    '''iterativeFunction : whileFunction'''
    print("iterativeFunction3")

def p_iterativeFunction4(p):
    '''iterativeFunction : casewhenFunction'''
    print("iterativeFunction4")

def p_iterativeFunction5(p):
    '''iterativeFunction : caseFunction'''
    print("iterativeFunction5")

# printFunction
def p_printFunction1(p):
    '''printFunction : PRINTVALUES LPAR ID consolePrint RPAR'''
    print("printFunction1")

def p_printFunction2(p):
    '''printFunction : PRINTVALUES LPAR TEXT consolePrint RPAR'''
    print("printFunction2")

# direction
def p_direction1(p):
    '''direction : NORTH'''
    print("direction1")

def p_direction2(p):
    '''direction : SOUTH'''
    print("direction2")

def p_direction3(p):
    '''direction : EAST'''
    print("direction3")

def p_direction4(p):
    '''direction : WEST'''
    print("direction4")

# logicOperator
def p_logicOperator1(p):
    '''logicOperator : EEOP'''
    print("logicOperator1")

def p_logicOperator2(p):
    '''logicOperator : NEOP'''
    print("logicOperator2")

def p_logicOperator3(p):
    '''logicOperator : GETOP'''
    print("logicOperator3")

def p_logicOperator4(p):
    '''logicOperator : LETOP'''
    print("logicOperator4")

def p_logicOperator5(p):
    '''logicOperator : GTOP'''
    print("logicOperator5")

def p_logicOperator6(p):
    '''logicOperator : LTOP'''
    print("logicOperator6")

# repeatFunction
def p_repeatFunction(p):
    '''repeatFunction : REPEAT LPAR insideInstruction BREAK SEMMICOLOM insideInstruction RPAR'''
    print("repeatFunction")

# untilFunction
def p_untilFunction1(p):
    '''untilFunction : UNTIL instructionBlock BOOLVALUE'''
    print("untilFunction1")

def p_untilFunction2(p):
    '''untilFunction : UNTIL instructionBlock returnBoolFunction'''
    print("untilFunction2")

def p_untilFunction3(p):
    '''untilFunction : UNTIL instructionBlock ID'''
    print("untilFunction3")

# whileFunction
def p_whileFunction1(p):
    '''whileFunction : WHILE BOOLVALUE instructionBlock'''
    print("whileFunction1")

def p_whileFunction2(p):
    '''whileFunction : WHILE returnBoolFunction instructionBlock'''
    print("whileFunction2")

def p_whileFunction3(p):
    '''whileFunction : WHILE ID instructionBlock'''
    print("whileFunction3")

# casewhenFunction
def p_casewhenFunction1(p):
    '''casewhenFunction : CASEWHEN LPAR BOOLVALUE RPAR THEN instructionBlock elseExpression'''
    print("casewhenFunction1")

def p_casewhenFunction2(p):
    '''casewhenFunction : CASEWHEN LPAR returnBoolFunction RPAR THEN instructionBlock elseExpression'''
    print("casewhenFunction2")

def p_casewhenFunction3(p):
    '''casewhenFunction : CASEWHEN LPAR ID RPAR THEN instructionBlock elseExpression'''
    print("casewhenFunction3")

# caseFunction
def p_caseFunction(p):
    '''caseFunction : CASE ID WHEN value THEN instructionBlock whenExpression elseExpression'''
    print("caseFunction")

# consolePrint
def p_consolePrint1(p):
    '''consolePrint : COMMA ID consolePrint'''
    print("consolePrint1")

def p_consolePrint2(p):
    '''consolePrint : COMMA TEXT consolePrint'''
    print("consolePrint2")

def p_consolePrint3(p):
    '''consolePrint : empty'''
    print("consolePrint3")

# elseExpression
def p_elseExpression1(p):
    '''elseExpression : ELSE instructionBlock'''
    print("elseExpression1")

def p_elseExpression2(p):
    '''elseExpression : empty'''
    print("elseExpression2")

# whenExpression
def p_whenExpression1(p):
    '''whenExpression : WHEN value THEN instructionBlock whenExpression'''
    print("whenExpression1")

def p_whenExpression2(p):
    '''whenExpression : empty'''
    print("whenExpression2")

# empty
def p_empty(p):
    '''empty :'''
    pass

# error
def p_error(p):
    print("Error de sintaxis" , p)
    print("Error en la linea" + str(p.lineno))
    
directorio = '/Users/vmartinezandres/Desktop/Lenguaje-TagaPlate/'
archivo = 'prueba.tagaplate' #buscarFicheros(directorio)
test = directorio + archivo
fp = codecs.open(test, "r", "utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()

result = parser.parse(cadena)

print(result)