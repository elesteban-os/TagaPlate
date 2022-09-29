import ply.yacc as yacc
from analizadorLexico import tokens
from sys import stdin

raiz = None

class Nodo():
    def __init__(self, name, son1 = None, son2 = None, son3 = None):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
    
# program
def p_program(p):
    '''program : COMMENT outsideInstruction principalProcedure outsideInstruction'''
    global raiz
    raiz = Nodo("program", p[2], p[3], p[4])

# outsideInstruction
def p_outsideInstruction1(p):
    '''outsideInstruction : procedure SEMMICOLOM outsideInstruction'''
    p[0] = Nodo("outsideInstruction1", p[1], p[3])

def p_outsideInstruction2(p):
    '''outsideInstruction : function SEMMICOLOM outsideInstruction'''
    p[0] = Nodo("outsideInstruction2", p[1], p[3])

def p_outsideInstruction3(p):
    '''outsideInstruction : attribute SEMMICOLOM outsideInstruction'''
    p[0] = Nodo("outsideInstruction3", p[1], p[3])

def p_outsideInstruction4(p):
    '''outsideInstruction : empty'''
    p[0] = Nodo("outsideInstruction4")

# principalProcedure
def p_principalProcedure(p):
    '''principalProcedure : PPROC instructionBlock SEMMICOLOM'''
    p[0] = Nodo("principalProcedure", p[2])

# procedure
def p_procedure(p):
    '''procedure : PROC ID instructionBlock'''
    p[0] = Nodo("procedure", p[2], p[3])

# function
def p_function1(p):
    '''function : languageFunction'''
    p[0] = Nodo("function1", p[1])

def p_function2(p):
    '''function : tagadaFunction'''
    p[0] = Nodo("function2", p[1])

# attribute
def p_attribute1(p):
    '''attribute : NEW ID COMMA LPAR datatype COMMA value RPAR'''
    p[0] = Nodo("attribute1", p[2], p[5], p[7])

def p_attribute2(p):
    '''attribute : NEW ID COMMA LPAR datatype COMMA alterFunction RPAR'''
    p[0] = Nodo("attribute2", p[2], p[5], p[7])

def p_attribute3(p):
    '''attribute : NEW ID COMMA LPAR datatype COMMA returnBoolFunction RPAR'''
    p[0] = Nodo("attribute3", p[2], p[5], p[7])

def p_attribute4(p):
    '''attribute : NEW ID COMMA LPAR datatype COMMA ID RPAR'''
    p[0] = Nodo("attribute4", p[2], p[5], p[7])

# instructionBlock
def p_instructionBlock(p):
    '''instructionBlock : LPAR insideInstruction RPAR'''
    p[0] = Nodo("instructionBlock", p[2])

# insideInstruction
def p_insideInstruction1(p):
    '''insideInstruction : function SEMMICOLOM insideInstruction'''
    p[0] = Nodo("insideInstruction1", p[1], p[3])

def p_insideInstruction2(p):
    '''insideInstruction : attribute SEMMICOLOM insideInstruction'''
    p[0] = Nodo("insideInstruction2", p[1], p[3])

def p_insideInstruction3(p):
    '''insideInstruction : empty'''
    p[0] = Nodo("insideInstruction3")
    
# languageFunction
def p_languageFunction1(p):
    '''languageFunction : alterFunction'''
    p[0] = Nodo("languageFunction1", p[1])

def p_languageFunction2(p):
    '''languageFunction : returnBoolFunction'''
    p[0] = Nodo("languageFunction2", p[1])

def p_languageFunction3(p):
    '''languageFunction : voidFunction'''
    p[0] = Nodo("languageFunction3", p[1])

# tagadaFunction
def p_tagadaFunction1(p):
    '''tagadaFunction : movementFunction'''
    p[0] = Nodo("tagadaFunction1", p[1])

def p_tagadaFunction2(p):
    '''tagadaFunction : hammerFunction'''
    p[0] = Nodo("tagadaFunction2", p[1])

# datatype
def p_datatype1(p):
    '''datatype : NUMDT'''
    p[0] = Nodo("datatype1", p[1])

def p_datatype2(p):
    '''datatype : BOOLDT'''
    p[0] = Nodo("datatype2", p[1])

