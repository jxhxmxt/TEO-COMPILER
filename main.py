import grammar_rules as table
import lexer
import non_terminals as nonTerminals
import terminals

nt = nonTerminals.NonTerminals
t = terminals.Terminals
c_lexer = lexer.lexer
tokens = lexer.tokens

stack = [t.EOF.value, nt.TRANSLATION_UNIT.value]
tabla = table.tablaC
myDict = {}

def get_hash(key):
    h=20
    for char in key:
        h += ord(char)
    return h % 100

def tlpParser():
    declaration_flag = 0
    block_flag = 0
    block_finish = True
    block_compount = False
    expression_statement_flag = False
    unary_operator = 0
    string_error = False
    hashWord = "Token 1"

    f = open('source.c','r')
    blocks = len(f.readlines())
    
    f.seek(0)

    if "\"" in f.read() :
        string_error = True
    f.seek(0)
        
    c_lexer.input(f.read() + '$')
    
    tok=c_lexer.token()
    
    x=stack[-1] #primer elemento de der a izq
    while True:
        if block_flag == (blocks-2) and block_finish:
            stack.pop()
            x = stack[-1]
            block_finish = False

        if x == t.IDENTIFIER.value and declaration_flag == 0 :
            declaration_flag = 1
        
        if x == t.ADD_EQ.value or x == t.MUL_EQ.value or x == t.SUB_EQ.value or x == t.DIV_EQ.value :
            unary_operator = unary_operator + 1

        if x == tok.type and x == t.EOF.value:
            print("Cadena reconocida exitosamente")
            return #aceptar

        else:
            if x == tok.type and x != t.EOF.value:

                hashKey = get_hash(hashWord)
                hashWord += "1"

                if tok.type != "error" :
                    auxDict = {hashKey: {"Type": tok.type, "Token": tok.value, "Line": tok.lineno, "Position": tok.lexpos}}
                    myDict.update(auxDict)   
                stack.pop()
                x=stack[-1]
                tok=c_lexer.token()                
            if x in tokens and x != tok.type:
                print("Error se esperaba: ", x)
                print("en la posicion: ", tok.lexpos)
                # Panic Mode - Manejador de Errores 
                while True :
                    tok = c_lexer.token()
                    if tok.type == x :
                        break
            if x not in tokens: 
                # es no terminal
                # print("van entrar a la tabla:")
                # print(x)
                # print(tok.type)
                if x == nt.BLOCK_ITEM_LIST.value and block_finish :
                    block_flag = block_flag + 1

                if x == nt.BLOCK_ITEM.value : 
                    block_compount = True

                if x == nt.BLOCK_ITEM.value and tok.type == t.IDENTIFIER.value :
                    expression_statement_flag = True
                
                celda=buscar_en_tabla(x,tok.type)
                if declaration_flag == 1 and celda == [t.IDENTIFIER.value, t.LEFT_PAREN.value, t.RIGHT_PAREN.value] :
                    celda = [t.IDENTIFIER.value]
                
                if block_compount and celda == [t.LEFT_CURLY.value, nt.BLOCK_ITEM_LIST.value, t.RIGHT_CURLY.value] : 
                    celda = [t.LEFT_CURLY.value, t.RIGHT_CURLY.value]
                
                if expression_statement_flag and x == nt.STATEMENT.value :
                    celda = [nt.EXPRESSION_STATEMENT.value]
                
                if x == nt.EXPRESSION.value and expression_statement_flag :
                    celda = [nt.ASSIGNMENT_EXPRESSION.value]
                
                if x == nt.ASSIGNMENT_OPERATOR.value and unary_operator == 0 :
                    celda = [t.ADD_EQ.value]
                elif x == nt.ASSIGNMENT_OPERATOR.value and unary_operator == 1 :
                    celda = [t.SUB_EQ.value]
                elif x == nt.ASSIGNMENT_OPERATOR.value and unary_operator == 2 :
                    celda = [t.MUL_EQ.value]
                elif x == nt.ASSIGNMENT_OPERATOR.value and unary_operator == 3 :
                    celda = [t.DIV_EQ.value]
                    expression_statement_flag = False
                
                if celda == [nt.DECLARATOR.value, t.EQUALS.value, t.NUMBER.value] and string_error :
                    celda = [nt.DECLARATOR.value, t.EQUALS.value, t.STRING.value]
                    string_error = False

                if  celda is None:
                    print("Error: NO se esperaba", tok.type)
                    print("En posición:", tok.lexpos)
                    return 0;
                else:
                    stack.pop()
                    agregar_pila(celda)
                    print(stack)
                    print("------------")
                    x=stack[-1]            

def buscar_en_tabla(no_terminal, terminal):
    for i in range(len(tabla)):
        if( tabla[i][0] == no_terminal and tabla[i][1] == terminal):
            return tabla[i][2] #retorno la celda

def agregar_pila(produccion):
    for elemento in reversed(produccion):
        if elemento != 'vacia': #la vacía no la inserta
            stack.append(elemento)

# Ejercucion del Parser 
tlpParser()

 #Imprimir valores del diccionario de datos
# print("Key","\t", "Value")
# for key, value in myDict.items() :
#     print(key,"\t", value)

# print("----------------")

semanticHash = []

def findVariableDeclarations() :
    hashIndex = 0
    hashedList = list(myDict.values())
    n = len(hashedList)
    for i in range(0, n) :
        if (hashedList[i]['Token'] == t.INT.value or hashedList[i]['Token'] == t.FLOAT.value) and hashedList[i+2]["Token"] == '=' :
            semanticHash.append({"Type": hashedList[i]['Token'], "Value": hashedList[i+3]['Token'], 'Line': hashedList[i]['Line']})
        
        if hashedList[i]['Token'] == t.IF.value and hashedList[i+2]['Type'] == t.IDENTIFIER.value:
            semanticHash.append({"Type": hashedList[i]['Token'], 'Value': hashedList[i+2]['Type'], 'Line': hashedList[i]['Line']})

def checkVariableDeclarations() :
    for i in semanticHash :
        if (i['Type'] == t.INT.value) and  type(i['Value']) != int :
            print("Error semántico: Declaracion de Variable Int espera un Entero en la linea ", i['Line'])
        
        if (i['Type'] == t.IF.value) and i['Value'] == t.IDENTIFIER.value :
            print("Error semántico: Tipos no Compatibles en la linea ", i['Line'])


# def miAnalizadorSemantico() :
#     findVariableDeclarations()
#     checkVariableDeclarations()

# miAnalizadorSemantico()

