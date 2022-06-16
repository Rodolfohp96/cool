from antlr4 import *
from antlr.coolLexer import coolLexer
from antlr.coolParser import coolParser

from listeners.semantic_one_listener import semanticOneListener
from listeners.semantic_two_listener import semanticTwoListener
from listeners.semantic_three_listener import semanticThreeListener
from listeners.tree import TreePrinter

def compile(file):
    parser = coolParser(CommonTokenStream(coolLexer(FileStream(file))))
    tree = parser.program()

    walker = ParseTreeWalker()
    
    walker.walk(semanticOneListener(), tree)
    walker.walk(semanticTwoListener(), tree)
    walker.walk(semanticThreeListener(), tree)
    walker.walk(TreePrinter(), tree)

def dummy():
    raise SystemExit(1)
    
if __name__ == '__main__':
    compile('resources/semantic/input/dispatch.cool')
