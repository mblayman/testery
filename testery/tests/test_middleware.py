import mock
from sqlalchemy.orm import session

from testery.middleware import SessionMiddleware
from testery.tests import TestCase


class TestSessionMiddleware(TestCase):

    def test_adds_session(self):
        req = self.factory.make_req()
        req.context['session'] = None
        resp = self.factory.make_resp()
        middleware = SessionMiddleware()
        middleware.process_request(req, resp)
        self.assertIsInstance(req.session, session.Session)

    def test_session_teardown(self):
        req = self.factory.make_req()
        req.context['session'] = mock.Mock()
        resp = self.factory.make_resp()
        resource = mock.Mock()
        middleware = SessionMiddleware()
        middleware.process_response(req, resp, resource)
        req.context['session'].remove.assert_called_once_with()