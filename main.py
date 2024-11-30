from tabulate import tabulate
import grammar_rules
import lexer
import non_terminals as nonTerminals
import terminals
from enum import Enum

# Definición de los no terminales y terminales
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

non_terminal_node_types = {
    nt.PROGRAM.value: NodeType.PROGRAM,
    nt.FUNCTION.value: NodeType.FUNCTION,
    nt.FUNC_BODY.value: NodeType.CODE_BLOCK,
    nt.DECLARATION.value: NodeType.VARIABLE,
    nt.DECLARATION_BODY.value: NodeType.VARIABLE,
    nt.STATEMENT.value: NodeType.CODE_BLOCK,
    nt.EXPRESSION.value: NodeType.CODE_BLOCK,
    nt.EXPRESSION_ALT.value: NodeType.CODE_BLOCK,
    nt.TERM.value: NodeType.CODE_BLOCK,
    nt.TERM_ALT.value: NodeType.CODE_BLOCK,
    nt.FACTOR.value: NodeType.CODE_BLOCK,
    nt.CONDITIONAL.value: NodeType.CONDITIONAL,
    nt.CONDITIONAL_ALT.value: NodeType.CONDITIONAL,
    nt.ASSIGNMENT.value: NodeType.ASSIGNMENT_OPERATOR,
    nt.DATA_TYPE.value: NodeType.DATA_TYPE,
    nt.COMMENT.value: NodeType.COMMENT,
    nt.MACRO.value: NodeType.MACROS,
    nt.COMPOUND_STATEMENT.value: NodeType.CODE_BLOCK,
    nt.WHILE_STATEMENT.value: NodeType.LOOP,
}

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
    if token in non_terminal_node_types:
        return non_terminal_node_types[token]
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

# estado inicial de la pila y la pila de árboles
stack = [t.EOF.value, nt.PROGRAM.value]
rules = grammar_rules.derivations
tree_stack = []

def read_file():
    f = open('source.c','r')
    f.seek(0)
        
    # Carga el código fuente en el lexer y agrega un token de fin de archivo.
    c_lexer.input(f.read() + '$')

def tlpParser():
    in_error = False 
    not_found_terminals = []

    read_file()

    # Obten el primer token generado por el lexer
    token=c_lexer.token()
    
    # Toma el último elemento de la pila (el tope) como elemento actual para operar.
    stack_element=stack[-1] 
    
    # Bucle principal del parser.
    while True:
        # Caso: Token final detectado y coincide con el elemento de la pila.
        if stack_element == token.type and stack_element == t.EOF.value:
            if (len(errors) == 0):
                print("C language code loaded successfully!")
            return
        
        # Caso: El token actual es un terminal y coincide con el tope de la pila.
        elif stack_element in tokens and stack_element == token.type and stack_element != t.EOF.value:
            print(f"Stak element: {stack_element} - Token: {token.type}")
            # Crea un nodo de árbol para este token y lo almacena.
            node = SyntaxTreeNode(get_node_type(token.type), token.value)
            tree_stack.append(node)
            
            # Elimina el elemento de la pila y avanza al siguiente token.
            stack.pop()
            stack_element=stack[-1]
            token=c_lexer.token()

            # Resetea errores y terminales no encontrados.
            not_found_terminals = []
            in_error = False
        
        # Caso: El token actual es un terminal, pero no coincide con el tope de la pila.             
        elif stack_element in tokens and stack_element != token.type:
            # Crea un nodo para el token y lo almacena.
            node = SyntaxTreeNode(get_node_type(token.type), token.value)
            tree_stack.append(node)
            
            # Avanza al siguiente token del lexer.
            token=c_lexer.token()
            
            # Si el token actual no está en la pila y no se han encontrado más de dos terminales, almacena el token actual.
            if token.type in tokens and len(not_found_terminals) <= 2:
                not_found_terminals.append(token.type)
            elif in_error == False:                    
                in_error = True
                if stack_element is not t.EOF.value:
                    message = f"Error: token {stack_element} in line {token.lineno} at POSITION {token.lexpos} was expected."
                    errors.append(message)
            continue
        
        # Caso: El elemento actual de la pila no es un terminal y no está en la lista de tokens.
        elif stack_element not in tokens:
            # Verifica si debe ignorar el token según reglas específicas.
            if should_ignore_token(stack_element, token.type):
                node = SyntaxTreeNode(get_node_type(token.type), token.value)
                tree_stack.append(node)
                token=c_lexer.token()
            
            # Busca una regla gramatical para derivar el no terminal actual.
            grammar_production=get_derivation(stack_element, token.type)                            
            if  grammar_production is None:
                # Si no se encuentra una regla válida, registra un error y termina.
                message = f"Error: token {token.type} in line {token.lineno} at POSITION {token.lexpos} was NOT expected." 
                errors.append(message)
                print("Grammar rule is not defined for this action. Aborting...")
                return 0
            else:
                # Si la regla es válida, crea un nodo en el árbol para el no terminal.
                if could_generate_tree_node(stack_element, token.type):
                    node = SyntaxTreeNode(get_node_type(stack_element), None)
                    for _ in grammar_production:
                        if len(tree_stack) > 0:
                            child = tree_stack.pop()
                            node.add_child(child)
                    tree_stack.append(node)

                # Actualiza la pila con los nuevos elementos de la producción.                     
                stack.pop()
                append_stack(grammar_production)
                stack_element=stack[-1]
                
                # Resetea errores y terminales no encontrados.
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

