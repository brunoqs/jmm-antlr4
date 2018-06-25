grammar jmm ;

compilationUnit : ('package' qualifiedIdentifier ';')?
				  ('import' qualifiedIdentifier ';')*
				  (typeDeclaration)* EOF
				;

qualifiedIdentifier : ID ('.' ID)*
					;

typeDeclaration : modifiers classDeclaration
				;

modifiers : ('public' | 'protected' | 'private' | 'static' | 'abstract')*
          ;

classDeclaration : 'class' ID ('extends' qualifiedIdentifier)? classBody
				 ;

classBody : '{' (modifiers memberDecl)* '}'
		  ;

memberDecl : ID formalParameters block
			 | ('void' | tipe) ID formalParameters (block | ';')
			 | tipe variableDeclarators ';'
		   ;

block : '{' (blockStatement)* '}'
      ;

blockStatement : localVariableDeclarationStatement
				 | statement
			   ;

statement : block
			| ID ':' statement
			| 'if' parExpression statement ('else' statement)?
			| 'while' parExpression statement
			| 'return' (expression)? ';'
			| ';'
			| statementExpression ';'
		  ;

formalParameters : '(' ( formalParameter (',' formalParameter)* )? ')'
  				 ;

formalParameter : tipe ID
    			;

parExpression : '(' expression ')'
			  ;

localVariableDeclarationStatement : tipe variableDeclarators ';'
								  ;

variableDeclarators : variableDeclarator (',' variableDeclarator)*
					;

variableDeclarator : ID ('=' variableInitializer)?
				   ;

variableInitializer : arrayInitializer | expression
                    ;

arrayInitializer : '{' ( variableInitializer (',' variableInitializer)* )? '}'
				 ;

arguments : '(' ( expression (',' expression)* )? ')'
		  ;

tipe : referenceType | basicType
     ;

basicType : 'boolean' | 'char' | 'int'
		  ;

referenceType : basicType '[' ']' ('[' ']')*
				| qualifiedIdentifier ('[' ']')*
			  ;

statementExpression : expression 
				    ;

expression : assignmentExpression	
		   ;

assignmentExpression : conditionalAndExpression ( ('=' | '+=') assignmentExpression)?
					 ;

conditionalAndExpression : equalityExpression ('&&' equalityExpression)*
						 ;

equalityExpression : relationalExpression ('==' relationalExpression)*
				   ;

relationalExpression : additiveExpression ( ('>' | '<=') additiveExpression | 'instanceof' referenceType)?
					 ;

additiveExpression : multiplicativeExpression ( ('+'|'-') multiplicativeExpression)*
				   ;

multiplicativeExpression : unaryExpression ('*' unaryExpression)*
						 ;

unaryExpression : '++' unaryExpression 
				  | '-' unaryExpression
				  | simpleUnaryExpression
				;

simpleUnaryExpression : '!' unaryExpression
						| '(' basicType ')' unaryExpression 
						| '(' referenceType ')' simpleUnaryExpression 
						| postfixExpression
					  ;

postfixExpression : primary (selector)* ('--')*
  				  ;

selector : '.' qualifiedIdentifier (arguments)?
		   | '[' expression ']'
		 ;

primary : parExpression
			| 'this' (arguments)?
			| 'super' (arguments | '.' ID (arguments)?)
			| literal
			| 'new' creator
			| qualifiedIdentifier (arguments)?
		;

creator : (basicType | qualifiedIdentifier)
		  ( arguments | '[' ']' ('[' ']')* (arrayInitializer)? | newArrayDeclarator )
		;

newArrayDeclarator : '[' expression ']' ('[' expression ']')* ('[' ']')*
 				   ;

literal : INT | CHAR | STRING | 'true' | 'false' | 'null'
        ;

ID : ([a-zA-Z]+|'_'|'$')([a-zA-Z]+|'_'|[0-9]+|'$')* ;
INT : [0-9]+ ;
CHAR : '\'' (~['\\\r\n] | EscapeSequence) '\'' ;
STRING : '"' (~["\\\r\n] | EscapeSequence)* '"' ;

WS : [ \t\r\n\u000C]+ -> channel(HIDDEN) ;
COMMENT : '/*' .*? '*/'    -> channel(HIDDEN) ;
LINE_COMMENT : '//' ~[\r\n]*    -> channel(HIDDEN) ;

fragment EscapeSequence : '\\' [btnfr"'\\]
    					  | '\\' ([0-3]? [0-7])? [0-7]
                          | '\\' 'u'+ HexDigit HexDigit HexDigit HexDigit
                        ;

fragment HexDigit : [0-9a-fA-F]
                  ;