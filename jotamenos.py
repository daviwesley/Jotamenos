from lark import Lark

grammar = '''
start : main_class class_declaration*
main_class : "class" IDENTIFIER "{" reserved_string reserved_string reserved_string reserved_string "(" reserved_string "[" "]" IDENTIFIER ")" "{" statement "}" "}"
class_declaration : "class" IDENTIFIER ( "extends"i IDENTIFIER )? "{" ( var_declaration )* ( method_declaration )* "}"
var_declaration : type IDENTIFIER ";"
method_declaration : "public"i type IDENTIFIER "(" ( type IDENTIFIER ( "," type IDENTIFIER )* )? ")" "{" ( var_declaration )* ( statement )* "return" expression ";" "}"
type : "int [ ]"
       | "boolean"
       | "int"
       | IDENTIFIER
statement : "{" ( statement )* "}"
            | "if" "("expression ")" statement "else" statement
            | "while" "(" expression ")" statement
            | "System.out.println" "(" expression ")" ";"
            | IDENTIFIER "=" expression ";"
            | IDENTIFIER "[" expression "]" "=" expression ";"
expression : expression ( "&&" | "<" | "+" | "-" | "*" ) expression
            | expression "[" expression "]"
            | expression "." "length"
            | expression "." IDENTIFIER "(" ( expression ( "," expression )* )? ")"
            | DIGIT*
            | "true"
            | "false"
            | IDENTIFIER
            | "this"
            | "new" "int" "[" expression "]"
            | "new" IDENTIFIER "(" ")"
            | "!" expression
            | "(" expression ")"
IDENTIFIER: WORD
reserved_string: "int" | "public" | "void" | "main" | "static"
%import common.WORD
%import common.DIGIT
%import common.ESCAPED_STRING
%import common.WS

%ignore WS
%ignore ESCAPED_STRING
'''

test_code = '''class Teste{
    public static void main(int[] a){
        System.out.println(10);
    }
}
'''

j = Lark(grammar, debug=True)
parse = j.parse(test_code)
print(parse)
