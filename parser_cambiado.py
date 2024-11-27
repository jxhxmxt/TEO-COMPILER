import ply.yacc as yacc
from s_lexer import *
from gramaticas.init import *

# Función para recorrer el árbol sintáctico y guardarlo en un archivo
def recorrer_arbol(nodo, archivo_arbol, level=0):
    if nodo:
        print("\t" * level, f'<{nodo.type}>', file=archivo_arbol)
        for contenido in nodo.contents:
            if isinstance(contenido, list):
                recorrer_arbol(contenido[0], archivo_arbol, level + 1)
            else:
                print("\t" * level, f"'{str(contenido)}'", file=archivo_arbol)

# Manejo de errores
def p_empty(p):
    'empty :'
    pass

def p_error(p):
    global error
    error = 1
    if p:
        print(f"Error en Sintaxis en la línea: {p.lexer.lineno} | No se esperaba '{p.value}'")
        print("\tProbando reparar con el siguiente token...\n")
        parser.errok()
    else:
        print("Error en Léxico hasta EOF, no ha sido posible recuperarse.")

# Configuración del parser
def inicializar_parser():
    return yacc.yacc()

# Función principal que maneja el análisis sintáctico
def analizar_archivo(nombre_archivo):
    with open(f'./source/{nombre_archivo}.c', 'r') as archivo:
        print("\nIniciando análisis sintáctico")
        print("----------------------------------------------------------\nERRORES:")
        
        # Analiza el contenido del archivo
        resultado = parser.parse(archivo.read())
        
        if error == 0:
            print("Ninguno")
        print("----------------------------------------------------------")
        
        if error == 0:
            generar_arbol_sintactico(nombre_archivo, resultado)
            print(f"\nÁrbol sintáctico generado en \"./resultados/Árbol sintáctico - {nombre_archivo}.txt\"")
        else:
            print('\nAnálisis sintáctico completado con errores')

# Genera el archivo con el árbol sintáctico
def generar_arbol_sintactico(nombre_archivo, resultado):
    with open(f'./resultados/Árbol sintáctico - {nombre_archivo}.txt', 'w', encoding="utf-8"):
        pass  # Crea el archivo vacío

    with open(f'./resultados/Árbol sintáctico - {nombre_archivo}.txt', 'a', encoding="utf-8") as salida:
        recorrer_arbol(resultado, salida)

# Ejecución principal
if __name__ == "__main__":
    error = 0
    parser = inicializar_parser()
    
    nombre_archivo = input("Ingrese solo el nombre del archivo .c que desea analizar\n(debe estar contenido en la carpeta 'Source'): ")
    analizar_archivo(nombre_archivo)
