import falcon
from sqlalchemy.orm import session

from testery.tests import TestCase
from testery.tests.factory import Factory


class TestFactory(TestCase):

    def test_has_factory(self):
        self.assertIsInstance(self.factory, Factory)

    def test_make_req(self):
        req = self.factory.make_req()
        self.assertIsInstance(req, falcon.Request)

    def test_req_has_session(self):
        req = self.factory.make_req()
        self.assertIsInstance(req.session, session.Session)

    def test_make_resp(self):
        resp = self.factory.make_resp()
        self.assertIsInstance(resp, falcon.Response)
