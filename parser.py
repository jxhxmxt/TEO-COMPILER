from s_lexer import lexer, tokens
from tablasGramaticas import (
    operationTable, SOpe, ZOpe, AOpe, BOpe, COpe, DOpe,
    SIfElse, AIfElse, BIfElse, CIfElse, ifElseTable,
    SWhile, whileTable,
    SVar, AVar, BVar, CVar, DVar, EVar, FVar, GVar, HVar, IVar, JVar, STipos, varFuncTable,
)
# Definir SAll y asignar un número único
SAll = 100

# Crear la tabla para SAll
allTable = [
    [SAll, 'BUCLE_MIENTRAS', [SWhile]],
    [SAll, 'CONDICIONAL', [SIfElse]],
    [SAll, 'TIPO_ENTERO', [SVar]],
    [SAll, 'TIPO_CADENA', [SVar]],
    [SAll, 'TIPO_LARGO', [SVar]],
    [SAll, 'TIPO_VACIO', [SVar]],
    [SAll, 'TIPO_CARACTER', [SVar]],
    [SAll, 'TIPO_FLOTANTE', [SVar]],
    [SAll, 'TIPO_DOUBLE', [SVar]],
    [SAll, 'IDENTIFICADOR', [SVar]],
    # Agregar más producciones según sea necesario
]

class Parser:
    def __init__(self, lexer, tokens, start_symbol):
        self.lexer = lexer
        self.tokens = tokens
        self.start_symbol = start_symbol
        self.stack = ['eof', self.start_symbol]
        self.tok = None
        self.x = None

        # Mapeo de no terminales a sus tablas de parsing
        self.non_terminal_table_mapping = {
            # Operaciones aritméticas
            SOpe: operationTable,
            ZOpe: operationTable,
            AOpe: operationTable,
            BOpe: operationTable,
            COpe: operationTable,
            DOpe: operationTable,
            # if-else
            SIfElse: ifElseTable,
            AIfElse: ifElseTable,
            BIfElse: ifElseTable,
            CIfElse: ifElseTable,
            # Variables y funciones
            SVar: varFuncTable,
            AVar: varFuncTable,
            BVar: varFuncTable,
            CVar: varFuncTable,
            DVar: varFuncTable,
            EVar: varFuncTable,
            FVar: varFuncTable,
            GVar: varFuncTable,
            HVar: varFuncTable,
            IVar: varFuncTable,
            JVar: varFuncTable,
            STipos: varFuncTable,
            # Bucle while
            SWhile: whileTable,
            # Símbolo inicial general
            SAll: allTable,
        }

    def parse(self, input_string):
        self.lexer.input(input_string)
        self.tok = self.next_token()
        self.x = self.stack[-1]
        success = self.parser_gen()
        if success:
            print("Cadena reconocida exitosamente")
        else:
            print("Se encontraron errores durante el análisis sintáctico.")

    def next_token(self):
        tok = self.lexer.token()
        if tok is None:
            # Crear un token 'eof' personalizado
            tok = type('Token', (object,), {'type': 'eof', 'value': '', 'lexpos': self.lexer.lexpos})
        return tok

    def parser_gen(self):
        while True:
            print("TOKEN:", self.tok.type)
            print("X:", self.x)
            if self.x == self.tok.type and self.x == 'eof':
                # Aceptar
                return True
            elif self.x == self.tok.type:
                # Coincidencia terminal, avanzar
                print('* Eliminando token:', self.x)
                self.stack.pop()
                self.tok = self.next_token()
                if not self.stack:
                    return False  # Error: Pila vacía antes de terminar
                self.x = self.stack[-1]
            elif self.x in self.tokens:
                # Error sintáctico
                print(f"Error: Se esperaba '{self.x}' pero se encontró '{self.tok.type}' en la posición {self.tok.lexpos}")
                return False
            else:
                # Es un no terminal
                production = self.buscar_en_tabla(self.x, self.tok.type)
                if production is None:
                    print(f"Error: No se esperaba '{self.tok.type}' después de '{self.x}' en la posición {self.tok.lexpos}")
                    return False
                else:
                    print(f"Aplicando producción: {self.x} -> {production}")
                    self.stack.pop()
                    self.agregar_pila(production)
                    if not self.stack:
                        return False  # Error: Pila vacía antes de terminar
                    self.x = self.stack[-1]
            print("Pila actual:", self.stack)
            print('------------------------------------------------------------------')

    def buscar_en_tabla(self, no_terminal, terminal):
        # Obtener la tabla de parsing correspondiente al no terminal
        tabla = self.non_terminal_table_mapping.get(no_terminal)
        if tabla is None:
            return None
        # Buscar la producción correspondiente
        for fila in tabla:
            if fila[0] == no_terminal and fila[1] == terminal:
                return fila[2]
        return None

    def agregar_pila(self, produccion):
        for elemento in reversed(produccion):
            if elemento != 'vacia':  # No agregar producciones vacías
                self.stack.append(elemento)

def main():

    # Símbolo inicial
    start_symbol = SAll  # Usar SAll como símbolo inicial general

    # Crear instancia del parser
    parser = Parser(lexer, tokens, start_symbol)

    # Leer el archivo de entrada
    with open('./source/ExampleCError.c', 'r') as f:
        input_string = f.read()

    # Ejecutar el parser
    parser.parse(input_string)

if __name__ == "__main__":
    main()
