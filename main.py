from antlr4 import *
from gen.LangLexer import LangLexer
from gen.LangParser import LangParser
from interpreter import Interpreter

def main():
    # load and tokenize 
    input = FileStream("test.lang") 
    lexer = LangLexer(input) 
    token_stream = CommonTokenStream(lexer) 

    # parse
    parser = LangParser(token_stream) 
    tree = parser.program()

    # execute
    visitor = Interpreter()
    visitor.visit(tree)

if __name__ == "__main__":
    main() # make it all happen