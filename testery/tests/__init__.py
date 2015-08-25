import logging
import os

from paste.deploy.loadwsgi import appconfig

from .. import models, server
from .testcase import TestCase  # noqa


def setup():
    """Prepare to execute tests by setting up the database.

    main does the db configuration. Then the tables need to be created.
    """
    # Hush factory boy.
    logging.getLogger('factory').setLevel(logging.WARN)

    here = os.path.dirname(__file__)
    ini_path = os.path.abspath(os.path.join(here, '..', '..', 'test.ini'))
    settings = appconfig('config:' + ini_path)
    server.main(global_config={}, **settings)

    # Use Base from models to get the benefit of declaring all models.
    models.Base.metadata.create_all()
