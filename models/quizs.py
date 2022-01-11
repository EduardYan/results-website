"""
This file have the model
of the note for the database.
"""

from utils.db import db

class Quizs(db.Model):
  """
  Model for the Quiz notes
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