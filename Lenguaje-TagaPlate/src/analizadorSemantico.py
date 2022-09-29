import codecs
import analizadorSintactico
from analizadorSintactico import Nodo

from pyfirmata import Arduino, SERVO, util, UNAVAILABLE
from time import sleep

port = 'COM3'
Martillo1 = 10
Martillo2 = 9
Giro = 8

board = Arduino(port)

board.digital[Martillo1].mode = SERVO
board.digital[Martillo1].write(90)

board.digital[Martillo2].mode = SERVO
board.digital[Martillo2].write(90)



localAttributes = {}
globalAttributes = {}
procedures = {}

numLocalAttList = []
repeatFunctionList = []
untilFunctionList = []
whileFunctionList = []
caseWhenFunctionList = []

isPrincipalProcedure = False 
isInstructionBlock = False 
isBreakFunction = False
isInsideLoop = False

numLocalAtt = 0

def recorrerArbol(root):
    if(root == None or type(root) == str): 
        return root
    else:

        # Aqui comienza a recorrer un arbol 
        if(root.name == "principalProcedure"):
            principalProcedure()

        elif(root.name == "procedure"):
            procedure(root)
        
        elif(root.name == "instructionBlock"):
            instructionBlock(False)

        elif(root.name == "insideInstruction1" or root.name == "insideInstruction2" or root.name == "insideInstruction3"):
            insideInstruction(root)

        elif(root.name == "iterativeFunction1" or root.name == "iterativeFunction2" or root.name == "iterativeFunction3"):
            iterativeFunction()

        elif(root.name == "repeatFunction"):
            repeatFunction(root, False)

        elif(root.name == "untilFunction1" or root.name == "untilFunction2" or root.name == "untilFunction3"):
            untilFunction(root, False)

        elif(root.name == "whileFunction1" or root.name == "whileFunction2" or root.name == "whileFunction3"):
            whileFunction(root, False)
        
        elif(root.name == "caseWhenFunction1" or root.name == "caseWhenFunction2" or root.name == "caseWhenFunction3"):
            caseWhenFunction(root, False)
        
        elif(root.name == "caseFunction"):
            caseFunction(root)
    
        root.son1 = recorrerArbol(root.son1)
        root.son2 = recorrerArbol(root.son2)
        root.son3 = recorrerArbol(root.son3)

        # Aqui termina de recorrer un arbol
        if(root.name == "principalProcedure"):
            principalProcedure()

        elif(root.name == "attribute1" or root.name == "attribute2" or root.name == "attribute3" or root.name == "attribute4"):
            attribute(root)
    
        elif(root.name == "instructionBlock"):
            instructionBlock(True)

        elif(root.name == "datatype1" or root.name == "datatype2"):
            return datatype(root)

        elif(root.name == "value1" or root.name == "value2"):
            return value(root)

        elif(root.name == "alterFunction1" or root.name == "alterFunction2"):
            return alterFunction(root)

        elif(root.name == "returnBoolFunction1" or root.name == "returnBoolFunction2" or root.name == "returnBoolFunction3"):
            return returnBoolFunction(root)

        elif(root.name == "movementFunction1" or root.name == "movementFunction2" or root.name == "movementFunction3"):
            movementFunction(root)
        
        elif(root.name == "hammerFunction"):
            hammerFunction(root)

        elif(root.name == "numericalOperator1" or root.name == "numericalOperator2" or root.name == "numericalOperator3" or root.name == "numericalOperator4"):
            return numericalOperator(root)
        
        elif(root.name == "alterbFunction"):
            return alterbFunction(root)

        elif(root.name == "istrueFunction1" or root.name == "istrueFunction2" or root.name == "istrueFunction3"):
            return istrueFunction(root)

        elif(root.name == "numericalConditionFunction1" or root.name == "numericalConditionFunction2" or root.name == "numericalConditionFunction3" or root.name == "numericalConditionFunction4" or root.name == "numericalConditionFunction5" or root.name == "numericalConditionFunction6" or root.name == "numericalConditionFunction7" or root.name == "numericalConditionFunction8" or root.name == "numericalConditionFunction9"):
            return numericalConditionFunction(root)

        elif(root.name == "callFunction"):
            callFunction(root)

        elif(root.name == "valuesFunction1" or root.name == "valuesFunction2" or root.name == "valuesFunction3" or root.name == "valuesFunction4"):
            valuesFunction(root)

        elif(root.name == "breakFunction"):
            breakFunction()

        elif(root.name == "printFunction1" or root.name == "printFunction2"):
            printFunction(root)

        elif(root.name == "direction1" or root.name == "direction2" or root.name == "direction3" or root.name == "direction4"):
            return direction(root)   

        elif(root.name == "logicOperator1" or root.name == "logicOperator2" or root.name == "logicOperator3" or root.name == "logicOperator4" or root.name == "logicOperator5" or root.name == "logicOperator6"):
            return logicOperator(root)

        elif(root.name == "repeatFunction"):
            repeatFunction(root, True)

        elif(root.name == "untilFunction1" or root.name == "untilFunction2" or root.name == "untilFunction3"):
            untilFunction(root, True)

        elif(root.name == "whileFunction1" or root.name == "whileFunction2" or root.name == "whileFunction3"):
            whileFunction(root, True)

        elif(root.name == "caseWhenFunction1" or root.name == "caseWhenFunction2" or root.name == "caseWhenFunction3"):
            caseWhenFunction(root, True)

        elif(root.name == "consolePrint1" or root.name == "consolePrint2" or root.name == "consolePrint3"):
            return consolePrint(root)

        return None
            
