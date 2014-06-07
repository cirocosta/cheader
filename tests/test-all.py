# -*- coding: utf-8 -*-

import unittest
import sys
sys.path[0:0] = ['.', '..']

suite = unittest.TestLoader().loadTestsFromNames(
    [
        'test-cheader',
    ]
)

testresult = unittest.TextTestRunner(verbosity=1).run(suite)
sys.exit(0 if testresult.wasSuccessful() else 1)

