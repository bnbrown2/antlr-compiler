grammar Lang;

program
  : statement* EOF
  ;

statement
  : printStmt ';'
  | ifStmt
  | assignment ';'
  | exprStmt ';'
  | whileStmt
  | forStmt
  ;

printStmt
  : 'print' '(' STRING ')'
  ;

exprStmt
  : expr
  ;

expr
  : expr ('+' | '-') expr          # AddSubExpr
  | expr ('*'|'/') expr            # MulDivExpr
  | INT                            # IntExpr
  | ID                             # IdExpr
  | 'cos' '(' expr ')'             # CosExpr
  | 'sin' ( '(' expr ')' )         # SinExpr
  | '(' expr ')'                   # ParensExpr
  | 'tan' '(' expr ')'             # TanExpr
  ;

assignment
  : ID '=' expr
  ;

ifStmt
  : 'if' '(' condition ')' '{' statement* '}'
  ;

forStmt
  : 'for' '(' assignment ';' condition ';' assignment ')' '{' statement* '}'
  ;

whileStmt
  : 'while' '(' condition ')' '{' statement* '}'
  ;

condition
  : expr comparisonOp expr
  ;

comparisonOp
  : '<' | '>' | '<=' | '>=' | '==' | '!='
  ;

STRING : '"' .*? '"' ;
ID     : [a-zA-Z_] [a-zA-Z_0-9]* ;
INT    : [0-9]+ ;
WS     : [ \t\n\r]+ -> skip ;