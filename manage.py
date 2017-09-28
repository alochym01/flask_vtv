from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)

# load all config for flask framework
app.config.from_object('config.settings')
# override config settings for production using instance/settings.py file
app.config.from_pyfile('settings.py', silent=True)

# initial database
db = SQLAlchemy()

# import all models right here
from flask_app.models.users import *

# initial migrate
migrate = Migrate(app, db)

# initial script
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
