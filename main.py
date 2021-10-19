import functools

from flask import (Blueprint, flash,g,render_template,request,session, url_for)

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
  return render_template('index.html')