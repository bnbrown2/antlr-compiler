grammar Lang;

program: statement* EOF;
statement: printStmt ';';
printStmt: 'print' '(' STRING ')';

STRING: '"' .*? '"';
WS: [ \t\r\n]+ -> skip;
