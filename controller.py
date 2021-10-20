

class Controller:
    def __init__(self, music_services):
        self.music_services = music_services
    
    def user_name(self):
        user_names = ''
        for i in self.music_services:
            user_names += i.user_name() + ' / '

        return user_names[:-2]

    def play_times(self):
        play_times = {}
        for i in self.music_services:
            play_times[i.service_name] = i.play_times()
        
        return play_times

    def top_artists(self):
        top_artists = {}
        for i in self.music_services:
            top_artists[i.service_name] = i.top_artists()

        return top_artists
    
    def top_tracks(self):
        top_tracks = {}
        for i in self.music_services:
            top_tracks[i.service_name] = i.top_tracks()

        return top_tracks