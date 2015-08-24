import unittest

from .. import db
from .factories import Factory


class TestCase(unittest.TestCase):
    """Base TestCase for testery"""

    def setUp(self):
        self.factory = Factory()
        self.session = db.Session()

    def tearDown(self):
        self.session.rollback()
        db.Session.remove()
