import falcon

from testery.resources.build import BuildCollection
from testery.tests import TestCase


class TestBuildCollection(TestCase):

    def _make_one(self):
        return BuildCollection()

    def test_status_ok(self):
        req = self.factory.make_req()
        resp = self.factory.make_resp()
        resource = self._make_one()
        resource.on_get(req, resp)
        self.assertEqual(falcon.HTTP_200, resp.status)
