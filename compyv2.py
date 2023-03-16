import ply.lex as lex
import ply.yacc as yacc
import tkinter as tk

tokens = (
    'ID',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Error de sintaxis en el token:", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()


def compilar():
    # Obtener el código fuente 
    codigo_fuente = editor.get("1.0", tk.END)

    # Llamar al lexer para generar la lista de tokens
    lexer.input(codigo_fuente)
    for token in lexer:
        print(token)



# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Compilador")

# Crear el cuadro de texto para ingresar el código fuente
editor = tk.Text(ventana)
editor.pack()

# Crear el botón "Compilar"
boton_compilar = tk.Button(ventana, text="Compilar", command=compilar)
boton_compilar.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
