import factory
import factory.alchemy
import falcon
from falcon import testing

from testery import db, models, request


class BuildFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = models.Build
        sqlalchemy_session = db.Session


class Factory(object):
    """Factory methods to create helper objects"""

    def make_req(self):
        env = testing.create_environ()
        req = request.Request(env)
        req.context['session'] = db.Session()
        return req

    def make_resp(self):
        return falcon.Response()

    def make_build(self, **kwargs):
        return BuildFactory.create(**kwargs)
