import json

from testery import db


class JSONSerializerMiddleware(object):
    """A middleware to transform a dict result into JSON."""

    def process_response(self, req, resp, resource):
        resp.body = json.dumps(req.context['result'], separators=(',', ':'))

class SessionMiddleware(object):
    """A middleware that attaches scoped sessions to requests."""

    def process_request(self, req, resp):
        """Make a new session and attach it to the request."""
        req.context['session'] = db.Session()

    def process_response(self, req, resp, resource):
        """Tear down the session."""
        db.Session.remove()
