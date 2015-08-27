import falcon
import sqlalchemy

from testery import db, middleware, request
from testery.resources import build


def main(global_config, **settings):
    """Make the API WSGI application.

    This method signature follows the paste.app_factory protocol
    for Paste Deploy.
    """
    configure_db(settings)
    api = make_api()
    set_routes(api)
    return api


def configure_db(settings):
    engine = sqlalchemy.engine_from_config(settings)
    db.Session.configure(bind=engine)
    db.Base.metadata.bind = engine


def make_api():
    api = falcon.API(request_type=request.Request, middleware=[
        middleware.SessionMiddleware(),
        middleware.JSONSerializerMiddleware(),
    ])
    return api


def set_routes(api):
    build_collection = build.BuildCollection()
    api.add_route('/builds', build_collection)
