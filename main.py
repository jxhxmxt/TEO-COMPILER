from tabulate import tabulate
import grammar_rules
import lexer
import non_terminals as nonTerminals
import terminals
from enum import Enum

# general definitions section
nt = nonTerminals.NonTerminals
t = terminals.Terminals
c_lexer = lexer.lexer
tokens = lexer.tokens
errors = []
    
class NodeType(Enum):
    DATA_TYPE = 'Data type'
    PROGRAM = 'Program'
    IDENTIFIER = 'Identifier'
    LITERALS = 'Literal'
    ARITHMETIC_OPERATOR = 'Arithmetic operator'
    ASSIGNMENT_OPERATOR = 'Assignment operator'
    LOGICAL_OPERATOR = 'Logical operator'
    COMPARISON_OPERATOR = 'Comparison operator'
    CONDITIONAL = 'Conditional'
    LOOP = 'Loop'
    FUNCTION = 'Function'
    VARIABLE = 'Variable declaration'
    CODE_BLOCK = 'Code block'
    COMMENT = 'Comment'
    MACROS  = 'Macros'
    
data_types = [t.INT.value, t.CHAR.value, t.FLOAT.value, t.VOID.value, nt.DATA_TYPE.value]
arithmetic_operators = [t.ADD_OPERATOR.value, t.SUB_OPERATOR.value, t.MUL_OPERATOR.value, t.DIV_OPERATOR.value]
comment = [t.COMMENT.value, t.COMMENT_BLOCK_START.value, t.COMMENT_BLOCK_END.value, t.LINE_COMMENT.value, nt.COMMENT.value]
logical_operators  = [t.AND_OPERATOR.value, t.OR_OPERATOR.value, t.NOT_OPERATOR.value]
delimeters = [t.LEFT_CURLY.value, t.RIGHT_CURLY.value, t.RIGHT_PAREN.value, t.LEFT_PAREN.value ]
functions  = [nt.FUNCTION.value, nt.FUNC_BODY.value]
variables = [t.SEMICOLON.value, t.IDENTIFIER.value, nt.DECLARATION.value, nt.DECLARATION_BODY.value]
macros = [t.INCLUDE.value, t.DEFINE.value, nt.MACRO.value]
generals = [t.EOF.value, nt.PROGRAM.value, nt.STATEMENT.value, nt.EXPRESSION.value, nt.EXPRESSION_ALT.value, nt.TERM.value, nt.TERM_ALT.value, nt.FACTOR.value, nt.COMPOUND_STATEMENT.value]
returns = [t.RETURN.value]
assignment = [t.EQUALS.value, nt.ASSIGNMENT.value]
loops = [t.WHILE.value, nt.WHILE_STATEMENT.value]
literals = [t.NUMBER.value, t.STRING.value, t.CHARACTER.value ]
conditional = [t.IF.value, t.ELSE.value, nt.CONDITIONAL.value, nt.CONDITIONAL_ALT.value]

tree_node_generators = [
    [nt.DECLARATION.value, t.CHAR.value],
    [nt.DECLARATION.value, t.FLOAT.value],
    [nt.DECLARATION_BODY.value, t.SEMICOLON.value],
    [nt.DECLARATION_BODY.value, t.EQUALS.value],
]

def get_node_type(token):
    if token in data_types:
        return NodeType.DATA_TYPE
    if token in arithmetic_operators:
        return NodeType.ARITHMETIC_OPERATOR
    if token in comment:
        return NodeType.COMMENT
    if token in logical_operators:
        return NodeType.LOGICAL_OPERATOR
    if token in delimeters:
        return NodeType.CODE_BLOCK
    if token in functions:
        return NodeType.FUNCTION
    if token in variables:
        return NodeType.VARIABLE
    if token in macros:
        return NodeType.MACROS
    if token in generals:
        return NodeType.CODE_BLOCK
    if token in returns:
        return NodeType.CODE_BLOCK
    if token in assignment:
        return NodeType.ASSIGNMENT_OPERATOR
    if token in loops:
        return NodeType.LOOP
    if token in literals:
        return NodeType.LITERALS
    if token in conditional:
        return NodeType.CONDITIONAL
    return NodeType.CODE_BLOCK

