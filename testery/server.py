import falcon

from testery.resources import build

application = falcon.API()

build_collection = build.BuildCollection()
application.add_route('/builds', build_collection)
