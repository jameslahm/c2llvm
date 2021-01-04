import sys
from antlr4 import *
from c2llvmLexer import c2llvmLexer
from c2llvmListener import c2llvmListener
from c2llvmVisitor import c2llvmVisitor
from c2llvmParser import c2llvmParser
from visitor import Visitor

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = c2llvmLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = c2llvmParser(stream)
    tree = parser.prog()
    v= Visitor()
    v.visit(tree)
    if (len(argv)==3):
        print(v.module,file=open(argv[2],'w'))
        print(v.module)

if __name__ == '__main__':
    main(sys.argv)