# value
def p_value1(p):
    '''value : NUMVALUE'''
    p[0] = Nodo("value1", p[1])

def p_value2(p):
    '''value : BOOLVALUE'''
    p[0] = Nodo("value2", p[1])

# alterFunction
def p_alterFunction1(p):
    '''alterFunction : ALTER LPAR ID COMMA numericalOperator COMMA value RPAR'''
    p[0] = Nodo("alterFunction1", p[3], p[5], p[7])

def p_alterFunction2(p):
    '''alterFunction : ALTER LPAR ID COMMA numericalOperator COMMA ID RPAR'''
    p[0] = Nodo("alterFunction2", p[3], p[5], p[7])

# returnBoolFunction
def p_returnBoolFunction1(p):
    '''returnBoolFunction : alterbFunction'''
    p[0] = Nodo("returnBoolFunction1", p[1])

def p_returnBoolFunction2(p):
    '''returnBoolFunction : istrueFunction'''
    p[0] = Nodo("returnBoolFunction2", p[1])

def p_returnBoolFunction3(p):
    '''returnBoolFunction : numericalConditionFunction'''
    p[0] = Nodo("returnBoolFunction3", p[1])

# voidFunction
def p_voidFunction1(p):
    '''voidFunction : callFunction'''
    p[0] = Nodo("voidFunction1", p[1])

def p_voidFunction2(p):
    '''voidFunction : valuesFunction'''
    p[0] = Nodo("voidFunction2", p[1])

def p_voidFunction3(p):
    '''voidFunction : iterativeFunction'''
    p[0] = Nodo("voidFunction3", p[1])

def p_voidFunction4(p):
    '''voidFunction : breakFunction'''
    p[0] = Nodo("voidFunction4", p[1])

def p_voidFunction5(p):
    '''voidFunction : caseWhenFunction'''
    p[0] = Nodo("voidFunction5", p[1])

def p_voidFunction6(p):
    '''voidFunction : caseFunction'''
    p[0] = Nodo("voidFunction6", p[1])

def p_voidFunction7(p):
    '''voidFunction : printFunction'''
    p[0] = Nodo("voidFunction7", p[1])

# movementFunction
def p_movementFunction1(p):
    '''movementFunction : MOVERIGHT'''
    p[0] = Nodo("movementFunction1", p[1])

def p_movementFunction2(p):
    '''movementFunction : MOVELEFT'''
    p[0] = Nodo("movementFunction2", p[1])

def p_movementFunction3(p):
    '''movementFunction : STOP'''
    p[0] = Nodo("movementFunction3", p[1])

# hammerFunction
def p_hammerFunction(p):
    '''hammerFunction : HAMMER LPAR direction RPAR'''
    p[0] = Nodo("hammerFunction", p[3])

# numericalOperator
def p_numericalOperator1(p):
    '''numericalOperator : ADDOP'''
    p[0] = Nodo("numericalOperator1", p[1])

def p_numericalOperator2(p):
    '''numericalOperator : SUBOP'''
    p[0] = Nodo("numericalOperator2", p[1])

def p_numericalOperator3(p):
    '''numericalOperator : MULOP'''
    p[0] = Nodo("numericalOperator3", p[1])

def p_numericalOperator4(p):
    '''numericalOperator : DIVOP'''
    p[0] = Nodo("numericalOperator4", p[1])

# alterbFunction
def p_alterbFunction(p):
    '''alterbFunction : ALTERB LPAR ID RPAR'''
    p[0] = Nodo("alterbFunction", p[3])

# istrueFunction
def p_istrueFunction1(p):
    '''istrueFunction : ISTRUE LPAR value RPAR'''
    p[0] = Nodo("istrueFunction1", p[3])

def p_istrueFunction2(p):
    '''istrueFunction : ISTRUE LPAR returnBoolFunction RPAR'''
    p[0] = Nodo("istrueFunction2", p[3])

def p_istrueFunction3(p):
    '''istrueFunction : ISTRUE LPAR ID RPAR'''
    p[0] = Nodo("istrueFunction3", p[3])

# numericalConditionFunction
def p_numericalConditionFunction1(p):
    '''numericalConditionFunction : value logicOperator value'''
    p[0] = Nodo("numericalConditionFunction1", p[1], p[2], p[3])

