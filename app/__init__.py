import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

from app import routes  # nopep8

login.login_view = 'login'

app.config['TEMPLATES_AUTO_RELOAD'] = True


if __name__ == '__main__':
    app.run()
