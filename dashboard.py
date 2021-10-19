from flask import (Blueprint, render_template, request, session, url_for, g)

from . import utils

bp = Blueprint('/dashboard', __name__)

@bp.route('/dashboard')
def dashboard():
  sp = utils.Spotify(session["token"])
  g.user = sp.user_name()
  g.play_times = sp.play_times()
  print(g.user)
  return render_template("dashboard.html")
