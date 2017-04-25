MANAGER=./manage.py

VENV=./flask/venv
REQUIREMENTS=./sensor_api/requirements.txt

RUNSCRIPT=./run.py
CREATE_TABLE_SCRIPT=sensor_api.scripts.db_create
DROP_TABLE_SCRIPT=sensor_api.scripts.db_drop

###########################################
# Installer
###########################################
inst: $(REQUIREMENTS)
	pip install virtualenv
	pip install virtualenvwrapper
	git clone git://github.com/kennethreitz/autoenv.git ~/.autoenv

setup-bashrc:
	echo '
	# Setup Virtualenvwrapper
	export PATH="/usr/local/bin:$PATH"
	export WORKON_HOME="~/Envs"
	source "/usr/local/bin/virtualenvwrapper.sh"

	# Setup AutoEnv
	source ~/.autoenv/activate.sh
	' >> ~/.bashrc
	source ~/.bashrc


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
create-tables: 
	python -m $(CREATE_TABLE_SCRIPT)

drop-tables:
	python -m $(DROP_TABLE_SCRIPT)

###########################################
# Flask Migrate Operations
###########################################

# Create migration files based on models
migrate: $(MANAGER)
	python $(MANAGER) db migrate

# Apply unapplied migrations
upgrade: $(MANAGER)
	python $(MANAGER) db upgrade

# Undo last migration
downgrade: $(MANAGER)
	python $(MANAGER) db downgrade

