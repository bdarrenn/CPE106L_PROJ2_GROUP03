import csv

class Search:
    def __init__(self):
        with open('MUSIC-DATASET.csv', encoding="utf8", newline='') as file:
            reader = csv.reader(file)
            self.data = [tuple(row) for row in reader]
    def searchBySong(self):
        song = input("Enter Song Name: ")
        for index, tup in enumerate(self.data):
            if song == tup[0]:
                print(tup)
    def searchByArtist(self):
        year = input(("Enter Artist: "))
        for index, tup in enumerate(self.data):
            if year == tup[1]:
                print(tup)
    def searchByGenre(self):
        year = input(("Enter Genre: "))
        for index, tup in enumerate(self.data):
            if year == tup[2]:
                print(tup)
    def searchByYear(self):
        year = input(("Enter Year: "))
        for index, tup in enumerate(self.data):
            if year == tup[3]:
                print(tup)
    def searchByAlbum(self):
        year = input(("Enter Album: "))
        for index, tup in enumerate(self.data):
            if year == tup[4]:
                print(tup)