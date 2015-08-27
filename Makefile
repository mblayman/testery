serve:
	gunicorn --paste development.ini

cover:
	nosetests --with-coverage --cover-package=testery

db:
	rm -f db.sqlite
	python -m testery.scripts.initializedb
