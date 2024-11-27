import ply.lex as lex
import terminals as t

terminals = t.Terminals

# region token list
tokens = (
   terminals.INT.value,
   terminals.CHAR.value,
   terminals.FLOAT.value,
   terminals.STRING.value,
   terminals.IDENTIFIER.value,
   terminals.IF.value,
   terminals.ELSE.value,
   terminals.GREATER_THAN.value,
   terminals.ADD_EQ.value,
   terminals.SUB_EQ.value,
   terminals.MUL_EQ.value,
   terminals.DIV_EQ.value,
   terminals.WHILE.value,
   terminals.LEFT_PAREN.value,
   terminals.RIGHT_PAREN.value,
   terminals.LEFT_CURLY.value,
   terminals.RIGHT_CURLY.value,
   terminals.SEMICOLON.value,
   terminals.EQUALS.value,
   terminals.STRUCT.value,
   terminals.NUMBER.value,
   terminals.COMMENT.value,
   terminals.EOF.value
)
# endregion

# region regex list for lexer
t_left_paren = r'\('
t_right_paren = r'\)'
t_left_curly = r'\{'
t_right_curly = r'\}'
t_semicolon = r'\;'
t_equals = r'\='
t_eof = r'\$'
t_greater_than = r'\>'
t_ignore  = ' \t'
# endregion

# region functions for regex in terminal tokens
def t_int(t):
    r'(int)'
    return t

def t_float(t):
    r'(float)'
    return t

def t_char(t):
    r'(char)'
    return t

def t_if(t) : 
    r'(if)'
    return t

def t_else(t) : 
    r'(else)'
    return t

def t_struct(t) : 
    r'(struct)'
    return t

def t_add_eq(t) : 
    r'\+='
    return t

def t_mul_eq(t) : 
    r'\*='
    return t

def t_sub_eq(t) : 
    r'\-='
    return t

def t_div_eq(t) : 
    r'\/='
    return t

def t_while(t) : 
    r'(while)'
    return t

def t_number(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_keyword(t):
    r'(return)|(if)|(else)|(do)|(while)|(for)|(void)'
    return t

def t_identifier(t):
    r'([a-z]|[A-Z]|_)([a-z]|[A-Z]|\d|_)*'
    return t

def t_string(t):
    r'\".*\"'
    return t

def t_comment(t):
    r'\/\/.*'
    return t

def t_comentario_bloque(t):
    r'\/\*(.|\n)*\*\/'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)    
    return t
# endregion

lexer = lex.lex()