from flask import Flask, render_template

from .exts.extensions import debug_toolbar, db, login_manager

# absolute import way
# from blueprints.users.view import user

# relative import way
from .views.users import users


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # load all config for flask framework
    app.config.from_object('config.settings')
    # override config settings for production using instance/settings.py file
    app.config.from_pyfile('settings.py', silent=True)

    # register blueprints modules
    app.register_blueprint(users)

    # initial env for all flask extensions/
    debug_toolbar.init_app(app)

    db.init_app(app)

    login_manager.init_app(app)

    @app.route('/')
    def index():
        return render_template('home.html')

    return app
