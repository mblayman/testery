from testery import middleware, request, server
from testery.tests import TestCase


class TestServer(TestCase):

    def test_uses_custom_request(self):
        api = server.make_api()
        self.assertEqual(request.Request, api._request_type)

    def test_has_session_middleware(self):
        api = server.make_api()
        process_req, _, process_resp = api._middleware[0]
        self.assertEqual(middleware.SessionMiddleware, process_req.im_class)
        self.assertEqual(middleware.SessionMiddleware, process_resp.im_class)

    def test_has_json_serializer_middleware(self):
        api = server.make_api()
        _, _, process_resp = api._middleware[1]
        self.assertEqual(
            middleware.JSONSerializerMiddleware, process_resp.im_class)