# Función para cambiar el valor de isPrincipalProcedure, para saber si se está dentro de la función principal
def principalProcedure():
    global isPrincipalProcedure
    isPrincipalProcedure = not isPrincipalProcedure

# Función para guardar el nombre de un procedimiento y saber lo que hace
def procedure(nodo):
    procedures[nodo.son1] = construirArbol(nodo.son2)

# Funcion para constriur un nuevo arbol que contenga las indicaciones de un procedimiento
def construirArbol(nodo):
    if(nodo == None or type(nodo) == str):
        return nodo
    else:
        return Nodo(nodo.name, construirArbol(nodo.son1), construirArbol(nodo.son2), construirArbol(nodo.son3))

# Función para guardar nuevos atributos
def attribute(nodo):
    comprobarAtributo(nodo.son1)
    global numLocalAtt

    nombre = nodo.son1
    tipo = nodo.son2
    valor = nodo.son3
               
    if(nodo.name == "attribute4"): 
        valor = buscarAtributo(nodo.son3)
        
    if((tipo == "Num" and type(valor) != int) or (tipo == "Bool" and type(valor) != bool)):
        print("Excepcion: (Atributo) La variable: \"" + nombre +"\" es de tipo: " + tipo +", pero el valor asignado es: " + str(valor))
        exit()
    else:
        if(isPrincipalProcedure):
            globalAttributes[nombre] = valor

        else:
            localAttributes[nombre] = valor
            if(isInstructionBlock):
                numLocalAtt += 1

# Función complementaria para comprobar la existencia de un atributo
def comprobarAtributo(nombre):
    if(nombre in localAttributes):
        print("Excepcion: (Atributo) La variable local: \"" + nombre +"\" ya existe")
        exit()
    else:
        if(nombre in globalAttributes):
            print("Excepcion: (Atributo) La variable global: \"" + nombre +"\" ya existe")
            exit()

# Función que devuelve el valor de una variable o un error
def buscarAtributo(nombre):
    if(nombre in localAttributes):
        return localAttributes[nombre]
    else:
        if(nombre in globalAttributes):
            return globalAttributes[nombre]
        else:
            print("Excepcion: (Atributo) La variable: \"" + nombre +"\" no existe")
            exit()

# Función para saber que variables locales deben existir o removerse
def instructionBlock(isFinished):
    if (not isPrincipalProcedure):
        global isInstructionBlock
        global numLocalAttList
        global numLocalAtt

        isInstructionBlock = not isFinished

        if(numLocalAtt > 0):
            numLocalAttList.append(numLocalAtt)
            numLocalAtt = 0

        if(isFinished):
            if(bool(numLocalAttList)):
                for i in range(numLocalAttList[len(numLocalAttList)-1]):
                    localAttributes.popitem()
                numLocalAttList.pop(len(numLocalAttList)-1)
                if(bool(numLocalAttList)):
                    numLocalAtt = numLocalAttList[len(numLocalAttList)-1]
                else:
                    numLocalAtt = 0

# Funcion para controlar que si hay un break y se deben dejar de ejecutar instrucciones
def insideInstruction(nodo):
    if(isBreakFunction):
        nodo.son1 = None
        nodo.son2 = None
        nodo.son3 = None

