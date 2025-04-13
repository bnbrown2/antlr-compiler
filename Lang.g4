grammar Lang;

program: statement* EOF;

statement
    : printStmt ';'
    | exprStmt ';'                 // added arithmetic statement
    ;

printStmt: 'print' '(' STRING ')';
exprStmt: expr;                    // arithmetic expression statement

expr
    : expr ('*' | '/') expr        # MulDivExpr
    | expr ('+' | '-') expr        # AddSubExpr
    | INT                          # IntExpr
    | '(' expr ')'                 # ParensExpr
    ;

STRING: '"' .*? '"';
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;