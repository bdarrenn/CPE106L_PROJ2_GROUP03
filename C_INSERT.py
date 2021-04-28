import csv

class Insert:
    def __init__(self, song, artist, genre, year, album, duration, streams):
        self.song = song
        self.artist = artist
        self.genre = genre
        self.year = year
        self.album = album
        self.duration = duration
        self.streams = streams
    def insertTrack(self):
        with open('MUSIC-DATASET.csv', 'a', newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow([self.song, self.artist, self.genre, self.year, self.album, self.duration, self.streams])