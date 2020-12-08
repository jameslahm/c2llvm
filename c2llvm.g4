grammar c2llvm;

prog: (include)* (declaration | statement)*;

include: '#include' '<' LIB '>';

declaration: functionDeclaration;

statement:
	variableDefinitionStatement
	| assignStatement
	| ifStatement
	| whileStatement
	| forStatement
	| returnStatement
	| breakStatement
	| continueStatement
	| funcStatement;

assignStatement: (ID '=')+ expression ';';

ifStatement:
	'if' '(' expression ')' '{' statement* '}' elseifStatement* elseStatement?;

elseifStatement:
	'else' 'if' '(' expression ')' '{' statement* '}';

elseStatement: 'else' '{' statement* '}';

whileStatement: 'while' '(' expression ')' '{' statement* '}';

forStatement:
	'for' '(' forInitStatement ';' expression ';' forExecStatement ')' (
		'{' statement* '}'
		| ';'
	);

forInitStatement: ID '=' expression (',' forInitStatement)? |;

forExecStatement: ID '=' expression (',' forExecStatement)? |;

returnStatement: 'return' (INT | ID | DOUBLE | CHAR)? ';';

breakStatement: 'break' ';';

continueStatement: 'continue' ';';

variableDefinitionStatement:
	vType ID ('=' expression)? (',' ID ('=' expression)?)* ';';

funcStatement: ID '(' paramsInvokePattern ')' ';';

paramsInvokePattern:
    paramInvokePattern (',' paramInvokePattern) *|;

paramInvokePattern:
    ID | CHAR | INT | DOUBLE | STRING;

functionDeclaration:
	vType ID '(' paramsDefinitionPattern ')' '{' statement* '}';

paramsDefinitionPattern: paramDefinitionPattern (',' paramDefinitionPattern)* |;

paramDefinitionPattern: vType ID;

expression:
	'(' expression ')'
	| op = '!' expression
	| expression op = ('*' | '/' | '%') expression
	| expression op = ('+' | '-') expression
	| expression op = ('==' | '!=' | '>=' | '>' | '<' | '<=') expression
	| expression '&&' expression
	| expression '||' expression
	| (op = '-')? INT
	| (op = '-')? DOUBLE
	| CHAR
	| ID
	| funcStatement;

vType: 'int' | 'double' | 'char';

ID: [a-zA-Z_][0-9a-zA-Z_]*;
DOUBLE: [0-9]+ '.' [0-9]+;
CHAR: '\'' .'\'';
STRING : '"'.*?'"';
INT: [0-9]+;
LIB: [a-zA-Z]+ '.h'?;
Conjunction: '&&' | '||';
Operator:
	'!'
	| '+'
	| '-'
	| '*'
	| '/'
	| '=='
	| '!='
	| '<'
	| '<='
	| '>'
	| '>=';
LineComment: '//' .*? '\r'? '\n' -> skip;
BlockComment: '/*' .*? '*/' -> skip;
WS: [ \t\r\n]+ -> skip;
