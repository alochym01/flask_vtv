# all extensions of flask should import here

from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager

# initial debug_toolbar
debug_toolbar = DebugToolbarExtension()

# initial database
db = SQLAlchemy()

login_manager = LoginManager()
