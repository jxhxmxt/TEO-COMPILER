from re import A

empty = ['vacia']

#Gramática operaciones aritméticas
SOpe=0
ZOpe=1
AOpe=2
BOpe=3
COpe=4
DOpe=5

#Gramatica if else
SIfElse = 6
AIfElse = 7
BIfElse = 8
CIfElse = 9

#Gramatica variables
SVar = 10
AVar = 11
BVar = 12
CVar = 13
DVar = 14
EVar = 15
FVar = 16
GVar = 17
HVar = 18
IVar = 19
JVar = 20

STipos = 21

SFunc = 22
AFunc = 23
BFunc = 24

#Gramtica while
SWhile = 25

#Gramtica do while
SDoWhile = 26

#Gramtica for
SFor = 27

SAll = 28


operationTable = [
    #SOpe
    [SOpe,'eof',None],
    [SOpe,'SUMAR',None],
    [SOpe,'RESTAR',None],
    [SOpe,'COMPARAR_IGUAL',None],
    [SOpe,'MAYOR_QUE',None],
    [SOpe,'MENOR_QUE',None],
    [SOpe,'MULTIPLICAR',None],
    [SOpe,'DIVIDIR',None],
    [SOpe,'MODULO',None],
    [SOpe,'AND_LOGICO_CONDICIONAL',None],
    [SOpe,'OR_LOGICO_CONDICIONAL',None],
    [SOpe,'PAREN_IZQ',[AOpe,ZOpe]],
    [SOpe,'PAREN_DER',None],
    [SOpe,'IDENTIFICADOR',[AOpe,ZOpe]],
    [SOpe,'NUMERO_DECIMAL',[AOpe,ZOpe]],
    [SOpe,'NUMERO_ENTERO',[AOpe,ZOpe]],
    [SOpe,'CORCHETE_IZQ',None],
    [SOpe,'CORCHETE_DER',None],
    #ZOpe
    [ZOpe,'eof',empty],
    [ZOpe,'SUMAR',['SUMAR',AOpe,ZOpe]],
    [ZOpe,'RESTAR',['RESTAR',AOpe,ZOpe]],
    [ZOpe,'COMPARAR_IGUAL',['COMPARAR_IGUAL',AOpe,ZOpe]],
    [ZOpe,'MAYOR_QUE',['MAYOR_QUE',AOpe,ZOpe]],
    [ZOpe,'MENOR_QUE',['MENOR_QUE',AOpe,ZOpe]],
    [ZOpe,'MULTIPLICAR',None],
    [ZOpe,'DIVIDIR',None],
    [ZOpe,'MODULO',None],
    [ZOpe,'AND_LOGICO_CONDICIONAL',None],
    [ZOpe,'OR_LOGICO_CONDICIONAL',None],
    [ZOpe,'PAREN_IZQ',None],
    [ZOpe,'PAREN_DER',empty],
    [ZOpe,'IDENTIFICADOR',None],
    [ZOpe,'NUMERO_DECIMAL',None],
    [ZOpe,'NUMERO_ENTERO',None],
    [ZOpe,'CORCHETE_IZQ',None],
    [ZOpe,'CORCHETE_DER',None],
    #AOpe
    [AOpe,'eof',None],
    [AOpe,'SUMAR',None],
    [AOpe,'RESTAR',None],
    [AOpe,'COMPARAR_IGUAL',None],
    [AOpe,'MAYOR_QUE',None],
    [AOpe,'MENOR_QUE',None],
    [AOpe,'MULTIPLICAR',None],
    [AOpe,'DIVIDIR',None],
    [AOpe,'MODULO',None],
    [AOpe,'AND_LOGICO_CONDICIONAL',None],
    [AOpe,'OR_LOGICO_CONDICIONAL',None],
    [AOpe,'PAREN_IZQ',[COpe,BOpe]],
    [AOpe,'PAREN_DER',None],
    [AOpe,'IDENTIFICADOR',[COpe,BOpe]],
    [AOpe,'NUMERO_DECIMAL',[COpe,BOpe]],
    [AOpe,'NUMERO_ENTERO',[COpe,BOpe]],
    [AOpe,'CORCHETE_IZQ',None],
    [AOpe,'CORCHETE_DER',None],
    #BOpe
    [BOpe,'eof',empty],
    [BOpe,'SUMAR',empty],
    [BOpe,'RESTAR',empty],
    [BOpe,'COMPARAR_IGUAL',empty],
    [BOpe,'MAYOR_QUE',empty],
    [BOpe,'MENOR_QUE',empty],
    [BOpe,'MULTIPLICAR',['MULTIPLICAR',COpe,BOpe]],
    [BOpe,'DIVIDIR',['DIVIDIR',COpe,BOpe]],
    [BOpe,'MODULO',['MODULO',COpe,BOpe]],
    [BOpe,'AND_LOGICO_CONDICIONAL',['AND_LOGICO_CONDICIONAL',COpe,BOpe]],
    [BOpe,'OR_LOGICO_CONDICIONAL',['OR_LOGICO_CONDICIONAL',COpe,BOpe]],
    [BOpe,'PAREN_IZQ',None],
    [BOpe,'PAREN_DER',empty],
    [BOpe,'IDENTIFICADOR',None],
    [BOpe,'NUMERO_DECIMAL',None],
    [BOpe,'NUMERO_ENTERO',None],
    [BOpe,'CORCHETE_IZQ',None],
    [BOpe,'CORCHETE_DER',None],
    #COpe
    [COpe,'eof',None],
    [COpe,'SUMAR',None],
    [COpe,'RESTAR',None],
    [COpe,'COMPARAR_IGUAL',None],
    [COpe,'MAYOR_QUE',None],
    [COpe,'MENOR_QUE',None],
    [COpe,'MULTIPLICAR',None],
    [COpe,'DIVIDIR',None],
    [COpe,'MODULO',None],
    [COpe,'AND_LOGICO_CONDICIONAL',None],
    [COpe,'OR_LOGICO_CONDICIONAL',None],
    [COpe,'PAREN_IZQ',['PAREN_IZQ',SOpe,'PAREN_DER']],
    [COpe,'PAREN_DER',None],
    [COpe,'IDENTIFICADOR',['IDENTIFICADOR',DOpe]],
    [COpe,'NUMERO_DECIMAL',['NUMERO_DECIMAL']],
    [COpe,'NUMERO_ENTERO',['NUMERO_ENTERO']],
    [COpe,'CORCHETE_IZQ',None],
    [COpe,'CORCHETE_DER',None],
    #DOpe
    [DOpe,'eof',empty],
    [DOpe,'SUMAR',empty],
    [DOpe,'RESTAR',empty],
    [DOpe,'COMPARAR_IGUAL',empty],
    [DOpe,'MAYOR_QUE',empty],
    [DOpe,'MENOR_QUE',empty],
    [DOpe,'MULTIPLICAR',empty],
    [DOpe,'DIVIDIR',empty],
    [DOpe,'MODULO',empty],
    [DOpe,'AND_LOGICO_CONDICIONAL',empty],
    [DOpe,'OR_LOGICO_CONDICIONAL',empty],
    [DOpe,'PAREN_IZQ',None],
    [DOpe,'PAREN_DER',empty],
    [DOpe,'IDENTIFICADOR',None],
    [DOpe,'NUMERO_DECIMAL',None],
    [DOpe,'NUMERO_ENTERO',None],
    [DOpe,'CORCHETE_IZQ',['CORCHETE_IZQ','NUMERO_ENTERO','CORCHETE_DER']],
    [DOpe,'CORCHETE_DER',None]
]

