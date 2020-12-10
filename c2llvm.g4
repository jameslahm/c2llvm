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

assignStatement: (vId '=')+ expression ';';

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

forInitStatement: vId '=' expression (',' forInitStatement)? |;

forExecStatement: vId '=' expression (',' forExecStatement)? |;

returnStatement: 'return' (vInt | vId | vDouble | vChar)? ';';

breakStatement: 'break' ';';

continueStatement: 'continue' ';';

variableDefinitionStatement:
	vType vId ('=' expression)? (',' vId ('=' expression)?)* ';';

funcStatement: vId '(' paramsInvokePattern ')' ';';

paramsInvokePattern:
	paramInvokePattern (',' paramInvokePattern)*
	|;

paramInvokePattern: vId | vChar | vInt | vDouble | vString;

functionDeclaration:
	vType vId '(' paramsDefinitionPattern ')' '{' statement* '}';

paramsDefinitionPattern:
	paramDefinitionPattern (',' paramDefinitionPattern)*
	|;

paramDefinitionPattern: vType vId;

expression:
	'(' expression ')' #Parens
	| op = '!' expression #Neg
	| expression op = ('*' | '/' | '%') expression #MulDivMod
	| expression op = ('+' | '-') expression #AddSub
	| expression op = ('==' | '!=' | '>=' | '>' | '<' | '<=') expression #Compare
	| expression '&&' expression #And
	| expression '||' expression #Or
	| (op = '-')? vInt #Int
	| (op = '-')? vDouble #Double
	| vChar #Char
	| vId #Id
	| vId '(' paramsInvokePattern ')' #FunctionExpr
	;

vType: 'int' | 'double' | 'char' | 'void';
vInt: INT;
vChar:CHAR;
vDouble:DOUBLE;
vString:STRING;
vId:ID;


ID: [a-zA-Z_][0-9a-zA-Z_]*;
DOUBLE: [0-9]+ '.' [0-9]+;
CHAR: '\'' .'\'';
STRING: '"' .*? '"';
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
