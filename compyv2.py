
import ply.lex as lex
import ply.yacc as yacc
import tkinter as tk
from tkinter import filedialog
# Definimos los tokens
tokens = (
    'NOMBRE',
    'NUMERO',
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'PARENTESIS_IZQ',
    'PARENTESIS_DER',
    'ASIGNACION',
    'SI',
    'SINO',
    'MIENTRAS',
    'DOS_PUNTOS',
    'INDENTACION',
    'DEDENTACION'
)

# Tokens
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_ASIGNACION = r'='
t_DOS_PUNTOS = r':'

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Nueva línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Asignar nombres a variables
def t_NOMBRE(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value == 'si':
        t.type = 'SI'
    elif t.value == 'sino':
        t.type = 'SINO'
    elif t.value == 'mientras':
        t.type = 'MIENTRAS'
    return t

# Asignar valores numéricos a variables
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Manejar comentarios
def t_COMENTARIO(t):
    r'\#.*'
    pass

# Manejar errores de sintaxis
def t_error(t):
    print("Carácter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir lexer
lexer = lex.lex()

# Definir reglas de gramática
def p_statement_asignacion(p):
    'statement : NOMBRE ASIGNACION expression'
    p[0] = ('ASIGNACION', p[1], p[3])

def p_statement_expr(p):
    'statement : expression'
    p[0] = ('EXPR', p[1])

def p_expression_binop(p):
    '''expression : expression SUMA expression
                  | expression RESTA expression
                  | expression MULTIPLICACION expression
                  | expression DIVISION expression'''
    p[0] = ('BINOP', p[2], p[1], p[3])

def p_expression_numero(p):
    'expression : NUMERO'
    p[0] = ('NUMERO', p[1])

def p_expression_nombre(p):
    'expression : NOMBRE'
    p[0] = ('NOMBRE', p[1])

def p_statement_si(p):
    'statement : SI expression DOS_PUNTOS INDENTACION statement DEDENTACION'
    p[0] = ('SI', p[2], p[5])

def p_statement_si_sino(p):
    'statement : SI expression DOS_PUNTOS INDENTACION statement DEDENTACION SINO DOS_PUNTOS INDENTACION statement DEDENTACION'
    p[0] = ('SI_SINO', p[2], p[5], p[10])
def p_statement_mientras(p):
    'statement : MIENTRAS expression DOS_PUNTOS INDENTACION statement DEDENTACION'
    p[0] = ('MIENTRAS', p[2], p[5])

def p_statement_mientras_error(p):
    'statement : MIENTRAS DOS_PUNTOS error DEDENTACION'
    print("Error de sintaxis en la estructura de control mientras")

def p_statement_error(p):
    'statement : error'
    print("Error de sintaxis en la expresión")
def p_error(p):
    print("Error de sintaxis en la expresión")

parser = yacc.yacc()

root = tk.Tk()
root.title("Analizador Sintáctico")
#Función para abrir archivo de entrada

def abrir_archivo():
    file_path = filedialog.askopenfilename()
    with open(file_path) as file:
# Leer archivo y ejecutar análisis sintáctico
     input_str = file.read()
    parser.parse(input_str)
#Crear botón para abrir archivo

abrir_btn = tk.Button(root, text="Abrir archivo", command=abrir_archivo)
abrir_btn.pack()
#Etiqueta para mostrar resultados

result_label = tk.Label(root, text="")
result_label.pack()
#Función para mostrar resultados

def mostrar_resultados(result):
    result_label.configure(text=result)

parser = yacc.yacc()
lexer = lex.lex()
#Función para ejecutar análisis sintáctico

def analizar():
    codigo_fuente = editor.get("1.0", tk.END)
    # Ejecutar análisis sintáctico
    try:
        parser.parse(codigo_fuente)
        mostrar_resultados("Análisis completado")  # Nueva línea
    except Exception as e:
        mostrar_resultados(f"Error de sintaxis: {e}")
#Crear botón para ejecutar análisis sintáctico

analizar_btn = tk.Button(root, text="Analizar", command=analizar)
analizar_btn.pack()
#Crear cuadro de texto para ingresar código

editor = tk.Text(root, height=20, width=50)
editor.pack()
#Iniciar loop de la interfaz gráfica

root.mainloop()