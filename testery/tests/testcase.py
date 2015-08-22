import unittest

from .factory import Factory


class TestCase(unittest.TestCase):
    """Base TestCase for testery"""

    def __init__(self, methodName='runTest'):
        super(TestCase, self).__init__(methodName)
        self.factory = Factory()
