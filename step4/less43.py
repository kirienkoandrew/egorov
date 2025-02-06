# Напишите определение классов Song и Playlist
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def __str__(self):
        return f'title: {self.title} - artist: {self.artist}'

class Playlist:
    def __init__(self, songs=None):
        self.songs = []

    def add_song(self, value):
        self.songs.append(value)

    def __str__(self):
        if len(self) == 0:
            return f'Empty playlist'
        else:
            return '\n'.join(map(str, self.songs))

    def __setitem__(self, key, value):
        if key + 1 <= len(self):
            self.songs.insert(key, value)
        else:
            raise KeyError(f'ключ {key} осутствует. общая длина листа {len(self)}')

    def __getitem__(self, key):
        if key <= len(self):
            return self.songs[key]
        else:
            raise KeyError(f'ключ {key} осутствует. общая длина листа {len(self)}')

    def __len__(self):
        return len(self.songs)


# Ниже код для проверки методов классов Song и Playlist


playlist = Playlist()
assert len(playlist.songs) == 0
assert isinstance(playlist, Playlist)
playlist.add_song(Song("Paradise", "Coldplay"))
assert playlist[0].title == 'Paradise'
assert playlist[0].artist == 'Coldplay'
assert len(playlist.songs) == 1

playlist[0] = Song("Resistance", "Muse")
assert playlist[0].title == 'Resistance'
assert playlist[0].artist == 'Muse'
assert playlist[1].title == 'Paradise'
assert playlist[1].artist == 'Coldplay'

playlist[1] = Song("Helena", "My Chemical Romance")
assert playlist[1].title == 'Helena'
assert playlist[1].artist == 'My Chemical Romance'

assert playlist[2].title == 'Paradise'
assert playlist[2].artist == 'Coldplay'
print('Good')