import falcon


class BuildCollection(object):
    """A set of summary information for builds."""

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
