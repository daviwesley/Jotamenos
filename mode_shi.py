from jotamenos_lexer import Lark_StandAlone


def parser():
    return Lark_StandAlone()


j = parser()

test_code = '''class Teste{
    public static void main(int[] a){
        System.out.println(10);
    }
}
'''

parse = j.parse(test_code)
print(parse)