def check_type_compatibility(expected_type, value):
    """
    Función para verificar la compatibilidad de tipos entre la variable declarada
    y el valor asignado, diferenciando entre enteros y flotantes.
    """
    if expected_type == 'int':
        try:
            # Intentamos convertir el valor a float primero para verificar si es un número
            float_value = float(value)
            # Si el valor convertido es un entero, lo devolvemos como int
            if float_value.is_integer():
                return True
            else:
                # Si tiene decimales, no es un entero
                return False
        except ValueError:
            return False  # Si no se puede convertir a número, es un error de tipo
    
    elif expected_type == t.FLOAT.value:
        try:
            # Verificar si el valor es un flotante válido
            float_value = float(value)
            return True  # Siempre es válido como float (incluso si es un número entero como 2.0)
        except ValueError:
            return False  # Si no se puede convertir a float, es un error de tipo
    
    elif expected_type == t.CHAR.value:
        # Verificar que el valor sea un solo carácter y es de tipo string
        if isinstance(value, str) and len(value) == 1:
            return True
        else:
            return False
    
    elif expected_type == t.STRING.value:
        # Los strings siempre son compatibles con el tipo string
        return isinstance(value, str)

    return False  # Si no es uno de los tipos esperados, es incompatible

def add_to_symbol_table(token, current_type, current_value=None):
    """
    Modificada para incluir la validación semántica de tipo de datos
    al momento de hacer asignaciones.
    """
    keys = list(symbol_table.keys())
    if token.type == t.IDENTIFIER.value:
        identifier = token.value
        if identifier not in symbol_table:
            symbol_table[identifier] = {
                
                'type': current_type,
                'value': current_value,
                'scope': scope_stack[-1]
            }
        elif((identifier in symbol_table) and (current_type != None)):
            errors.append(f"Error semántico: el identificador {identifier} ya ha sido declarado.")
    elif (len(keys) > 0) and (token.type == t.NUMBER.value or token.type == t.STRING.value or token.type == t.CHARACTER.value) and (not symbol_table[keys[-1]]['value']):
        last_identifier = list(symbol_table.keys())[-1]
        symbol_table[last_identifier]['value'] = token.value
        if token.type == t.NUMBER.value:
            # Si es un número, convertirlo a float o int según el tipo esperado
            value_to_check = float(token.value)  # Se convierte a float, ya que los números pueden ser decimales
        elif token.type == t.STRING.value:
            value_to_check = token.value[1:-1]  # Eliminar las comillas de un string
        elif token.type == t.CHARACTER.value:
            value_to_check = token.value[1:-1]
        # Validar tipo de asignación en la declaración
        if  check_type_compatibility(current_type, value_to_check) == False:
            
            errors.append(f"Error semántico: tipo incompatible en la asignación de valor {token.value} a {current_type}.")
    
    elif (len(keys) > 0) and token.type == t.STRING.value:
        last_identifier = keys[-1]
        if symbol_table[last_identifier]['value'] is None:
            symbol_table[last_identifier]['value'] = token.value[1:-1]

# Ejecucion del Parser 
tlpParser()

# Tabla de símbolos
symbol_table = {}
current_value = None
tokens_found = []
scope_stack = [0]
    
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


print()
red = '\033[91m'
white = '\033[97m' 
for error in errors:
    print(red + error)
print(white)

print_symbol_table()
print()

print("Arbol de análisis sintáctico:")
for node in tree_stack:
    print_tree(node)