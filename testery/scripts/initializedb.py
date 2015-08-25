import os

from paste.deploy.loadwsgi import appconfig

from testery import models, server


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

if __name__ == '__main__':
    main()
