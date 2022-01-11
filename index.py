"""
This file run
the application of server.
"""

from app import app
from utils.db import db

# creating tables
with app.app_context():
  db.create_all()


if __name__ == '__main__':
  # running
  app.run(host = '0.0.0.0', port = 3000, debug = True)