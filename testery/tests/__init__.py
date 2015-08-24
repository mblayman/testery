import sqlalchemy

from .. import db, models
from .testcase import TestCase  # noqa


def setup():
    """Prepare to execute tests by setting up the database."""
    # Set echo to True to view SQL.
    engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)
    db.Session.configure(bind=engine)
    # Use Base from models to get the benefit of declaring all models.
    models.Base.metadata.create_all(engine)
