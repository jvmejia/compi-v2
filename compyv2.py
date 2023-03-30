import ply.lex as lex
import ply.yacc as yacc
import tkinter as tk
from tkinter import filedialog
reservadas = ['INICIO','FIN','Si','entonces','mientras','hacer','const','var','print']

tokens = reservadas+['ID','Numero','Mas','Menos','Por','Entre','Coma','Punto','Asigna','Dif','Menor','Mayor','Menorigual','Mayorigual','izpar','derpar','puntocoma']

t_Mas=r'\+'
t_Asigna=r'='
t_Menos=r'\-'
t_Por=r'\*'
t_Entre=r'/'
t_Coma=r'\,'
t_Punto=r'\.'
t_Dif=r'<>'
t_Menor=r'<'
t_Mayor=r'>'
t_Menorigual=r'<='
t_Mayorigual=r'>='
t_izpar=r'\('
t_derpar=r'\)'
t_puntocoma=r';'


def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value.upper() in reservadas:
		t.value = t.value.upper()
		t.type = t.value
	return t
def t_Numero(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)
def t_error(t):
	print ("caracter ilegal '%s'" %t.value[0])
	t.lexer.skip(1)
        

# Definición de gramática
def p_programa(p):
    '''programa : INICIO cuerpo FIN'''
    pass
def p_expresion_decimal(p):
    '''
    expresion : Numero Punto Numero
    '''
    p[0] = float(str(p[1]) + '.' + str(p[3]))

def p_cuerpo(p):
    '''cuerpo : lista_declaraciones'''
    pass

def p_lista_declaraciones(p):
    '''lista_declaraciones : lista_declaraciones declaracion
                           | declaracion'''
    pass

def p_declaracion(p):
    '''declaracion : tipo lista_variables puntocoma'''
    pass

def p_tipo(p):
    '''tipo : const
            | var'''
    pass

def p_lista_variables(p):
    '''lista_variables : lista_variables Coma ID
                       | ID'''
    pass

def p_sentencia(p):
    '''sentencia : asignacion
                 | estructura_control
                 | escritura'''
    pass

def p_asignacion(p):
    '''asignacion : ID Asigna expresion puntocoma'''
    pass

def p_estructura_control(p):
    '''estructura_control : sentencia_if
                          | sentencia_while'''
    pass

def p_sentencia_if(p):
    '''sentencia_if : Si condicion entonces cuerpo FIN'''
    pass

def p_sentencia_while(p):
    '''sentencia_while : mientras condicion hacer cuerpo FIN'''
    pass

def p_condicion(p):
    '''condicion : expresion comparador expresion'''
    pass

def p_comparador(p):
    '''comparador : Menor
                  | Mayor
                  | Menorigual
                  | Mayorigual
                  | Dif'''
    pass

def p_expresion(p):
    '''expresion : expresion Mas expresion
                 | expresion Menos expresion
                 | expresion Por expresion
                 | expresion Entre expresion
                 | ID
                 | Numero
                 | izpar expresion derpar'''
    pass

def p_escritura(p):
    '''escritura : print izpar expresion derpar puntocoma'''
    pass

def p_error(p):
    print("Error de sintaxis en '%s'" % p.value)

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
