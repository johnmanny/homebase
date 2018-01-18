# to ensure commands are ran in virtual environment
INENV = . env/bin/activate ;

# make install to make env and install requirements
install: env

env:
	python3 -m venv env
	$(INENV) pip3 install -r requirements.txt

# make run for flask's debug setup unless turned off in config.py
run: 	env
	($(INENV) cd homebase; python flask_main.py) || true

test:	env
	$(INENV) cd server; nosetests

# to freeze requirements in requirements.txt
dist:	env
	$(INENV) pip freeze > requirements.txt

# cleans up the directories
clean:
	rm -f *.pyc */*.pyc
	rm -rf __pycache__ */__pycache__

veryclean:
	make clean
	rm -rf env
