"""
This file have the model
for the physicals notes.
"""

from utils.db import db

class Physicals(db.Model):
  """
  Model for the notes physicals

  id not null
  name varchar(50)
  note integer
  """

  id = db.Column(db.Integer, primary_key = True)
  student = db.Column(db.String(50))
  note = db.Column(db.Integer)

  def __init__(self, student:str, note:str) -> None:
      # values
      self.student = student
      self.note = note