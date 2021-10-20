from flask import (Blueprint, render_template, request, session, url_for, g)

from . import utils

bp = Blueprint('/dashboard', __name__)

@bp.route('/dashboard')
def dashboard():
  sp = utils.Spotify(session["token"])
  g.user = sp.user_name()
  # g.play_times = sp.play_times()
  return render_template("dashboard.html")

@bp.route('/dashboard/top_artists')
def top_artists():
  sp = utils.Spotify(session['token'])
  return sp.top_artists()

@bp.route('/dashboard/top_tracks')
def top_tracks():
  sp = utils.Spotify(session['token'])
  return sp.top_tracks()
