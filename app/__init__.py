from flask import Flask
from flask_bootstrap import Bootstrap
from flask_cors import CORS

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
bootstrap = Bootstrap(app)

from app import routes  # We specify this import later to avoid circular imports
