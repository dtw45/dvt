import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from senseapi import app, db
from senseapi.config import BaseConfig

app.config.from_object('BaseConfig')
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
