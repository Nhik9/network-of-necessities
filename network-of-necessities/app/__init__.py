from flask import Flask
from app.config import Config

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

current_app = Flask(__name__)
current_app.config.from_object(Config)
db = SQLAlchemy(current_app)
migrate = Migrate(current_app, db)

from app.api import routes
from app import models
