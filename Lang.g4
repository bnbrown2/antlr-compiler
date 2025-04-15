grammar Lang;
program: statement* EOF;

statement
    : printStmt ';'
    | exprStmt ';'
    | assignment ';'
    | ifStmt
    | forStmt
    | whileStmt
    ;

printStmt: 'print' '(' STRING ')';
exprStmt: expr;

assignment: ID '=' expr;
ifStmt: 'if' '(' condition ')' '{' statement* '}';
forStmt: 'for' '(' assignment ';' condition ';' assignment ')' '{' statement* '}';
whileStmt: 'while' '(' condition ')' '{' statement* '}';

condition: expr comparisonOp expr;
comparisonOp: '==' | '!=' | '<' | '<=' | '>' | '>=';

expr
    : expr ('*' | '/') expr        # MulDivExpr
    | expr ('+' | '-') expr        # AddSubExpr
    | 'sin' '(' expr ')'           # SinExpr
    | 'cos' '(' expr ')'           # CosExpr
    | 'tan' '(' expr ')'           # TanExpr
    | INT                          # IntExpr
    | ID                           # IdExpr
    | '(' expr ')'                 # ParensExpr
    ;

STRING: '"' .*? '"';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;