# Función que retorna el tipo de dato                    
def datatype(nodo):
    return nodo.son1

# Función que deveulve un valor numerico o booleano                   
def value(nodo):
    if(nodo.son1 == "True"):
        return True
    elif(nodo.son1 == "False"):
        return False
    else:
        return int(nodo.son1)

# Función que cambia el valor de una variable numerica y retorna su valor
def alterFunction(nodo):
    valor1 = buscarAtributo(nodo.son1)
    if(type(valor1) != int):
        print("Excepcion: (Función Alter) La variable: \"" + nodo.son1 +"\" no es de tipo: Num")
        exit()
    else:
        valor2 = nodo.son3
        if(nodo.name == "alterFunction2"):
            valor2 = buscarAtributo(nodo.son3)

        if(type(valor2) != int):
            print("Excepcion: (Función Alter) La variable: \"" + nodo.son3 +"\" no es de tipo: Num")
            exit()
        else:
            if(nodo.son2 == "ADD"):
                resultado = valor1 + valor2

            elif(nodo.son2 == "SUB"):
                resultado = valor1 - valor2

            elif(nodo.son2 == "MUL"):
                resultado = valor1 * valor2

            else:
                resultado = valor1 / valor2


            if(nodo.son1 in localAttributes):
                localAttributes[nodo.son1] = resultado

            else:
                globalAttributes[nodo.son1] = resultado

            return resultado  

# Función que devuelve el valor booleano retornado por otras funciones
def returnBoolFunction(nodo):
    return nodo.son1

# Función para realizar movimientos de la tagada
def movementFunction(nodo):
    global board
    
    if(nodo.son1 == "MoveRight"):
        print("Aquí pase1")
        board.digital[Giro].mode = SERVO

        board.digital[Giro].write(180)#Hace que el motor gire 180° a la izquierda.
        sleep(0.2)#Timer para que el motor gire

        board.exit()
        
        board = Arduino(port)

        board.digital[Martillo1].mode = SERVO
        board.digital[Martillo1].write(90)

        board.digital[Martillo2].mode = SERVO
        board.digital[Martillo2].write(90)

        sleep(1) #Espera 1 segundo para la siguiente instrucción

    elif(nodo.son1 == "MoveLeft"):
        print("Aquí pase2")
        board.digital[Giro].mode = SERVO

        board.digital[Giro].write(20)  # Hace que el motor gire 180° a la derecha.
        sleep(0.2)  # Timer para que el motor gire

        board.exit()

        board = Arduino(port)

        board.digital[Martillo1].mode = SERVO
        board.digital[Martillo1].write(90)

        sleep(1)

        board.digital[Martillo2].mode = SERVO
        board.digital[Martillo2].write(90)

        sleep(1)  # Espera 1 segundo para la siguiente instrucción
    else:
        print("Se detuvo")


# Función para realizar utilizar el martillo en la tagada
def hammerFunction(nodo):
    if nodo.son1 == "N":
        print("Martillo Norte")
        board.digital[Martillo1].write(180)
        sleep(1)
        board.digital[Martillo1].write(90)
        sleep(1)
        

    elif nodo.son1 == "S":
        print("Martillo Sur")
        board.digital[Martillo1].write(0)
        sleep(1)
        board.digital[Martillo1].write(90)
        sleep(1)


    elif nodo.son1=="E":
        print("Martillo Este")
        board.digital[Martillo2].write(180)
        sleep(1)
        board.digital[Martillo2].write(90)
        sleep(1)


    elif nodo.son1=="O":
        print("Martillo Oeste")
        board.digital[Martillo2].write(0)
        sleep(1)
        board.digital[Martillo2].write(90)
        sleep(1)

# Función que devuelve el operador numerico
def numericalOperator(nodo):
    return nodo.son1

# Función que cambia el valor de una variable booleana y retorna su valor
def alterbFunction(nodo):
    valor = buscarAtributo(nodo.son1)
    if(type(valor) != bool):
        print("Excepcion: (Función AlterB) La variable: \"" + nodo.son1 +"\" no es de tipo: Bool")
        exit()
    else:
        if(nodo.son1 in localAttributes):
            localAttributes[nodo.son1] = not valor

        else:
            globalAttributes[nodo.son1] = not valor

        return not valor   

