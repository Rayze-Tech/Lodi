import os
from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
basedir = os.path.abspath(os.path.dirname(__file__))

#app = Flask(__name__)
app = Flask(__name__, static_url_path="/static")
app.config.from_object(Config)
bootstrap=Bootstrap(app)

from app import routes
