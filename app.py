"""
This file have the configuration for the server.
Only configurations, run with index.py
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.results import results
from config import CONNECTION

# creating
app = Flask(__name__)

# settings
app.config['SQLALCHEMY_DATABASE_URI'] = CONNECTION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)

# routes
app.register_blueprint(results)