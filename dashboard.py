from flask import (Blueprint, render_template, request, session, url_for, g)

from . import utils

from .spotify import Spotify
from .lastfm import lastfm
from .controller import Controller

# def startController():
music_services = []
c = Controller(music_services)

bp = Blueprint('/dashboard', __name__)

@bp.route('/dashboard')
def dashboard():
  if not c.music_services:
    c.music_services.append(Spotify(session['token']))
    c.music_services.append(lastfm())
  # g.c = startController()
  g.user = c.user_name()
  return render_template("dashboard.html")

@bp.route('/dashboard/play_times')
def top_play_times():
  return c.play_times()

@bp.route('/dashboard/top_artists')
def top_artists():
  return c.top_artists()

@bp.route('/dashboard/top_tracks')
def top_tracks():
  return c.top_tracks()
