import falcon
import mock
from sqlalchemy.orm import session

from testery import db
from testery.middleware import JSONSerializerMiddleware, SessionMiddleware
from testery.tests import TestCase


class TestJSONSerializerMiddleware(TestCase):

    def test_serializes_to_json(self):
        req = self.factory.make_req()
        req.context['marshalled'] = {'hello': 'world'}
        resp = self.factory.make_resp()
        resource = mock.Mock()
        middleware = JSONSerializerMiddleware()
        middleware.process_response(req, resp, resource)
        self.assertEqual('{"hello":"world"}', resp.body)

    @mock.patch('testery.middleware.json')
    def test_do_not_serialize_404(self, json):
        req = self.factory.make_req()
        resp = self.factory.make_resp()
        resp.status = falcon.HTTP_NOT_FOUND
        resource = mock.Mock()
        middleware = JSONSerializerMiddleware()
        middleware.process_response(req, resp, resource)
        self.assertFalse(json.dumps.called)


class TestSessionMiddleware(TestCase):

    def test_adds_session(self):
        req = self.factory.make_req()
        req.context['session'] = None
        resp = self.factory.make_resp()
        middleware = SessionMiddleware()
        middleware.process_request(req, resp)
        self.assertIsInstance(req.session, session.Session)

    @mock.patch.object(db.Session, 'remove')
    def test_session_teardown(self, remove):
        req = self.factory.make_req()
        resp = self.factory.make_resp()
        resource = mock.Mock()
        middleware = SessionMiddleware()
        middleware.process_response(req, resp, resource)
        remove.assert_called_once_with()
