from antlr4 import *
from gen.LangLexer import LangLexer
from gen.LangParser import LangParser
from interpreter import Interpreter

def main():
    input_stream = FileStream("test.lang")
    lexer = LangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LangParser(stream)
    tree = parser.program()

    visitor = Interpreter()
    visitor.visit(tree)

if __name__ == "__main__":
    main()