class SyntaxTreeNode:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def print_tree(node, indent=0):
    arrow = " |-node → "
    print("|   " * indent + arrow + f" {node.type.value }: {node.value} ")

    for child in node.children:
        print_tree(child, indent + 1)

def should_ignore_token(stack_element, token):
    if (stack_element == nt.STATEMENT.value and (token == t.LEFT_CURLY.value or token == t.ELSE.value)):
        return True
    if (stack_element == nt.EXPRESSION.value and (token == t.EQUALS.value or token == t.CHARACTER.value)):
        return True
    if (stack_element == nt.EXPRESSION_ALT.value and (token == t.NUMBER.value or token == t.IDENTIFIER.value)):
        return True
    if (stack_element == nt.TERM.value and token == t.ADD_OPERATOR.value):
        return True
    if (stack_element == nt.EXPRESSION_ALT.value and token in arithmetic_operators):
        return True
    return False

# initial state for stack and grammar rules for parser
stack = [t.EOF.value, nt.PROGRAM.value]
rules = grammar_rules.derivations
tree_stack = []

def read_file():
    f = open('source.c','r')
    f.seek(0)
        
    # Adding end of file character at the end of the C language code
    c_lexer.input(f.read() + '$')

def tlpParser():
    in_error = False 
    not_found_terminals = []

    read_file()
    # Get the next token detected by the lexer
    token=c_lexer.token()
    
    # Retrieve the last element from the stack to operate with
    stack_element=stack[-1] 
    
    # Recursive algorithm for parser
    while True:
        # If the token for the end of the code has been reached
        if stack_element == token.type and stack_element == t.EOF.value:
            if (len(errors) == 0):
                print("C language code loaded successfully!")
            return
        else:
            # We got a terminal token and matches the stack element
            if stack_element in tokens and stack_element == token.type and stack_element != t.EOF.value:
                node = SyntaxTreeNode(get_node_type(token.type), token.value)
                tree_stack.append(node)
                
                stack.pop()
                stack_element=stack[-1]
                token=c_lexer.token()
                not_found_terminals = []
                in_error = False
            # We got a terminal token but is not the same for the stack element             
            if stack_element in tokens and stack_element != token.type:
                node = SyntaxTreeNode(get_node_type(token.type), token.value)
                tree_stack.append(node)
                
                token=c_lexer.token()
                # If token is also a terminal we don't throw the difference as an error, just continue with the procedure                               
                if token.type in tokens and len(not_found_terminals) <= 2:
                    not_found_terminals.append(token.type)
                elif in_error == False:                    
                    in_error = True
                    if stack_element is not t.EOF.value:
                        message = f"Error: token {stack_element} in line {token.lineno} at POSITION {token.lexpos} was expected."
                        errors.append(message)
                continue
            # If the element from the stack is a non-terminal token then we use grammar rules
            if stack_element not in tokens:
                # Special cases to pop a token from lexer
                if should_ignore_token(stack_element, token.type):
                    node = SyntaxTreeNode(get_node_type(token.type), token.value)
                    tree_stack.append(node)
                    token=c_lexer.token()
                
                
                grammar_production=get_derivation(stack_element, token.type)                            
                if  grammar_production is None:
                    message = f"Error: token {token.type} in line {token.lineno} at POSITION {token.lexpos} was NOT expected." 
                    errors.append(message)
                    print(f"Grammar rule is not defined for this action. Aborting...")
                    return 0
                else:
                    if could_generate_tree_node(stack_element, token.type) and False:                    
                        node = SyntaxTreeNode(get_node_type(token.type), token.value)
                        modified = grammar_production
                        for c in  modified:
                            if len(tree_stack) > 0:
                                child = tree_stack.pop()
                                node.add_child(child)
                        tree_stack.append(node)
                                         
                    stack.pop()
                    append_stack(grammar_production)
                    stack_element=stack[-1]
                    not_found_terminals = []
                    in_error = False
        print("Stack: ", stack)
        print()
        print("------------------------------------------")
        print()

