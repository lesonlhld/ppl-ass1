grammar BKIT;
//1810482
@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

program  : (variable_decl | body_decl)+ EOF;

fragment LETTER: [a-zA-Z];
fragment DIGIT: [0-9];
fragment NON_ZERO_DIGIT: [1-9];
fragment OCT_DIGIT: [0-7];
fragment NON_OCT_DIGIT: [1-7];
fragment HEX_DIGIT: [0-9A-F];
fragment NON_HEX_DIGIT: [1-9A-F];
fragment INT_PART: DECIMAL_INTEGER;
fragment DEC_PART: DOT DECIMAL_INTEGER;
fragment EXPONENT: [eE][+-]? DECIMAL_INTEGER;
fragment POINT_FLOAT : (INT_PART DEC_PART) | INT_PART DOT;
fragment EXPONENT_FLOAT : (INT_PART | POINT_FLOAT) EXPONENT;
fragment WS: [ \t\r\n\f]+; // White-space characters
fragment COMMENT: '**' .*? '**';
fragment NEWLINE: ('\r' '\n'? | '\n');
fragment DOUBLE_QUOTE: ["];
fragment SINGLE_QUOTE: ['];
fragment STRING_CONTENT: '\'"' | ~["\b\f\r\n\t\\] | ESCAPE_SEQ;
fragment ESCAPE_SEQ: '\\' [bfrnt'\\"];
fragment ESCAPE_ILLEGAL: '\\' ~[bfrnt'\\"] | ~'\\' | '\'' ~["];
fragment ARRAY_LIST: ARRAY_TYPE (COMMA ARRAY_TYPE)*;
fragment ARRAY_TYPE: DECIMAL_INTEGER | STRING | BOOLEAN | FLOAT | ARRAY;
fragment DIMENSION: LEFT_BRACKET (DECIMAL_INTEGER | ID) RIGHT_BRACKET;

/*
 * Lexer rules
 */

// Identifiers
ID: [a-z][a-zA-Z0-9_]*;

// Keywords
VAR: 'Var';
BODY: 'Body';
BREAK: 'Break';
CONTINUE: 'Continue';
DO: 'Do';
ELSE: 'Else';
ELSEIF:'ElseIf';
ENDBODY:'EndBody';
ENDIF:'EndIf';
ENDFOR:'EndFor';
ENDWHILE:'EndWhile';
FOR:'For';
FUNCTION:'Function';
IF:'If';
PARAMETER:'Parameter';
RETURN:'Return';
THEN:'Then';
WHILE:'While';
TRUE:'True';
FALSE:'False';
ENDDO:'EndDo';

// Type
INT_TYPE: 'int';
FLOAT_TYPE: 'float';
BOOLEAN_TYPE: 'boolean';
STRING_TYPE: 'string';

// Operators
ADD: '+';
ADD_F: '+.';
SUB: '-';
SUB_F: '-.';
MULTI: '*';
MULTI_F: '*.';
DIV: '\\';
DIV_F: '\\.';
MOD: '%';

NOT: '!';
ANDAND: '&&';
OROR: '||';

EQUAL: '==';
NOT_EQUAL: '!=';
LESS_THAN: '<';
GREATER_THAN: '>';
GREATER_EQUAL: '>=';
LESS_EQUAL: '<=';
NOT_EQUAL_F: '=/=';
LESS_THAN_F: '<.';
GREATER_THAN_F: '>.';
GREATER_EQUAL_F: '>=.';
LESS_EQUAL_F: '<=.';

// Separators
SEMI: ';';
COLON: ':';
DOT: '.';
COMMA: ',';
LEFT_PAREN: '(';
RIGHT_PAREN: ')';
LEFT_BRACKET: '[';
RIGHT_BRACKET: ']';
LEFT_BRACE: '{';
RIGHT_BRACE: '}';
ASSIGN: '=';

// Literals
DECIMAL_INTEGER: NON_ZERO_DIGIT DIGIT* | [0];
HEX_INTEGER: [0][xX] NON_HEX_DIGIT HEX_DIGIT*;
OCT_INTEGER: [0][oO] NON_OCT_DIGIT OCT_DIGIT*;

FLOAT: POINT_FLOAT | EXPONENT_FLOAT;

BOOLEAN: TRUE | FALSE;

STRING: DOUBLE_QUOTE STRING_CONTENT*? DOUBLE_QUOTE {
		y = str(self.text)
		self.text = y[1:-1]
	};

ARRAY: LEFT_BRACE ARRAY_LIST? RIGHT_BRACE;
ARRAY_DECL: ID DIMENSION+;

SKIP_ : (COMMENT | WS | NEWLINE) -> skip ; // skip spaces, tabs, newlines or comment

/*
 * Parser rules
 */
variable_decl: VAR COLON variable_list (ASSIGN init_value)? SEMI;

variable_list: ID | ARRAY_DECL | (ID | ARRAY_DECL) COMMA variable_list;

var_list: ID | ARRAY_DECL | array_index | (ID | ARRAY_DECL | array_index) COMMA variable_list;

init_value: literal (COMMA literal)*;

literal: DECIMAL_INTEGER|FLOAT|BOOLEAN|STRING|ARRAY|ID;

array_index: ID index_operators;

body_decl: init_body body;

init_body: FUNCTION COLON ID parameter?;

parameter: PARAMETER COLON variable_list;

body: BODY COLON variable_decl*? stmt_list? ENDBODY DOT;

// Statement
stmt: assign_stmt | if_stmt | for_stmt | while_stmt | do_while_stmt | break_stmt | continue_stmt | call_stmt | return_stmt;

stmt_list: stmt*;

assign_stmt: var_list ASSIGN exp SEMI;

if_stmt: IF exp THEN stmt_list? (ELSEIF exp THEN stmt_list?)* (ELSE stmt_list?)? ENDIF DOT;

for_stmt: FOR LEFT_PAREN for_condition RIGHT_PAREN DO stmt_list ENDFOR DOT;

for_condition: ID ASSIGN exp COMMA exp COMMA exp;

while_stmt: WHILE exp DO stmt_list ENDWHILE DOT;

do_while_stmt: DO stmt_list WHILE exp ENDDO DOT;

break_stmt: BREAK SEMI;

continue_stmt: CONTINUE SEMI;

call_stmt: ID LEFT_PAREN exp_list? RIGHT_PAREN SEMI;

return_stmt: RETURN exp? SEMI;

// Expression
exp: exp1 relational_operators exp1 | exp1;

exp1: exp1 boolean_operators exp2 | exp2;

exp2: exp2 adding_operators exp3 | exp3;

exp3: exp3 multiplying_operators exp4 | exp4;

exp4: NOT exp4 | exp5;

exp5: sign_operators exp5 | exp6;

exp6: exp6 LEFT_BRACKET exp7 (COMMA exp7)* RIGHT_BRACKET | exp7;

exp7: function_call | operands;

exp_list: exp (COMMA exp)*;

operands: literal | LEFT_PAREN exp RIGHT_PAREN | index_operators | ARRAY_DECL;

// Funtion call
function_call: ID LEFT_PAREN exp_list? RIGHT_PAREN;

// Operators
multiplying_operators: MULTI | MULTI_F | DIV | DIV_F | MOD;

adding_operators: ADD | ADD_F | SUB | SUB_F;

sign_operators: SUB| SUB_F;

boolean_operators: NOT | ANDAND | OROR;

relational_operators: EQUAL | NOT_EQUAL | LESS_THAN | GREATER_THAN | GREATER_EQUAL | LESS_EQUAL | NOT_EQUAL_F | LESS_EQUAL_F | GREATER_THAN_F | GREATER_EQUAL_F | LESS_EQUAL_F;

element_exp: exp index_operators;

index_operators: LEFT_BRACKET exp RIGHT_BRACKET | LEFT_BRACKET exp RIGHT_BRACKET index_operators;


ERROR_CHAR: .;
UNCLOSE_STRING: '"' STRING_CONTENT* ([\b\f\r\n\t\\] | EOF) {
		y = str(self.text)
		self.text = y[1:]
	};
ILLEGAL_ESCAPE: '"' STRING_CONTENT* ESCAPE_ILLEGAL {
		y = str(self.text)
		self.text = y[1:]
	};
UNTERMINATED_COMMENT: '**' .*?;