serve:
	gunicorn --paste development.ini

cover:
	nosetests --with-coverage --cover-package=testery
