from project.song import Song


class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.published = False
        self.songs = []
        for song in songs:
            self.add_song(song)

    def add_song(self, song: Song):
        if song.single:
            return f'Cannot add {song.name}. It\'s a single'
        if self.published:
            return 'Cannot add songs. Album is published.'
        if song.name in map(lambda s: s.name, self.songs):
            return 'Song is already in the album.'

        self.songs.append(song)
        return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name: str):
        if self.published:
            return 'Cannot remove songs. Album is published.'

        songs = [song.name for song in self.songs]
        if song_name not in songs:
            return 'Song is not in the album.'

        del self.songs[songs.index(song_name)]
        return f'Removed song {song_name} from album {self.name}.'

    def publish(self):
        if not self.published:
            self.published = True
            return f'Album {self.name} has been published.'

        return f'Album {self.name} is already published.'

    def details(self):
        album_name = [f'Album {self.name}']
        album_songs = [f'== {song.get_info()}' for song in self.songs]
        return '\n'.join(album_name + album_songs) + '\n'
