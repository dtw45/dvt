MANAGER=./manage.py

VENV=./flask/venv
REQUIREMENTS=./sensor_api/requirements.txt

RUNSCRIPT=./run.py
CREATE_TABLE_SCRIPT=sensor_api.scripts.db_create
DROP_TABLE_SCRIPT= sensor_api.scripts.db_drop

###########################################
# Installer
###########################################
install: $(REQUIREMENTS)
	test -d $(VENV) || virtualenv $(VENV)
	$(VENV)/bin/pip install -Ur $(REQUIREMENTS)
	touch $(VENV)/bin/activate

###########################################
# Runners
###########################################
run: $(RUNSCRIPT)
	python $(RUNSCRIPT)

###########################################
# Database Operations
###########################################
create-tables: $(CREATE_TABLE_SCRIPT)
	python -m $(CREATE_TABLE_SCRIPT)

drop-tables: $(DROP_TABLE_SCRIPT)
	python -m $(DROP_TABLE_SCRIPT)

###########################################
# Flask Migrate Operations
###########################################

# Create migration files based on models
migrate:
	python $(MANAGER) db migrate

# Apply unapplied migrations
upgrade:
	python $(MANAGER) db upgrade

