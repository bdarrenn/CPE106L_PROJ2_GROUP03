import csv

class Search:
    def __init__(self):
        with open('MUSIC-DATASET.csv', encoding="utf8", newline='') as file:
            reader = csv.reader(file)
            self.data = [tuple(row) for row in reader]
    def searchBySong(self):
        song = input("\t\tEnter Song Name: ")
        for index, tup in enumerate(self.data):
            if song == tup[0]:
                print("\t\t", tup)
    def searchByArtist(self):
        year = input(("\t\tEnter Artist: "))
        for index, tup in enumerate(self.data):
            if year == tup[1]:
                print("\t\t",tup)
    def searchByGenre(self):
        year = input(("\t\tEnter Genre: "))
        for index, tup in enumerate(self.data):
            if year == tup[2]:
                print("\t\t", tup)
    def searchByYear(self):
        year = input(("\t\tEnter Year: "))
        for index, tup in enumerate(self.data):
            if year == tup[3]:
                print("\t\t", tup)
    def searchByAlbum(self):
        year = input(("\t\tEnter Album: "))
        for index, tup in enumerate(self.data):
            if year == tup[4]:
                print("\t\t", tup)