def p_numericalConditionFunction2(p):
    '''numericalConditionFunction : value logicOperator alterFunction'''
    p[0] = Nodo("numericalConditionFunction2", p[1], p[2], p[3])

def p_numericalConditionFunction3(p):
    '''numericalConditionFunction : value logicOperator ID'''
    p[0] = Nodo("numericalConditionFunction3", p[1], p[2], p[3])

def p_numericalConditionFunction4(p):
    '''numericalConditionFunction : alterFunction logicOperator value'''
    p[0] = Nodo("numericalConditionFunction4", p[1], p[2], p[3])

def p_numericalConditionFunction5(p):
    '''numericalConditionFunction : alterFunction logicOperator alterFunction'''
    p[0] = Nodo("numericalConditionFunction5", p[1], p[2], p[3])

def p_numericalConditionFunction6(p):
    '''numericalConditionFunction : alterFunction logicOperator ID'''
    p[0] = Nodo("numericalConditionFunction6", p[1], p[2], p[3])

def p_numericalConditionFunction7(p):
    '''numericalConditionFunction : ID logicOperator value'''
    p[0] = Nodo("numericalConditionFunction7", p[1], p[2], p[3])

def p_numericalConditionFunction8(p):
    '''numericalConditionFunction : ID logicOperator alterFunction'''
    p[0] = Nodo("numericalConditionFunction8", p[1], p[2], p[3])

def p_numericalConditionFunction9(p):
    '''numericalConditionFunction : ID logicOperator ID'''
    p[0] = Nodo("numericalConditionFunction9", p[1], p[2], p[3])

# callFunction
def p_callFunction(p):
    '''callFunction : CALL LPAR ID RPAR'''
    p[0] = Nodo("callFunction", p[3])

# valuesFunction
def p_valuesFunction1(p):
    '''valuesFunction : VALUES LPAR ID COMMA value RPAR'''
    p[0] = Nodo("valuesFunction1", p[3], p[5])

def p_valuesFunction2(p):
    '''valuesFunction : VALUES LPAR ID COMMA alterFunction RPAR'''
    p[0] = Nodo("valuesFunction2", p[3], p[5])

def p_valuesFunction3(p):
    '''valuesFunction : VALUES LPAR ID COMMA returnBoolFunction RPAR'''
    p[0] = Nodo("valuesFunction3", p[3], p[5])

def p_valuesFunction4(p):
    '''valuesFunction : VALUES LPAR ID COMMA ID RPAR'''
    p[0] = Nodo("valuesFunction4", p[3], p[5])

# iterativeFunction
def p_iterativeFunction1(p):
    '''iterativeFunction : repeatFunction'''
    p[0] = Nodo("iterativeFunction1", p[1])

def p_iterativeFunction2(p):
    '''iterativeFunction : untilFunction'''
    p[0] = Nodo("iterativeFunction2", p[1])

def p_iterativeFunction3(p):
    '''iterativeFunction : whileFunction'''
    p[0] = Nodo("iterativeFunction3", p[1])

# breakFunction
def p_breakFunction(p):
    '''breakFunction : BREAK'''
    p[0] = Nodo("breakFunction", p[1])

# printFunction
def p_printFunction1(p):
    '''printFunction : PRINTVALUES LPAR ID consolePrint RPAR'''
    p[0] = Nodo("printFunction1", p[3], p[4])

def p_printFunction2(p):
    '''printFunction : PRINTVALUES LPAR TEXT consolePrint RPAR'''
    p[0] = Nodo("printFunction2", p[3], p[4])

# direction
def p_direction1(p):
    '''direction : NORTH'''
    p[0] = Nodo("direction1", p[1])

def p_direction2(p):
    '''direction : SOUTH'''
    p[0] = Nodo("direction2", p[1])

def p_direction3(p):
    '''direction : EAST'''
    p[0] = Nodo("direction3", p[1])

def p_direction4(p):
    '''direction : WEST'''
    p[0] = Nodo("direction4", p[1])

# logicOperator
def p_logicOperator1(p):
    '''logicOperator : EEOP'''
    p[0] = Nodo("logicOperator1", p[1])

def p_logicOperator2(p):
    '''logicOperator : NEOP'''
    p[0] = Nodo("logicOperator2", p[1])

