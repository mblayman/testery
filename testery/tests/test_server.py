from testery import request, server
from testery.tests import TestCase


class TestServer(TestCase):

    def test_uses_custom_request(self):
        api = server.make_api()
        self.assertEqual(request.Request, api._request_type)
