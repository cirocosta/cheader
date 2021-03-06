#!/usr/bin/python

from __future__ import print_function
import sys

sys.path.extend(['.', '..'])

from pycparser import c_parser, c_ast, parse_file, c_generator


def get_func_defs(filename):
    gotten = []
    ast = parse_file(filename, use_cpp=True)
    generator = c_generator.CGenerator()

    for ext in ast.ext:
        gotten.append(generator.visit_Decl(ext.decl))

    return '\n'.join(gotten)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename  = sys.argv[1]
        get_func_defs(filename)
    else:
        print('No args passed. Exiting.')
