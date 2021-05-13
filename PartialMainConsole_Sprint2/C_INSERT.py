import csv

class Insert:
    def __init__(self):
        list = []
    def insertTrack(self):
        print("\n\t-----------------------------------------------------------------------------")
        song = input("\t|\tEnter Song Title: ")
        artist = input("\t|\tEnter Song Artist: ")
        genre = input("\t|\tEnter Song Genre ")
        year = input("\t|\tEnter Song Year: ")
        album = input("\t|\tEnter Song Album: ")
        duration = input("\t|\tEnter Song Duration(seconds): ")
        streams = input("\t|\tEnter Stream Count: ")
        print("\t-----------------------------------------------------------------------------")
        self.list =[song, artist, genre, year, album, duration, streams]
        with open('MUSIC-DATASET.csv', 'a', newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(self.list)
            print("\n\t\tTrack Added Successfully\n")

