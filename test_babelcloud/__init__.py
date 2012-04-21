# Copyright (C) 2011 by Alex Brandt <alunduil@alunduil.com>

"""Primary testing suite for babelcloud"""

__all__ = [
        "SUITE",
        ]

import sys
import os
import unittest

from test_login import LoginTest
from test_account import AccountTest
from test_server import ServerExistenceTest
from test_server import ServerManipulationTest

SUITE_LIST = [
        unittest.TestLoader().loadTestsFromTestCase(LoginTest),
        unittest.TestLoader().loadTestsFromTestCase(AccountTest),
        unittest.TestLoader().loadTestsFromTestCase(ServerExistenceTest),
        unittest.TestLoader().loadTestsFromTestCase(ServerManipulationTest),
        ]
SUITE = unittest.TestSuite(SUITE_LIST)

