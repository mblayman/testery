from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
Session = orm.scoped_session(orm.sessionmaker())
