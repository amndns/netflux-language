
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULTIPLYDIVIDErightPOWERMODULUSINT REAL STRING NAME LBRACK RBRACK COMMA PLUS MINUS DIVIDE MULTIPLY POWER MODULUS EQUALS\n    calc : expression\n         | var_assign\n         | list_access_assign\n         | empty\n    \n    var_assign : NAME EQUALS expression\n    \n    expression : expression POWER expression\n               | expression MULTIPLY expression\n               | expression DIVIDE expression\n               | expression MODULUS expression\n               | expression PLUS expression\n               | expression MINUS expression\n    \n    expression : INT\n               | REAL\n    \n    expression : NAME\n    \n    empty :\n    \n    arguments : arguments COMMA expression\n              | expression\n              |\n    \n    expression : LBRACK arguments RBRACK\n    \n    expression : NAME LBRACK expression RBRACK\n    \n    list_access_assign : NAME LBRACK expression RBRACK EQUALS expression\n    '
    
_lr_action_items = {'INT':([0,9,10,11,12,13,14,15,16,17,30,31,35,],[6,6,6,6,6,6,6,6,6,6,6,6,6,]),'REAL':([0,9,10,11,12,13,14,15,16,17,30,31,35,],[7,7,7,7,7,7,7,7,7,7,7,7,7,]),'NAME':([0,9,10,11,12,13,14,15,16,17,30,31,35,],[8,20,20,20,20,20,20,20,20,20,20,20,20,]),'LBRACK':([0,8,9,10,11,12,13,14,15,16,17,20,30,31,35,],[9,16,9,9,9,9,9,9,9,9,9,31,9,9,9,]),'$end':([0,1,2,3,4,5,6,7,8,20,21,22,23,24,25,26,28,29,32,36,37,],[-15,0,-1,-2,-3,-4,-12,-13,-14,-14,-6,-7,-8,-9,-10,-11,-5,-19,-20,-20,-21,]),'POWER':([2,6,7,8,19,20,21,22,23,24,25,26,27,28,29,32,33,34,36,37,],[10,-12,-13,-14,10,-14,10,10,10,10,10,10,10,10,-19,-20,10,10,-20,10,]),'MULTIPLY':([2,6,7,8,19,20,21,22,23,24,25,26,27,28,29,32,33,34,36,37,],[11,-12,-13,-14,11,-14,-6,-7,-8,-9,11,11,11,11,-19,-20,11,11,-20,11,]),'DIVIDE':([2,6,7,8,19,20,21,22,23,24,25,26,27,28,29,32,33,34,36,37,],[12,-12,-13,-14,12,-14,-6,-7,-8,-9,12,12,12,12,-19,-20,12,12,-20,12,]),'MODULUS':([2,6,7,8,19,20,21,22,23,24,25,26,27,28,29,32,33,34,36,37,],[13,-12,-13,-14,13,-14,13,13,13,13,13,13,13,13,-19,-20,13,13,-20,13,]),'PLUS':([2,6,7,8,19,20,21,22,23,24,25,26,27,28,29,32,33,34,36,37,],[14,-12,-13,-14,14,-14,-6,-7,-8,-9,-10,-11,14,14,-19,-20,14,14,-20,14,]),'MINUS':([2,6,7,8,19,20,21,22,23,24,25,26,27,28,29,32,33,34,36,37,],[15,-12,-13,-14,15,-14,-6,-7,-8,-9,-10,-11,15,15,-19,-20,15,15,-20,15,]),'RBRACK':([6,7,9,18,19,20,21,22,23,24,25,26,27,29,33,34,36,],[-12,-13,-18,29,-17,-14,-6,-7,-8,-9,-10,-11,32,-19,-16,36,-20,]),'COMMA':([6,7,9,18,19,20,21,22,23,24,25,26,29,33,36,],[-12,-13,-18,30,-17,-14,-6,-7,-8,-9,-10,-11,-19,-16,-20,]),'EQUALS':([8,32,],[17,35,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'calc':([0,],[1,]),'expression':([0,9,10,11,12,13,14,15,16,17,30,31,35,],[2,19,21,22,23,24,25,26,27,28,33,34,37,]),'var_assign':([0,],[3,]),'list_access_assign':([0,],[4,]),'empty':([0,],[5,]),'arguments':([9,],[18,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> calc","S'",1,None,None,None),
  ('calc -> expression','calc',1,'p_calc','parser.py',15),
  ('calc -> var_assign','calc',1,'p_calc','parser.py',16),
  ('calc -> list_access_assign','calc',1,'p_calc','parser.py',17),
  ('calc -> empty','calc',1,'p_calc','parser.py',18),
  ('var_assign -> NAME EQUALS expression','var_assign',3,'p_var_assign','parser.py',24),
  ('expression -> expression POWER expression','expression',3,'p_expression','parser.py',30),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression','parser.py',31),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','parser.py',32),
  ('expression -> expression MODULUS expression','expression',3,'p_expression','parser.py',33),
  ('expression -> expression PLUS expression','expression',3,'p_expression','parser.py',34),
  ('expression -> expression MINUS expression','expression',3,'p_expression','parser.py',35),
  ('expression -> INT','expression',1,'p_expression_int_float','parser.py',41),
  ('expression -> REAL','expression',1,'p_expression_int_float','parser.py',42),
  ('expression -> NAME','expression',1,'p_expression_var','parser.py',48),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',54),
  ('arguments -> arguments COMMA expression','arguments',3,'p_comma_separated_expr','parser.py',60),
  ('arguments -> expression','arguments',1,'p_comma_separated_expr','parser.py',61),
  ('arguments -> <empty>','arguments',0,'p_comma_separated_expr','parser.py',62),
  ('expression -> LBRACK arguments RBRACK','expression',3,'p_list','parser.py',74),
  ('expression -> NAME LBRACK expression RBRACK','expression',4,'p_list_access','parser.py',80),
  ('list_access_assign -> NAME LBRACK expression RBRACK EQUALS expression','list_access_assign',6,'p_list_access_assign','parser.py',86),
]
