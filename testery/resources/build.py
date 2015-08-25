import json

import falcon

from testery.models import Build


class BuildCollection(object):
    """A set of summary information for builds."""

    def on_get(self, req, resp):
        # TODO: test configuration files
        # TODO: make some marshalling stuff
        builds = req.session.query(Build).all()
        marshalled = {'builds': []}
        for build in builds:
            marshalled['builds'].append({'id': build.id})
        resp.body = json.dumps(marshalled)
        resp.status = falcon.HTTP_200
