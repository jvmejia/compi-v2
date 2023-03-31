
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASIGNACION DEDENTACION DIVISION DOS_PUNTOS INDENTACION MIENTRAS MULTIPLICACION NOMBRE NUMERO PARENTESIS_DER PARENTESIS_IZQ RESTA SI SINO SUMAstatement : NOMBRE ASIGNACION expressionstatement : expressionexpression : expression SUMA expression\n                  | expression RESTA expression\n                  | expression MULTIPLICACION expression\n                  | expression DIVISION expressionexpression : NUMEROexpression : NOMBREstatement : SI expression DOS_PUNTOS INDENTACION statement DEDENTACIONstatement : SI expression DOS_PUNTOS INDENTACION statement DEDENTACION SINO DOS_PUNTOS INDENTACION statement DEDENTACIONstatement : MIENTRAS expression DOS_PUNTOS INDENTACION statement DEDENTACIONstatement : MIENTRAS DOS_PUNTOS error DEDENTACIONstatement : error'
    
_lr_action_items = {'NOMBRE':([0,4,5,8,9,10,11,12,25,26,34,],[2,14,14,14,14,14,14,14,2,2,2,]),'SI':([0,25,26,34,],[4,4,4,4,]),'MIENTRAS':([0,25,26,34,],[5,5,5,5,]),'error':([0,16,25,26,34,],[6,24,6,6,6,]),'NUMERO':([0,4,5,8,9,10,11,12,25,26,34,],[7,7,7,7,7,7,7,7,7,7,7,]),'$end':([1,2,3,6,7,14,17,18,19,20,21,27,30,31,36,],[0,-8,-2,-13,-7,-8,-1,-3,-4,-5,-6,-12,-9,-11,-10,]),'ASIGNACION':([2,],[8,]),'SUMA':([2,3,7,13,14,15,17,18,19,20,21,],[-8,9,-7,9,-8,9,9,9,9,9,9,]),'RESTA':([2,3,7,13,14,15,17,18,19,20,21,],[-8,10,-7,10,-8,10,10,10,10,10,10,]),'MULTIPLICACION':([2,3,7,13,14,15,17,18,19,20,21,],[-8,11,-7,11,-8,11,11,11,11,11,11,]),'DIVISION':([2,3,7,13,14,15,17,18,19,20,21,],[-8,12,-7,12,-8,12,12,12,12,12,12,]),'DEDENTACION':([2,3,6,7,14,17,18,19,20,21,24,27,28,29,30,31,35,36,],[-8,-2,-13,-7,-8,-1,-3,-4,-5,-6,27,-12,30,31,-9,-11,36,-10,]),'DOS_PUNTOS':([5,7,13,14,15,18,19,20,21,32,],[16,-7,22,-8,23,-3,-4,-5,-6,33,]),'INDENTACION':([22,23,33,],[25,26,34,]),'SINO':([30,],[32,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,25,26,34,],[1,28,29,35,]),'expression':([0,4,5,8,9,10,11,12,25,26,34,],[3,13,15,17,18,19,20,21,3,3,3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> NOMBRE ASIGNACION expression','statement',3,'p_statement_asignacion','compyv2.py',75),
  ('statement -> expression','statement',1,'p_statement_expr','compyv2.py',79),
  ('expression -> expression SUMA expression','expression',3,'p_expression_binop','compyv2.py',83),
  ('expression -> expression RESTA expression','expression',3,'p_expression_binop','compyv2.py',84),
  ('expression -> expression MULTIPLICACION expression','expression',3,'p_expression_binop','compyv2.py',85),
  ('expression -> expression DIVISION expression','expression',3,'p_expression_binop','compyv2.py',86),
  ('expression -> NUMERO','expression',1,'p_expression_numero','compyv2.py',90),
  ('expression -> NOMBRE','expression',1,'p_expression_nombre','compyv2.py',94),
  ('statement -> SI expression DOS_PUNTOS INDENTACION statement DEDENTACION','statement',6,'p_statement_si','compyv2.py',98),
  ('statement -> SI expression DOS_PUNTOS INDENTACION statement DEDENTACION SINO DOS_PUNTOS INDENTACION statement DEDENTACION','statement',11,'p_statement_si_sino','compyv2.py',102),
  ('statement -> MIENTRAS expression DOS_PUNTOS INDENTACION statement DEDENTACION','statement',6,'p_statement_mientras','compyv2.py',105),
  ('statement -> MIENTRAS DOS_PUNTOS error DEDENTACION','statement',4,'p_statement_mientras_error','compyv2.py',109),
  ('statement -> error','statement',1,'p_statement_error','compyv2.py',113),
]
