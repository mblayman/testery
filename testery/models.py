import sqlalchemy as sa

from .db import Base


class Build(Base):
    """A build is an instance of a test run reported by a project."""
    __tablename__ = 'builds'

    id = sa.Column(sa.Integer, primary_key=True)
    passes = sa.Column(sa.Integer, default=0)
    fails = sa.Column(sa.Integer, default=0)
    skips = sa.Column(sa.Integer, default=0)
