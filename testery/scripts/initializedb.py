import os

from paste.deploy.loadwsgi import appconfig

from testery import db, models, server


def main():
    """Initialize a development database."""
    here = os.path.dirname(__file__)
    ini_path = os.path.abspath(os.path.join(here, '..', '..', 'development.ini'))
    settings = appconfig('config:' + ini_path)
    # Show the SQL to see table creation output.
    settings['sqlalchemy.echo'] = True
    server.main(global_config={}, **settings)

    # # Use Base from models to get the benefit of declaring all models.
    models.Base.metadata.create_all()

    session = db.Session()
    session.add(models.Build(passes=42, fails=4))
    session.add(models.Build(passes=52, fails=2))
    session.add(models.Build(passes=62, fails=1))
    session.commit()


if __name__ == '__main__':
    main()
