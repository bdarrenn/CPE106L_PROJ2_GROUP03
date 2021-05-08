import csv
import pandas as pd

class sortPlaylist:
    def __init__(self):
        df = None
    
    def sortSong(self):
        df = pd.read_csv('MUSIC-DATASETS.csv')
        df = df.sort_values('Song', ascending=True)
        df.to_csv('MUSTIC-DATASETS.csv', index=False)

    def sortGenre(self):
        df = pd.read_csv('MUSIC-DATASETS.csv')
        df = df.sort_values('Genre', ascending=True)
        df.to_csv('MUSTIC-DATASETS.csv', index=False)

    def sortYear(self):
        df = pd.read_csv('MUSIC-DATASETS.csv')
        df = df.sort_values('Year', ascending=True)
        df.to_csv('MUSTIC-DATASETS.csv', index=False)

    def sortStreams(self):
        df = pd.read_csv('MUSIC-DATASETS.csv')
        df = df.sort_values('Streams', ascending=False)
        df.to_csv('MUSTIC-DATASETS.csv', index=False)

    def sortAlbum(self):
        df = pd.read_csv('MUSIC-DATASETS.csv')
        df = df.sort_values('Album', ascending=True)
        df.to_csv('MUSTIC-DATASETS.csv', index=False)

    def sortDuration(self):
        x = input('1. Ascending\n' '2.Descending\n' 'Enter: ')
        df = pd.read_csv('MUSIC-DATASETS.csv')

        if x == '1':
            df = df.sort_values('Duration (seconds)', ascending=True)
        elif x == '2':
            df = df.sort_values('Duration (seconds)', ascending=False)
        else:
            print("Invalid Input. Try Again.") 

        df.to_csv('MUSTIC-DATASETS.csv', index=False)
