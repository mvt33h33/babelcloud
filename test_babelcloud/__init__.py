# Copyright (C) 2011 by Alex Brandt <alunduil@alunduil.com>

"""Primary testing suite for babelcloud"""

import sys
import os
import unittest

import test_login
import test_account
import test_server

def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_login.suite())
    suite.addTest(test_account.suite())
    suite.addTest(test_server.suite())
    return suite

if __name__ == "__main__":
    unittest.main()

