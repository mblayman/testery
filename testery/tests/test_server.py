from testery import middleware, request, server
from testery.tests import TestCase


class TestServer(TestCase):

    def test_uses_custom_request(self):
        api = server.make_api()
        self.assertEqual(request.Request, api._request_type)

    def test_has_session_middleware(self):
        api = server.make_api()
        process_req, _, process_resp = api._middleware[0]
        self.assertTrue(middleware.SessionMiddleware, process_req.__class__)
        self.assertTrue(middleware.SessionMiddleware, process_resp.__class__)