ifElseTable = [
    #SIfElse
    [SIfElse, 'eof', None],
    [SIfElse, 'CONDICIONAL',['CONDICIONAL', 'PAREN_IZQ',SOpe,'PAREN_DER', 'LLAVE_IZQ', AIfElse]], #Agregar SInst antes de AIfElse
    [SIfElse, 'PAREN_IZQ', None],
    [SIfElse, 'PAREN_DER', None],
    [SIfElse, 'LLAVE_IZQ', None],
    [SIfElse, 'LLAVE_DER', None],
    [SIfElse, 'CASO_CONTRARIO', None],
    #AIfElse
    [AIfElse, 'eof', None],
    [AIfElse, 'CONDICIONAL', None],
    [AIfElse, 'PAREN_IZQ', None],
    [AIfElse, 'PAREN_DER', None],
    [AIfElse, 'LLAVE_IZQ', None],
    [AIfElse, 'LLAVE_DER', ['LLAVE_DER', BIfElse]], 
    [AIfElse, 'CASO_CONTRARIO', None],
    #BIfElse
    [BIfElse, 'eof', empty],
    [BIfElse, 'CONDICIONAL', None],
    [BIfElse, 'PAREN_IZQ', None],
    [BIfElse, 'PAREN_DER', None],
    [BIfElse, 'LLAVE_IZQ', None],
    [BIfElse, 'LLAVE_DER', empty],
    [BIfElse, 'CASO_CONTRARIO', ['CASO_CONTRARIO',CIfElse]],
    #CIfElse
    [CIfElse, 'eof', None],
    [CIfElse, 'CONDICIONAL', [SIfElse]],
    [CIfElse, 'PAREN_IZQ', None],
    [CIfElse, 'PAREN_DER', None],
    [CIfElse, 'LLAVE_IZQ', ['LLAVE_IZQ', AIfElse]], #Agregar SInst
    [CIfElse, 'LLAVE_DER', None],
    [CIfElse, 'CASO_CONTRARIO', None]
    
]

