import falcon
from falcon import testing

from testery import db, request


class Factory(object):
    """Factory methods to create helper objects"""

    def make_req(self):
        env = testing.create_environ()
        req = request.Request(env)
        req.context['session'] = db.Session()
        return req

    def make_resp(self):
        return falcon.Response()
