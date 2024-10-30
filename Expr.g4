grammar Expr;



prog:   block EOF;

block:	((stat|func) NEWLINE)*;

blockif:	block;
blockelse:	block;
blockwhile:	block;
blockfunc:	(stat NEWLINE)*;

func:	FUNCTION TYPE namefunc '(' paramsfunc? ')' '{' blockfunc '}';

namefunc:	ID;

paramsfunc:	paramfunc (',' paramfunc)*;

paramfunc:	value;

stat:	PRINT expr	#print
    |	ID '=' expr	#assign
    |	READ TYPE ID 	#read
    |	IF cond '{' blockif '}'	(ELSE '{' blockelse '}')?	#if
    |	WHILE cond '{' blockwhile '}'	#while
;

cond:	value COND_OP value;

expr:	expr_follow			#to_expr_follow
    |	expr ADDSUBSIGN expr		#addsub
;

expr_follow:	value				#to_value
    |	expr_follow MULDIVSIGN expr_follow	#muldiv

;
value:	ID	#id
    |   INT	#int
    |	REAL	#real
    |	TOINT value	#toint
    |	TOREAL value	#toreal
    |	'(' expr ')'	#par
    |	ID '(' value* ')'	#callfunc
;



NEWLINE : [\r\n]+ ;

ADDSUBSIGN	: '+'|'-' ;
MULDIVSIGN	: '*'|'/' ;

COND_OP	: '=='|'!='|'>'|'<' ;

PRINT	: 'print' ;
READ	: 'read' ;
TOINT	: 'toint' ;
TOREAL	: 'toreal' ;
TYPE	: 'int'|'real' ;

FUNCTION: 'function' ;
IF	: 'if' ;
ELSE	: 'else' ;
WHILE	: 'while' ;

INT     : [0-9]+ ;
REAL	: [0-9]+ '.' [0-9]* ;
// STRING	: '"' ( ~('\\'|'"') )* '"' ;
// BOOL	: 'true' | 'false' ;
ID	: ('a'..'z'|'A'..'Z')+ ;

WS:   [ \t]+ -> skip;