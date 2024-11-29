from enum import Enum

class Terminals(Enum):
    EOF = 'eof'
    INT = 'int'
    CHAR = 'char'
    FLOAT = 'float'
    IF = 'if'
    ELSE = 'else'
    RETURN = 'return'
    VOID = 'void'
    EQUALS = 'equals'
    ADD_OPERATOR = 'add_operator'
    SUB_OPERATOR = 'sub_operator'
    MUL_OPERATOR = 'mul_operator'
    DIV_OPERATOR = 'div_operator'
    AND_OPERATOR = 'and_operator'
    OR_OPERATOR = 'or_operator'
    NOT_OPERATOR = 'not_operator'
    IDENTIFIER = 'identifier'
    NUMBER = 'number'
    STRING = 'string'
    LEFT_CURLY = 'left_curly'
    RIGHT_CURLY = 'right_curly'
    LEFT_PAREN = 'left_paren'
    RIGHT_PAREN = 'right_paren'
    SEMICOLON = 'semicolon'
    INCLUDE = 'include'
    DEFINE = 'define'
    LINE_COMMENT = 'line_comment'
    COMMENT_BLOCK_START = 'comment_block_start'
    COMMENT_BLOCK_END = 'comment_block_end'
    WHILE = 'while'
    COMMENT = 'comment'
    CHARACTER = 'character'
