import falcon
from falcon import testing


class Factory(object):
    """Factory methods to create helper objects"""

    def make_req(self):
        env = testing.create_environ()
        return falcon.Request(env)

    def make_resp(self):
        return falcon.Response()