def get_derivation(nt_token, t_token):
    print(f"Searching grammar rule {nt_token} -> {t_token}") 
    for i in range(len(rules)):
        if rules[i][0] == nt_token and rules[i][1] == t_token:
            return rules[i][2] 

def could_generate_tree_node(nt_token, t_token):
    for i in range(len(tree_node_generators)):
        if tree_node_generators[i][0] == nt_token and tree_node_generators[i][1] == t_token:
            return True
    return False

def append_stack(production):
    for element in reversed(production):
        stack.append(element)

# Ejecucion del Parser 
tlpParser()

print()
red = '\033[91m'
white = '\033[97m' 
for error in errors:
    print(red + error)
print(white)

# Symbols table variables and functions
symbol_table = {}
current_value = None
tokens_found = []
scope_stack = [0]

def add_to_symbol_table(token, current_type, current_value=None):
    keys = list(symbol_table.keys())
    if token.type == t.IDENTIFIER.value:
        identifier = token.value
        if identifier not in symbol_table:
            symbol_table[identifier] = {
                'type': current_type,
                'value': current_value,
                'scope': scope_stack[-1]
            }
    elif (len(keys) > 0) and (token.type == t.NUMBER.value or token.type == t.STRING.value or token.type == t.CHARACTER.value) and (not symbol_table[keys[-1]]['value']):
        last_identifier = list(symbol_table.keys())[-1]
        symbol_table[last_identifier]['value'] = token.value
    elif (len(keys) > 0) and token.type == t.STRING.value:
        last_identifier = keys[-1]
        if symbol_table[last_identifier]['value'] is None:
            symbol_table[last_identifier]['value'] = token.value[1:-1]

def update_symbol(identifier, new_type=None, new_value=None):
    if identifier in symbol_table:
        if new_type is not None:
            symbol_table[identifier]['type'] = new_type
        if new_value is not None:
            symbol_table[identifier]['value'] = new_value

def delete_symbol(identifier):
    if identifier in symbol_table:
        del symbol_table[identifier]

def search_symbol(identifier):
    if identifier in symbol_table:
        return symbol_table[identifier]
    else:
        return None
    
def build_symbol_table():
    read_file()
    current_type = None
    
    for token in c_lexer:
        if token.type != t.COMMENT.value:
            if (token.type == t.INT.value or token.type == t.CHAR.value or token.type == t.STRING.value or token.type == t.FLOAT.value):
                current_type = token.value
            elif token.type == t.SEMICOLON.value :
                current_type = None
            tokens_found.append((token.type, token.value))
            add_to_symbol_table(token, current_type)

            # Actualizar el ámbito al encontrar una apertura de bloque
            if token.type == t.LEFT_CURLY.value:
                scope_stack.append(scope_stack[-1] + 1)

            # Disminuir el ámbito al encontrar un cierre de bloque
            elif token.type == t.RIGHT_CURLY.value:
                scope_stack.pop()

# Mostrar la tabla de símbolos con tipo de dato, valor y ámbito
def print_symbol_table():
    print("\nSYMBOLS TABLE:")
    symbol_table_data = []
    for identifier, data in symbol_table.items():
        symbol_table_data.append([identifier, data['type'], data['value'], data['scope']])

    headers = ["Identifier", "Data type", "Value", "Scope"]
    print(tabulate(symbol_table_data, headers, tablefmt="fancy_grid"))

build_symbol_table()
print_symbol_table()
print()

print("Arbol de análisis sintáctico:")
for node in tree_stack:
    print_tree(node)

# Por si se necesita mostrar en la defensa
# print('actualizar')
# update_symbol('var', new_type='char', new_value='l')
# print_symbol_table()

# print('eliminar')
# delete_symbol('b')
# print_symbol_table()

# print('buscar')
# result = search_symbol('c')
# print(result)