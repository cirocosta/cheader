# -*- coding: utf-8 -*-

import sys
import unittest

sys.path.insert(0, '.')

from src import cheader

class TestSanity(unittest.TestCase):

    def setUp(self):
        pass

    def test(self):
        self.assertEqual(1,1)

class TestMainFunctionality(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_func_def(self):
        expected = "void perform_cool_stuff(int number)\n" +\
                   "int perform_awesome_stuff(char c)"
        actual = cheader.get_func_defs('tests/test-files/file1.c')

        self.assertEqual(actual, expected);


if __name__ == '__main__':
    unittest.main()
