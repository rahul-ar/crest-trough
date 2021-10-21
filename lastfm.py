import pylast

import calendar
import datetime as dt

from .music_service import Music_service

class lastfm(Music_service):
    def __init__(self):
        self.service_name = "Last.fm"
        self.API_KEY = "e64588b7955f4fb940fb3cd3b11de6ad"
        self.API_SECRET = "a078c0fe139bde012830f0fb0576131f"

        self.username = "eyelashwash"
        self.password_hash = pylast.md5("eyelashwash1!")

        self.network = pylast.LastFMNetwork(
            api_key=self.API_KEY,
            api_secret=self.API_SECRET,
            username=self.username,
            password_hash=self.password_hash,
        )
        self.user = self.network.get_user(self.username)
    
    def user_name(self):
        return self.username
    
    def like(self, artist="Iron Maiden", title="The Nomad"):
        track = self.network.get_track(artist, title)
        track.love()

    def unlike(self, artist="Iron Maiden", title="The Nomad"):
        track = self.network.get_track(artist, title)
        track.unlove()
    
    def top_artists(self):
        artists = self.user.get_top_artists()
        artists = [item[0].get_name() for item in artists]
        return artists

    def top_albums(self):
        albums = self.user.get_top_albums()
        return albums

    def top_tracks(self):
        tracks = self.user.get_top_tracks()
        tracks = [item[0].get_name() for item in tracks]
        return tracks

    def play_times(self, year, month, day):
        start = dt.datetime(year, month, day, 0, 0)
        end = dt.datetime(year, month, day, 23, 59)

        utc_start = calendar.timegm(start.utctimetuple())
        utc_end = calendar.timegm(end.utctimetuple())

        tracks = self.user.get_recent_tracks(time_from=utc_start, time_to=utc_end)
        return tracks
