import ply.lex as lex
import ply.yacc as yacc
import tkinter as tk
from tkinter import filedialog
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

#PASER
lexer = lex.lex()


def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_divide(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_number(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_group(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    print("Error de sintaxis en la entrada:", p)

parser = yacc.yacc()
def compilar():
    # Obtener el código fuente 
    codigo_fuente = editor.get("1.0", tk.END)

    # Llamar al lexer para generar la lista de tokens
    lexer.input(codigo_fuente)
    for token in lexer:
        print(token)


# Definir la función de compilación
def compilar():
    # Obtener el código fuente del editor
    codigo_fuente = editor.get("1.0", tk.END)
    
    # Limpiar el cuadro de errores y la ventana de resultados
    errores.config(text="")
    resultado.delete("1.0", tk.END)
    
    # Compilar el código fuente
    try:
        ast = parser.parse(codigo_fuente)
        resultado.insert(tk.END, "Compilación exitosa.\n")
        resultado.insert(tk.END, str(ast))
    except Exception as e:
        errores.config(text=str(e))

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Compilador")
ventana.geometry("800x600")

# Crear el widget de edición
editor = tk.Text(ventana, font=("Consolas", 12))
editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Crear el widget de resultados
resultado = tk.Text(ventana, font=("Consolas", 12))
resultado.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Crear la barra de herramientas
barra_herramientas = tk.Frame(ventana, bd=1, relief=tk.RAISED)
abrir_boton = tk.Button(barra_herramientas, text="Abrir", command=lambda: abrir_archivo(editor))
guardar_boton = tk.Button(barra_herramientas, text="Guardar", command=lambda: guardar_archivo(editor))
compilar_boton = tk.Button(barra_herramientas, text="Compilar", command=compilar)
abrir_boton.pack(side=tk.LEFT, padx=2, pady=2)
guardar_boton.pack(side=tk.LEFT, padx=2, pady=2)
compilar_boton.pack(side=tk.LEFT, padx=2, pady=2)
barra_herramientas.pack(side=tk.TOP, fill=tk.X)

# Crear la barra de estado
barra_estado = tk.Label(ventana, text="Listo", bd=1, relief=tk.SUNKEN, anchor=tk.W)
barra_estado.pack(side=tk.BOTTOM, fill=tk.X)

# Crear el cuadro de diálogo de errores
errores = tk.Label(ventana, text="", fg="red")
errores.pack(side=tk.BOTTOM, fill=tk.X)

# Crear el lexer y el parser
lexer = lex.lex()
parser = yacc.yacc()

# Definir funciones para abrir y guardar archivos
def abrir_archivo(editor):
    archivo = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
    if archivo:
        editor.delete("1.0", tk.END)
        with open(archivo, "r") as archivo_fuente:
            editor.insert(tk.END, archivo_fuente.read())

def guardar_archivo(editor):
    archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
    if archivo:
        with open(archivo, "w") as archivo_fuente:
            archivo
            codigo_fuente = editor.get("1.0", tk.END)
            archivo_fuente.write(codigo_fuente)

ventana.mainloop()
