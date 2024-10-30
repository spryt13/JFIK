import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprListener import ExprListener
from LLVMActions import LLVMActions

input = "x =2* (1 - 2)*3\n y = 3.3 \nx = toint y +1 \n"
#input = "read int x \n x = x +2\n  \t print x*3 \n"

input_stream = InputStream(input)
lexer = ExprLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = ExprParser(stream)
tree = parser.prog()

walker = ParseTreeWalker()
#walker.walk(ExprListener(), tree)
walker.walk(LLVMActions(), tree)