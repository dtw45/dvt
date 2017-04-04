VENV=./flask/venv
REQUIREMENTS=./senseapi/requirements.txt
RUNSCRIPT=./run.py

install: $(REQUIREMENTS)
	test -d $(VENV) || virtualenv $(VENV)
	$(VENV)/bin/pip install -Ur $(REQUIREMENTS)
	touch $(VENV)/bin/activate

run:
	python $(RUNSCRIPT)

create-tables:
	python -m senseapi.scripts.db_create

drop-tables:
	python -m senseapi.scripts.db_drop

