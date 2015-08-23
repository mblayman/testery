import falcon

from testery.resources import build


def main(global_config, **settings):
    """Make the API WSGI application.

    This method signature follows the paste.app_factory protocol
    for Paste Deploy.
    """
    api = falcon.API()

    build_collection = build.BuildCollection()
    api.add_route('/builds', build_collection)

    return api
