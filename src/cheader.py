#!/usr/bin/python

from __future__ import print_function
import sys

sys.path.extend(['.', '..'])

from pycparser import c_parser, c_ast, parse_file, c_generator

class FuncDefVisitor(c_ast.NodeVisitor):
    def visit_FuncDef(self, node):
        generator = c_generator.CGenerator()
        decl = generator.visit_Decl(node.decl)
        print('%s' % (decl))


def show_func_defs(filename):
    ast = parse_file(filename, use_cpp=True)

    v = FuncDefVisitor()
    v.visit(ast)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename  = sys.argv[1]
        show_func_defs(filename)
    else:
        print('No args passed. Exiting.')
