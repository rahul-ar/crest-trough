from abc import ABC, abstractmethod

class Music_service (ABC):
    @abstractmethod
    def user_name(self):
        pass

    @abstractmethod
    def play_times(self):
        pass

    @abstractmethod
    def top_artists(self):
        pass

    @abstractmethod
    def top_tracks(self):
        pass
