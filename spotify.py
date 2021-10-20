import spotipy
import arrow
from dateutil import tz
from .music_service import Music_service

from .utils import convert_ms

class Spotify(Music_service):
  def __init__(self, token):
    self.service_name = "Spotify"
    self.sp = spotipy.Spotify(token)
  
  def user_name(self):
    return self.sp.me()["display_name"]

  def play_times(self):
    now = arrow.now('Asia/Kolkata')
    day = now.replace(hour=0, minute=0).timestamp * 1000
    week = now.floor('week').timestamp * 1000
    month = now.floor('month').timestamp * 1000
    day_tracks = []
    day_play_time = 0
    while arrow.get(day_tracks[-1]["played_at"]) >= now:
      day_tracks.append(self.sp.current_user_recently_played(after=day))
      day = day_tracks[-1]["played_at"]
    for track in day_tracks:
      day_play_time += track["track"]["duration"]
    if day_play_time == 0:
      day_play_time = "You have not listened"
    day_play_time = convert_ms(day_play_time)

  def top_artists(self):
    return self.sp.current_user_top_artists(limit=5, offset=0, time_range='medium_term')

  def top_tracks(self):
    return self.sp.current_user_top_tracks(limit=10, offset=0, time_range='medium_term')