varFuncTable = [
    #SVar
    [SVar,'eof',None],
    [SVar,'IDENTIFICADOR',['IDENTIFICADOR',DVar]],
    [SVar,'IDENTIFICADOR',['IDENTIFICADOR','ASIGNAR','EXPRESION','PUNTO_COMA']],  # Asignación simple a un identificador
    [SVar,'ASIGNAR',None],
    [SVar,'COMA',None],
    [SVar,'PUNTO_COMA',None],
    [SVar,'PAREN_DER',None],
    [SVar,'LLAVE_IZQ',None],
    [SVar,'LLAVE_DER',None],
    [SVar,'LLAVE_IZQ',['NUMERO_ENTERO', SVar]],
    [SVar,'TIPO_ENTERO',[STipos,'IDENTIFICADOR',FVar]],
    [SVar,'TIPO_ENTERO',[STipos,'IDENTIFICADOR','ASIGNAR','EXPRESION','PUNTO_COMA']],  # Permitir asignación dentro de bloques
    [SVar,'TIPO_CADENA',[STipos,'IDENTIFICADOR',FVar]],
    [SVar,'TIPO_LARGO',[STipos,'IDENTIFICADOR',FVar]],
    [SVar,'TIPO_VACIO',[STipos,'IDENTIFICADOR',FVar]],
    [SVar,'TIPO_CARACTER',[STipos,'IDENTIFICADOR',FVar]],
    [SVar,'TIPO_FLOTANTE',[STipos,'IDENTIFICADOR',FVar]],
    [SVar,'TIPO_DOUBLE',[STipos,'IDENTIFICADOR',FVar]],
    [SVar,'PAREN_IZQ',None],
    #AVar
    [AVar,'eof',None],
    [AVar,'IDENTIFICADOR',None],
    [AVar,'ASIGNAR',['ASIGNAR',BVar]],
    [AVar,'COMA',['COMA','IDENTIFICADOR',AVar]],
    [AVar,'PUNTO_COMA',['PUNTO_COMA']],
    [AVar,'PAREN_DER',None],
    [AVar,'LLAVE_IZQ',None],
    [AVar,'LLAVE_DER',None],
    [AVar,'TIPO_ENTERO',None],
    [AVar,'TIPO_CADENA',None],
    [AVar,'TIPO_LARGO',None],
    [AVar,'TIPO_VACIO',None],
    [AVar,'TIPO_CARACTER',None],
    [AVar,'TIPO_FLOTANTE',None],
    [AVar,'TIPO_DOUBLE',None],
    [AVar,'PAREN_IZQ',None],
    #BVar
    [BVar,'eof',None],
    [BVar,'IDENTIFICADOR',['IDENTIFICADOR',AVar]],
    [BVar,'ASIGNAR',None],
    [BVar,'COMA',[CVar]],
    [BVar,'PUNTO_COMA',[CVar]],
    [BVar,'PAREN_DER',None],
    [BVar,'LLAVE_IZQ',None],
    [BVar,'LLAVE_DER',None],
    [BVar,'TIPO_ENTERO',None],
    [BVar,'TIPO_CADENA',None],
    [BVar,'TIPO_LARGO',None],
    [BVar,'TIPO_VACIO',None],
    [BVar,'TIPO_CARACTER',None],
    [BVar,'TIPO_FLOTANTE',None],
    [BVar,'TIPO_DOUBLE',None],
    [BVar,'PAREN_IZQ',None],
    #CVar
    [CVar,'eof',None],
    [CVar,'IDENTIFICADOR',None],
    [CVar,'ASIGNAR',None],
    [CVar,'COMA',['COMA',BVar]],
    [CVar,'PUNTO_COMA',['PUNTO_COMA']],
    [CVar,'PAREN_DER',None],
    [CVar,'LLAVE_IZQ',None],
    [CVar,'LLAVE_DER',None],
    [CVar,'TIPO_ENTERO',None],
    [CVar,'TIPO_CADENA',None],
    [CVar,'TIPO_LARGO',None],
    [CVar,'TIPO_VACIO',None],
    [CVar,'TIPO_CARACTER',None],
    [CVar,'TIPO_FLOTANTE',None],
    [CVar,'TIPO_DOUBLE',None],
    [CVar,'PAREN_IZQ',None],

    #DVar
    [DVar,'eof', None],
    [DVar,'IDENTIFICADOR',None],
    [DVar,'ASIGNAR',['ASIGNAR',EVar]],
    [DVar,'COMA',None],
    [DVar,'PUNTO_COMA',['PUNTO_COMA']],
    [DVar,'PAREN_DER',None],
    [DVar,'LLAVE_IZQ',None],
    [DVar,'LLAVE_DER',None],
    [DVar,'TIPO_ENTERO',None],
    [DVar,'TIPO_CADENA',None],
    [DVar,'TIPO_LARGO',None],
    [DVar,'TIPO_VACIO',None],
    [DVar,'TIPO_CARACTER',None],
    [DVar,'TIPO_FLOTANTE',None],
    [DVar,'TIPO_DOUBLE',None],
    [DVar,'PAREN_IZQ',None],
    #EVar
    [EVar,'eof', None],
    [EVar,'IDENTIFICADOR', ['IDENTIFICADOR', DVar]],
    [EVar,'ASIGNAR',None],
    [EVar,'COMA',None],
    [EVar,'PUNTO_COMA',['PUNTO_COMA']],
    [EVar,'PAREN_DER',None],
    [EVar,'LLAVE_IZQ',None],
    [EVar,'LLAVE_DER',None],
    [EVar,'TIPO_ENTERO',None],
    [EVar,'TIPO_CADENA',None],
    [EVar,'TIPO_LARGO',None],
    [EVar,'TIPO_VACIO',None],
    [EVar,'TIPO_CARACTER',None],
    [EVar,'TIPO_FLOTANTE',None],
    [EVar,'TIPO_DOUBLE',None],
    [EVar,'PAREN_IZQ',None],
    #FVar 
    [FVar,'eof', None],
    [FVar,'IDENTIFICADOR', None],
    [FVar,'ASIGNAR', [AVar]],
    [FVar,'COMA', [AVar]],
    [FVar,'PUNTO_COMA',[AVar]],
    [FVar,'PAREN_DER',None],
    [FVar,'LLAVE_IZQ',None],
    [FVar,'LLAVE_DER',None],
    [FVar,'TIPO_ENTERO',None],
    [FVar,'TIPO_CADENA',None],
    [FVar,'TIPO_LARGO',None],
    [FVar,'TIPO_VACIO',None],
    [FVar,'TIPO_CARACTER',None],
    [FVar,'TIPO_FLOTANTE',None],
    [FVar,'TIPO_DOUBLE',None],
    [FVar,'PAREN_IZQ',['PAREN_IZQ',GVar]],
    #GVar 
    [GVar,'eof', None],
    [GVar,'IDENTIFICADOR', None],
    [GVar,'ASIGNAR', None],
    [GVar,'COMA', None],
    [GVar,'PUNTO_COMA',None],
    [GVar,'PAREN_DER',['PAREN_DER', JVar]],
    [GVar,'LLAVE_IZQ',None],
    [GVar,'LLAVE_DER',None],
    [GVar,'TIPO_ENTERO', [STipos, HVar]],
    [GVar,'TIPO_CADENA',[STipos, HVar]],
    [GVar,'TIPO_LARGO',[STipos, HVar]],
    [GVar,'TIPO_VACIO',[STipos, HVar]],
    [GVar,'TIPO_CARACTER',[STipos, HVar]],
    [GVar,'TIPO_FLOTANTE',[STipos, HVar]],
    [GVar,'TIPO_DOUBLE',[STipos, HVar]],
    [GVar,'PAREN_IZQ',None],
    #HVar 
    [HVar,'eof', None],
    [HVar,'IDENTIFICADOR', ['IDENTIFICADOR', IVar]],
    [HVar,'ASIGNAR', None],
    [HVar,'COMA', [IVar]],
    [HVar,'PUNTO_COMA', None],
    [HVar,'PAREN_DER',[IVar]],
    [HVar,'LLAVE_IZQ',None],
    [HVar,'LLAVE_DER',None],
    [HVar,'TIPO_ENTERO',None],
    [HVar,'TIPO_CADENA',None],
    [HVar,'TIPO_LARGO',None],
    [HVar,'TIPO_VACIO',None],
    [HVar,'TIPO_CARACTER',None],
    [HVar,'TIPO_FLOTANTE',None],
    [HVar,'TIPO_DOUBLE',None],
    [HVar,'PAREN_IZQ',None],
    #IVar 
    [IVar,'eof', None],
    [IVar,'IDENTIFICADOR', None],
    [IVar,'ASIGNAR', None],
    [IVar,'COMA', ['COMA', GVar]],
    [IVar,'PUNTO_COMA', None],
    [IVar,'PAREN_DER',['PAREN_DER', JVar]],
    [IVar,'LLAVE_IZQ',None],
    [IVar,'LLAVE_DER',None],
    [IVar,'TIPO_ENTERO',None],
    [IVar,'TIPO_CADENA',None],
    [IVar,'TIPO_LARGO',None],
    [IVar,'TIPO_VACIO',None],
    [IVar,'TIPO_CARACTER',None],
    [IVar,'TIPO_FLOTANTE',None],
    [IVar,'TIPO_DOUBLE',None],
    [IVar,'PAREN_IZQ',None],
    #JVar
    [JVar,'eof',None],
    [JVar,'IDENTIFICADOR',None],
    [JVar,'ASIGNAR',None],
    [JVar,'COMA',None],
    [JVar,'PUNTO_COMA',['PUNTO_COMA']],
    [JVar,'PAREN_DER',None],
    [JVar,'LLAVE_IZQ',['LLAVE_IZQ','TIPO_ENTERO','IDENTIFICADOR','ASIGNAR','NUMERO_ENTERO','PUNTO_COMA',SWhile]],
    [JVar,'LLAVE_IZQ',['LLAVE_IZQ', SIfElse ,'LLAVE_DER']], #Agregar SInst antes de LLAVE_DER
    [JVar,'LLAVE_DER',None],
    [JVar,'TIPO_ENTERO',None],
    [JVar,'TIPO_CADENA',None],
    [JVar,'TIPO_LARGO',None],
    [JVar,'TIPO_VACIO',None],
    [JVar,'TIPO_CARACTER',None],
    [JVar,'TIPO_FLOTANTE',None],
    [JVar,'TIPO_DOUBLE',None],
    [JVar,'PAREN_IZQ',None],
    #STipos
    [STipos,'eof',None],
    [STipos,'IDENTIFICADOR',None],
    [STipos,'ASIGNAR',None],
    [STipos,'COMA',None],
    [STipos,'PUNTO_COMA',None],
    [STipos,'PAREN_DER',None],
    [STipos,'LLAVE_IZQ',None],
    [STipos,'LLAVE_DER',None],
    [STipos,'TIPO_ENTERO',['TIPO_ENTERO']],
    [STipos,'TIPO_CADENA',['TIPO_CADENA']],
    [STipos,'TIPO_LARGO',['TIPO_LARGO']],
    [STipos,'TIPO_VACIO',['TIPO_VACIO']],
    [STipos,'TIPO_CARACTER',['TIPO_CARACTER']],
    [STipos,'TIPO_FLOTANTE',['TIPO_FLOTANTE']],
    [STipos,'TIPO_DOUBLE',['TIPO_DOUBLE']],
    [STipos,'PAREN_IZQ',None]
]

whileTable = [
    #SWhile
    [SWhile, 'eof', None],
    [SWhile, 'BUCLE_MIENTRAS', ['BUCLE_MIENTRAS', 'PAREN_IZQ', SOpe, 'PAREN_DER', 'LLAVE_IZQ', SIfElse, 'LLAVE_DER'] ],
    [SWhile, 'PAREN_IZQ', None],
    [SWhile, 'PAREN_DER', None],
    [SWhile, 'LLAVE_IZQ', None],
    [SWhile, 'LLAVE_DER', None]
]