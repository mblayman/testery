import json

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

    def test_get(self):
        build_1 = self.factory.make_build(passes=42, fails=1)
        build_2 = self.factory.make_build(passes=43, fails=0)
        req = self.factory.make_req()
        resp = self.factory.make_resp()
        resource = self._make_one()

        resource.on_get(req, resp)

        expected = {
            'builds': [{
                'id': build_1.id,
                'passes': 42,
                'fails': 1,
            }, {
                'id': build_2.id,
                'passes': 43,
                'fails': 0,
            }]
        }
        self.assertEqual(expected, json.loads(resp.body))
