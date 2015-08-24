import falcon


class Request(falcon.Request):

    @property
    def session(self):
        """Get the database session.

        The Falcon Request uses slots so the session can't be
        directly attached to the request. This avoids the
        gnarly syntax of reaching into the context for the session.
        """
        return self.context['session']
