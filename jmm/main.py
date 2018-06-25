import sys
from antlr4 import *
from compiler.jmmLexer import jmmLexer
from compiler.jmmParser import jmmParser
from compiler.jmmListener import jmmListener
 
def main(argv):
    input = FileStream(argv[1])
    lexer = jmmLexer(input)
    stream = CommonTokenStream(lexer)
    parser = jmmParser(stream)

    # setando primeira regra da gramatica
    tree = parser.compilationUnit()
    listener = jmmListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
 
if __name__ == '__main__':
    main(sys.argv)
