from ply import lex

tokens = (
  #operadores
  'ASIGNAR',
  'SUMAR',
  'RESTAR',  
  'DIVIDIR',
  'MULTIPLICAR',
  'MODULO',
  'MAYOR_QUE', 
  'MENOR_QUE',
  'NEGACION',
  'AND_LOGICO',
  'OR_LOGICO',
  #operadores compuestos
  'MAYOR_IGUAL', 
  'MENOR_IGUAL',
  'INCREMENTO',
  'DECREMENTO',
  'COMPARAR_IGUAL',
  'COMPARAR_DIF',
  'AND_LOGICO_CONDICIONAL',
  'OR_LOGICO_CONDICIONAL',
  'ASIGNAR_SUMA',
  'ASIGNAR_RESTA',
  'ASIGNAR_MULT',
  'ASIGNAR_DIV',
  'DIVISION_ENTERA',
  #palabras reservadas
  'ESTATICO',
  'CONDICIONAL',
  'BUCLE_PARA',
  'BUCLE_MIENTRAS',
  'HACER',
  'RETORNAR',
  'CASO_CONTRARIO',
  'ESTRUCTURA',
  'ROMPER',
  #directivas
  "DIR_INCLUIR",
  "DIR_DEFINIR",
  "DIR_UNDEFINIR",
  #tipos de datos

  'TIPO_ENTERO',
  'TIPO_CADENA',
  'TIPO_LARGO',
  'TIPO_VACIO',
  'TIPO_CARACTER',
  'TIPO_FLOTANTE',
  'TIPO_DOUBLE',

  #puntuacion
  'PUNTO',
  'PUNTO_COMA',
  'COMILLA_SIMPLE',
  'COMA',
  'PAREN_IZQ',
  'PAREN_DER',
  'CORCHETE_IZQ',
  'CORCHETE_DER',
  'COMILLA_DOBLE',
  'LLAVE_IZQ',
  'LLAVE_DER',
  #identificador
  'IDENTIFICADOR',
  #cadenas
  'CADENA',
  'CARACTER',
  #numeros
  'NUMERO_ENTERO',
  'NUMERO_DECIMAL',
  #eof
  'eof'
)

reservadas = {
  'int': 'TIPO_ENTERO',
  'string': 'TIPO_CADENA',
  'long': 'TIPO_LARGO',
  'void': 'TIPO_VACIO',
  'char': 'TIPO_CARACTER',
  'float': 'TIPO_FLOTANTE',
  'double': 'TIPO_DOUBLE',
  'static': 'ESTATICO',
  'if': 'CONDICIONAL',
  'for': 'BUCLE_PARA',
  'while': 'BUCLE_MIENTRAS',
  'do': 'HACER',
  'return': 'RETORNAR',
  'else': 'CASO_CONTRARIO',
  'struct': 'ESTRUCTURA',
  'break': 'ROMPER'
}

t_ignore = ' \t'

#Operadores compuestos
t_MAYOR_IGUAL = r'>='
t_MENOR_IGUAL = r'<='
t_INCREMENTO = r'\+\+'
t_DECREMENTO = r'--'
t_COMPARAR_IGUAL = r'=='
t_COMPARAR_DIF = r'!='
t_AND_LOGICO_CONDICIONAL = r'&&'
t_OR_LOGICO_CONDICIONAL = r'\|\|'
t_ASIGNAR_SUMA = r'\+='
t_ASIGNAR_RESTA = r'-='
t_ASIGNAR_MULT = r'\*='
t_ASIGNAR_DIV = r'\/='
t_DIVISION_ENTERA = r'\/'

#Operadores Simples
t_ASIGNAR = r'='
t_SUMAR = r'\+'
t_RESTAR = r'-'
t_MULTIPLICAR = r'\*'
t_DIVIDIR = r'/'
t_MODULO = r'%'
t_MAYOR_QUE = r'>'
t_MENOR_QUE = r'<'
t_NEGACION = r'!'
t_AND_LOGICO = r'&'
t_OR_LOGICO = r'\|'

#palabras reservadas
t_RETORNAR = r'return'
t_CASO_CONTRARIO = r'else'
t_ESTRUCTURA = r'struct'
t_ROMPER = r'break'

#directivas
t_DIR_INCLUIR = r'\#include'
t_DIR_DEFINIR = r'\#define'
t_DIR_UNDEFINIR = r'\#undefine'

#puntuacion
t_PUNTO = r'\.'
t_PUNTO_COMA = r';'
t_COMILLA_SIMPLE = r'\''
t_COMA = r','
t_PAREN_IZQ = r'\('
t_PAREN_DER = r'\)'
t_CORCHETE_IZQ = r'\['
t_CORCHETE_DER = r'\]'
t_COMILLA_DOBLE = r'"'
t_LLAVE_IZQ = r'{'
t_LLAVE_DER = r'}'

#cadenas
t_CADENA = r'"(.*?)"'
t_CARACTER = r'\'[a-zA-Z]\''
    
def t_NUMERO_DECIMAL( t ) :
  r'\d+\.\d+'
  t.value = float( t.value )
  return t

def t_NUMERO_ENTERO( t ) :
  r'\d+'
  t.value = int( t.value )
  return t

def t_comentario_linea(t):
    r'//.*'
    pass  # Ignorar comentarios de línea

def t_comentario_bloque(t):
    r'/\*[\s\S]*?\*/'
    t.lexer.lineno += t.value.count('\n')
    pass  # Ignorar comentarios de bloque

def t_IDENTIFICADOR(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value,'IDENTIFICADOR')    # Check for reserved words
     return t

def t_newline( t ):
  r'\n+'
  t.lexer.lineno += len( t.value )

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

#Test
lexer = lex.lex()
