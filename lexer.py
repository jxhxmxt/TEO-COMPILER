import ply.lex as lex
import terminals as t

terminals = t.Terminals

# region token list
tokens = (
   terminals.EOF.value,
   terminals.INT.value,
   terminals.CHAR.value,
   terminals.FLOAT.value,
   terminals.IF.value,
   terminals.ELSE.value,
   terminals.RETURN.value,
   terminals.VOID.value,
   terminals.EQUALS.value,
   terminals.ADD_OPERATOR.value,
   terminals.SUB_OPERATOR.value,
   terminals.MUL_OPERATOR.value,
   terminals.DIV_OPERATOR.value,
   terminals.AND_OPERATOR.value,
   terminals.OR_OPERATOR.value,
   terminals.NOT_OPERATOR.value,
   terminals.IDENTIFIER.value,
   terminals.NUMBER.value,
   terminals.STRING.value,
   terminals.LEFT_CURLY.value,
   terminals.RIGHT_CURLY.value,
   terminals.LEFT_PAREN.value,
   terminals.RIGHT_PAREN.value,
   terminals.SEMICOLON.value,
   terminals.INCLUDE.value,
   terminals.DEFINE.value,
   terminals.LINE_COMMENT.value,
   terminals.COMMENT_BLOCK_START.value,
   terminals.COMMENT_BLOCK_END.value,
   terminals.WHILE.value,
   terminals.COMMENT.value,
   terminals.CHARACTER.value
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
t_ignore = ' \t\r'
# endregion

# region functions for regex in terminal tokens
def t_int(t):
    r'(int)'
    return t

def t_char(t):
    r'(char)'
    return t

def t_float(t):
    r'(float)'
    return t

def t_if(t) : 
    r'(if)'
    return t

def t_else(t) : 
    r'(else)'
    return t

def t_return(t):
    r'(return)'
    return t

def t_void(t):
    r'(void)'
    return t

def t_while(t):
    r'(while)'
    return t

def t_line_comment(t):
    r'\/\/.*'
    return t

def t_comment_block_start(t):
    r'\/\*'
    return t

def t_comment_block_end(t):
    r'\*\/'
    return t

def t_add_operator(t):
    r'\+'
    return t
   
def t_sub_operator(t):
    r'\-'
    return t

def t_mul_operator(t):
    r'\*'
    return t

def t_div_operator(t):
    r'/'
    return t
    
def t_and_operator(t):
    r'\&\&'
    return t

def t_or_operator(t):
    r'\|\|'
    return t

def t_not_operator(t):
    r'\!'
    return t

def t_identifier(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_number(t):
    r'\d+(\.\d+)?'
    return t

def t_character(t):
    r"\'.*\'"
    return t

def t_string(t):
    r'\".*?\"'
    return t

def t_include(t):
    r'(\#include)'
    return t

def t_define(t):
    r'(\#define)'
    return t

def t_comment(t):
    r'//.*'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Caracter inválido '%s'" % t.value[0])
    t.lexer.skip(1)    
    return t
# endregion

lexer = lex.lex()