# Función que determina si lo que está dentro es verdadero o falso
def istrueFunction(nodo):
    valor = nodo.son1
    if(nodo.name == "istrueFunction3"):
        valor = buscarAtributo(nodo.son1)
    
    if(type(valor) != bool):
        print("Excepcion: (Función Istrue) valor no booleano encontrado")
        exit()
    else:
        print(valor)
        return valor

# Función que determina la veracidad de una expresión booleana que utiliza operadores logicos
def numericalConditionFunction(nodo):
    valor1 = nodo.son1
    valor2 = nodo.son3

    if(nodo.name == "numericalConditionFunction7" or nodo.name == "numericalConditionFunction8" or nodo.name == "numericalConditionFunction9"):
        valor1 = buscarAtributo(nodo.son1)
    
    if(nodo.name == "numericalConditionFunction3" or nodo.name == "numericalConditionFunction6" or nodo.name == "numericalConditionFunction9"):
        valor2 = buscarAtributo(nodo.son3)

    if(type(valor1) != int or type(valor2) != int):
        print("Excepcion: (Función Numerical-Condition) Valores no numéricos encontrados")
        exit()
    else:
        if(nodo.son2 == "=="):
            resultado = valor1 == valor2

        elif(nodo.son2 == "<>"):
            resultado = valor1 != valor2

        elif(nodo.son2 == ">="):
            resultado = valor1 >= valor2

        elif(nodo.son2 == "<="):
            resultado = valor1 <= valor2

        elif(nodo.son2 == ">"):
            resultado = valor1 > valor2

        else:
            resultado = valor1 < valor2

        return resultado

# Función para llamar otras funciones
def callFunction(nodo):
    if(nodo.son1 in procedures):
        instructionBlockNode = construirArbol(procedures[nodo.son1])
        recorrerArbol(instructionBlockNode)
    else:
        print("Excepcion: (Función CALL) El procedimiento: \"" + nodo.son1 +"\" no existe")
        exit()

# Función para cambiar el valor de un valor numérico o booleano
def valuesFunction(nodo):
    nombre = nodo.son1
    valor = nodo.son2
    
    if(nodo.name == "valuesFunction4"):
        valor = buscarAtributo(nodo.son2)

    if(nodo.son1 in localAttributes):
        localAttributes[nombre] = valor

    else:
        globalAttributes[nombre] = valor

# Funcion para saber si se está en un bucle
def iterativeFunction():
    global isInsideLoop
    isInsideLoop = True

# breakFunction
def breakFunction():
    if(isInsideLoop):
        global isBreakFunction
        isBreakFunction = True
    else:
        print("Excepcion: (Función Break) Procedimiento fuera de un bucle")
        exit()

# Función para imprimir texto, variables o una concatenacion de ambos
def printFunction(nodo):
    if(nodo.name == "printFunction1"):
        texto = str(buscarAtributo(nodo.son1)) + nodo.son2
        print(texto)

    else:
        texto = nodo.son1[1:len(nodo.son1) - 1] + nodo.son2
        print(texto)   

# Función que retorna la direccion
def direction(nodo):
    return nodo.son1  

# Función que retorna el operador lógico
def logicOperator(nodo):
    return nodo.son1

# Funcion de while infinito
def repeatFunction(nodo, isFinished):
    global isInsideLoop
    global isBreakFunction
    if(isFinished):
        if(isBreakFunction):
            repeatFunctionList.pop(len(repeatFunctionList) - 1)
            isBreakFunction = False
        
        else:
            repeatFunctionNode = construirArbol(repeatFunctionList[len(repeatFunctionList) - 1])
            repeatFunctionList.pop(len(repeatFunctionList) - 1)
            recorrerArbol(repeatFunctionNode)
    
        if(not(bool(repeatFunctionList) and bool(untilFunctionList) and bool(whileFunctionList))):
            isInsideLoop = False

    else:
        repeatFunctionList.append(construirArbol(nodo))

# Funcion iterativa, parecida a un do-while
def untilFunction(nodo, isFinished):
    global isInsideLoop
    global isBreakFunction
    if(isFinished):
        if(isBreakFunction):
            untilFunctionList.pop(len(untilFunctionList) - 1)
            isBreakFunction = False
        
        else:
            condicion = nodo.son2
            if(nodo.name == "untilFunction3"):
                condicion = buscarAtributo(nodo.son2)

            if(type(condicion) != bool):
                print("Excepcion: (Función Until) condición no booleana encontrada")
                exit()
            
            else:
                if(condicion):
                    untilFunctionNode = construirArbol(untilFunctionList[len(untilFunctionList) - 1])
                    untilFunctionList.pop(len(untilFunctionList) - 1)
                    recorrerArbol(untilFunctionNode)
                else:
                    untilFunctionList.pop(len(untilFunctionList) - 1)

        if(not(bool(repeatFunctionList) and bool(untilFunctionList) and bool(whileFunctionList))):
            isInsideLoop = False

    else:
        untilFunctionList.append(construirArbol(nodo))

