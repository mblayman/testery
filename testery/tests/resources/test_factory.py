from testery.tests import TestCase
from testery.tests.factory import Factory


class TestFactory(TestCase):

    def test_has_factory(self):
        self.assertIsInstance(self.factory, Factory)
