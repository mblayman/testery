import json

import falcon

from testery.models import Build


class BuildCollection(object):
    """A set of summary information for builds."""

    def on_get(self, req, resp):
        # TODO: make some marshalling stuff
        builds = req.session.query(Build).all()
        marshalled = {'builds': []}
        for build in builds:
            marshalled['builds'].append({
                'id': build.id,
                'passes': build.passes,
                'fails': build.fails,
            })
        req.context['marshalled'] = marshalled
        resp.status = falcon.HTTP_200
