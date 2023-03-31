import ply.lex as lex
import ply.yacc as yacc
import tkinter as tk

# Definir tokens
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
    'DEDENTACION',
)

# Expresiones regulares para tokens
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_ASIGNACION = r'='
t_DOS_PUNTOS = r':'

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejar saltos de línea
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

def p_error(p):
    print("Error de sintaxis en '%s'" % p.value)

parser = yacc.yacc()

class CompilerApp:
    def init(self, master):
        self.master = master
        master.title("Compilador")



        self.label = tk.Label(master, text="Ingresa el código:")
        self.label.pack()

        self.code_text = tk.Text(master, width=40, height=10)
        self.code_text.pack()

        self.button = tk.Button(master, text="Compilar", command=self.compile_code)
        self.button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

def compile_code(self):
    code = self.code_text.get("1.0", "end")
    result = self.run_compiler(code)
    self.result_label.config(text=result)

def run_compiler(self, code):
    lexer.input(code)
    parsed = parser.parse(code)
    return str(parsed)

root = tk.Tk()
app = CompilerApp(root)
root.mainloop()