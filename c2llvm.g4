grammar c2llvm;

prog: (include)* (declaration | statement)*;

include: '#include' '<' HEADER '>';

declaration: functionDeclaration | structDeclaration;

structDeclaration:
	vStruct '{' (structMemberDeclaration)+ '}' ';';

structMemberDeclaration:
	(vType | vStruct) (vId | vArray) (',' (vId | vArray))* ';';



statement:
	variableDefinitionStatement
	| arrayDefinitionStatement
	| structDefinitionStatement
	| assignStatement
	| conditionStatement
	| whileStatement
	| forStatement
	| returnStatement
	| breakStatement
	| continueStatement
	| funcStatement;

assignStatement: ((vId | vArrayItem | vStructMember) '=')+ expression ';';

conditionStatement:
	ifStatement elseifStatement* elseStatement?;

ifStatement:
	'if' '(' expression ')' '{' statement* '}';

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

arrayDefinitionStatement:
	vType vId '[' vInt ']' ';';

structDefinitionStatement:
	vStruct (vId | vArray) ';';

vArrayItem: 
	vId '[' expression ']';

vStructMember:
	(vId | vArrayItem) '.' (vId | vArrayItem);

funcStatement: funcExpression ';';

funcExpression: vId '(' paramsInvokePattern ')';

paramsInvokePattern:
	paramInvokePattern (',' paramInvokePattern)*
	|;

paramInvokePattern: expression;

functionDeclaration:
	vType vId '(' paramsDefinitionPattern ')' '{' statement* '}';

paramsDefinitionPattern:
	paramDefinitionPattern (',' paramDefinitionPattern)*
	|;

paramDefinitionPattern: vType vId;

expression:
	'(' expression ')' #Parens
	| '!' expression #Neg
	| expression ('*' | '/' | '%') expression #MulDivMod
	| expression ('+' | '-') expression #AddSub
	| expression ('==' | '!=' | '>=' | '>' | '<' | '<=') expression #Compare
	| expression '&&' expression #And
	| expression '||' expression #Or
	| vArrayItem     #ArrayItem
	| vStructMember  #structMember
	| ('-')? vInt #Int
	| ('-')? vDouble #Double
	| vChar #Char
	| vString #String
	| vId #Id
	| funcExpression #FunctionExpr
	;

vType: 'int' | 'double' | 'char' | 'void';
vInt: INT;
vChar:CHAR;
vDouble:DOUBLE;
vString:STRING;
vId:ID;
vStruct: 'struct' vId;
vArray: vId '[' vInt ']';


ID: [a-zA-Z_][0-9a-zA-Z_]*;
DOUBLE: [0-9]+ '.' [0-9]+;
CHAR: '\'' .'\'';
STRING: '"' .*? '"';
INT: [0-9]+;
HEADER: [a-zA-Z]+ '.h'?;
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
