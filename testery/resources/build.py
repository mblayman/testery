import falcon

from testery import marshaller
from testery.models import Build


class BuildCollection(object):
    """A set of summary information for builds."""

    def on_get(self, req, resp):
        builds = req.session.query(Build).all()
        req.context['marshalled'] = marshaller.marshall(Build, builds)
        resp.status = falcon.HTTP_200
