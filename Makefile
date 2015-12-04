serve:
	gunicorn --paste development.ini --reload

ember:
	cd client; ember serve

cover:
	nosetests --with-coverage --cover-package=testery

db:
	rm -f db.sqlite
	python -m testery.scripts.initializedb