def p_logicOperator3(p):
    '''logicOperator : GETOP'''
    p[0] = Nodo("logicOperator3", p[1])

def p_logicOperator4(p):
    '''logicOperator : LETOP'''
    p[0] = Nodo("logicOperator4", p[1])

def p_logicOperator5(p):
    '''logicOperator : GTOP'''
    p[0] = Nodo("logicOperator5", p[1])

def p_logicOperator6(p):
    '''logicOperator : LTOP'''
    p[0] = Nodo("logicOperator6", p[1])

# repeatFunction
def p_repeatFunction(p):
    '''repeatFunction : REPEAT LPAR insideInstruction RPAR'''
    p[0] = Nodo("repeatFunction", p[3])

# untilFunction
def p_untilFunction1(p):
    '''untilFunction : UNTIL instructionBlock value'''
    p[0] = Nodo("untilFunction1", p[2], p[3])

def p_untilFunction2(p):
    '''untilFunction : UNTIL instructionBlock returnBoolFunction'''
    p[0] = Nodo("untilFunction2", p[2], p[3])

def p_untilFunction3(p):
    '''untilFunction : UNTIL instructionBlock ID'''
    p[0] = Nodo("untilFunction3", p[2], p[3])

# whileFunction
def p_whileFunction1(p):
    '''whileFunction : WHILE value instructionBlock'''
    p[0] = Nodo("whileFunction1", p[2], p[3])

def p_whileFunction2(p):
    '''whileFunction : WHILE returnBoolFunction instructionBlock'''
    p[0] = Nodo("whileFunction2", p[2], p[3])

def p_whileFunction3(p):
    '''whileFunction : WHILE ID instructionBlock'''
    p[0] = Nodo("whileFunction3", p[2], p[3])

# caseWhenFunction
def p_caseWhenFunction1(p):
    '''caseWhenFunction : CASE WHEN LPAR value RPAR THEN instructionBlock elseExpression'''
    p[0] = Nodo("caseWhenFunction1", p[4], p[7], p[8])

def p_caseWhenFunction2(p):
    '''caseWhenFunction : CASE WHEN LPAR returnBoolFunction RPAR THEN instructionBlock elseExpression'''
    p[0] = Nodo("caseWhenFunction2", p[4], p[7], p[8])

def p_caseWhenFunction3(p):
    '''caseWhenFunction : CASE WHEN LPAR ID RPAR THEN instructionBlock elseExpression'''
    p[0] = Nodo("caseWhenFunction3", p[4], p[7], p[8])

# caseFunction
def p_caseFunction(p):
    '''caseFunction : CASE ID whenExpression elseExpression'''
    p[0] = Nodo("caseFunction", p[2], p[3], p[4])

# consolePrint
def p_consolePrint1(p):
    '''consolePrint : COMMA ID consolePrint'''
    p[0] = Nodo("consolePrint1", p[2], p[3])

def p_consolePrint2(p):
    '''consolePrint : COMMA TEXT consolePrint'''
    p[0] = Nodo("consolePrint2", p[2], p[3])

def p_consolePrint3(p):
    '''consolePrint : empty'''
    p[0] = Nodo("consolePrint3")

# elseExpression
def p_elseExpression1(p):
    '''elseExpression : ELSE instructionBlock'''
    p[0] = Nodo("elseExpression1", p[2])

def p_elseExpression2(p):
    '''elseExpression : empty'''
    p[0] = Nodo("elseExpression2")

# whenExpression
def p_whenExpression1(p):
    '''whenExpression : WHEN value THEN instructionBlock whenExpression'''
    p[0] = Nodo("whenExpression1", p[2], p[4], p[5])

def p_whenExpression2(p):
    '''whenExpression : WHEN value THEN instructionBlock'''
    p[0] = Nodo("whenExpression2", p[2], p[4])

# empty
def p_empty(p):
    '''empty :'''
    pass

# error
def p_error(p):
    try:
        print("Excepcion: (Sintactico) Sintaxis incorrecta, linea: " + str(p.lineno))
    except:
        print("Excepcion: (Sintactico) Sintaxis incorrecta")
    exit()

def iniciarAnalisis(cadena):
    parser = yacc.yacc()
    parser.parse(cadena)