# Funcion iterativa, parecida a un while
def whileFunction(nodo, isFinished):
    global isInsideLoop
    global isBreakFunction
    if(isFinished):
        if(isBreakFunction):
            whileFunctionList.pop(len(whileFunctionList) - 1)
            isBreakFunction = False

        else:
            condicion = nodo.son1

            if(nodo.name == "whileFunction3"):
                condicion = buscarAtributo(nodo.son1)

            if(type(condicion) != bool):
                print("Excepcion: (Función While) condición no booleana encontrada")
                exit()
            else:
                if(condicion):
                    instructionBlockNode = construirArbol(whileFunctionList[len(whileFunctionList) - 1].son2)
                    recorrerArbol(instructionBlockNode)

                    whileFunctionNode = construirArbol(whileFunctionList[len(whileFunctionList) - 1])
                    whileFunctionList.pop(len(whileFunctionList) - 1)
                    recorrerArbol(whileFunctionNode)
                else:
                    whileFunctionList.pop(len(whileFunctionList) - 1)

        if(not(bool(repeatFunctionList) and bool(untilFunctionList) and bool(whileFunctionList))):
            isInsideLoop = False

    else:   
        whileFunctionList.append(construirArbol(nodo))
        nodo.son2 = None

# Funcion parecida a un if
def caseWhenFunction(nodo, isFinished):
    if(isFinished):
        condicion = nodo.son1

        if(nodo.name == "caseWhenFunction3"):
            condicion = buscarAtributo(nodo.son1)

        if(type(condicion) != bool):
            print("Excepcion: (Función Case-When) condición no booleana encontrada")
            exit()
        else:
            if(condicion):
                instructionBlockNode = construirArbol(caseWhenFunctionList[len(caseWhenFunctionList) - 1].son2)
                caseWhenFunctionList.pop(len(caseWhenFunctionList) - 1)
                recorrerArbol(instructionBlockNode)
            else:
                ElseExpressionNode = construirArbol(caseWhenFunctionList[len(caseWhenFunctionList) - 1].son3)
                caseWhenFunctionList.pop(len(caseWhenFunctionList) - 1)
                recorrerArbol(ElseExpressionNode)

    else:   
        caseWhenFunctionList.append(construirArbol(nodo))
        nodo.son2 = None
        nodo.son3 = None

# Funcion para guardar el valor de una expresion case
def caseFunction(nodo):
    valor = buscarAtributo(nodo.son1)
    nodo.son2 = whenExpression(nodo.son2, valor)
    if(nodo.son2 != None):
        recorrerArbol(nodo.son2.son2)
        nodo.son2 = None
        nodo.son3 = None
    else:
        nodo.son2 = None    

# Función para poder concatenar el texto o variables en un print
def consolePrint(nodo):
    if(nodo.name == "consolePrint1"):
        texto = str(buscarAtributo(nodo.son1)) + nodo.son2

    elif(nodo.name == "consolePrint2"):
        texto = nodo.son1[1:len(nodo.son1) - 1] + nodo.son2

    else:
        texto = ""

    return texto

# Funcion para guardar las expresiones when
def whenExpression(nodo, valor1):
    if(nodo == None):
        return nodo
    else:
        valor2 = value(nodo.son1)
        if(type(valor1) != type(valor2)):
            print("Excepcion: (Función Case) El tipo de dato de la variable no concuerda con el valor ingresado")
            exit()
        else:
            if(valor1 == valor2):
                nodo.son3 = None
                return nodo
            else:
                return whenExpression(nodo.son3, valor1)
    
    
directorio = 'C:/Users/Daniel Montoya/Desktop/Taga/Lenguaje-TagaPlate/'
archivo = 'prueba.tagaplate'
test = directorio + archivo
fp = codecs.open(test, "r", "utf-8")
cadena = fp.read()
fp.close()

analizadorSintactico.iniciarAnalisis(cadena)

recorrerArbol(analizadorSintactico.raiz)
