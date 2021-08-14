from flask import Flask
from app.config import Config
# import os
#
# current_dir = os.path.abspath(os.path.dirname(__file__))
# db_path = os.path.join(current_dir, 'db.sqlite')

current_app = Flask(__name__)
current_app.config.from_object(Config)
from app.api import routes
