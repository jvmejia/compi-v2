import sys
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
precedence = (
    ('left', 'Mas', 'Menos'),
    ('left', 'Por', 'Entre'),
)
        

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
#Crear ventana principal

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