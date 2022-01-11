"""
This file have the routes
for use in the website.
"""

from flask import Blueprint, render_template
from models.physicals import Physicals
from models.quizs import Quizs
from models.physicals import Physicals

results = Blueprint('results', __name__)

@results.route('/')
def home():
  """
  Principal route /
  """

  # getting results for pass to page
  quizs_results = Quizs.query.all()
  physicals_results = Physicals.query.all()

  # changing int to str of note
  for result in quizs_results:
    result.note = int(result.note)

  for result in physicals_results:
    result.note = int(result.note)

  return render_template(
    'index.html',
    quizs_results = quizs_results,
    physicals_results = physicals_results
  )

@results.route('/contacts')
def contacts():
  """
  Route for show the page
  of the contacts
  """

  return render_template('contacts.html')


@results.route('/more')
def more():
  """
  Route for show the page
  of more
  """

  return render_template('more.html')