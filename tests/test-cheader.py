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

if __name__ == '__main__':
    unittest.main()
