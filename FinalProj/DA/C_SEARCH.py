import csv

class Search:
    def __init__(self):
        #the programmer is using hadoop linux directory #change the directory for convenience
        with open('/home/hduser/localrepo/kivy/hive/CPE106L/Project/FinalProj/BL/MUSIC-DATASET.csv', encoding="utf8", newline='') as file:
            reader = csv.reader(file)
            self.song = [tuple(row) for row in reader]
            self.artist = [tuple(row) for row in reader]
            self.genre = [tuple(row) for row in reader]
            self.year = [tuple(row) for row in reader]
            self.album = [tuple(row) for row in reader]
            self.duration = [tuple(row) for row in reader]
            self.stream = [tuple(row) for row in reader]
    def searchBySong(self):
        songPick = input("\t|\tEnter Song Name: ")
        for index, tup in enumerate(self.song):
            if songPick == tup[0]:
                self.song = tup[0]
                self.artist = tup[1]
                self.genre = tup[2]
                self.year = tup[3]
                self.album = tup[4]
                self.duration = tup[5]
                self.stream = tup[6]
                print("\t|",f'{self.song:^42}', f'{self.artist:^20}', f'{self.genre:^25}', f'{self.year:>8}', f'{self.album:^42}', f'{self.duration:>10}', f'{self.stream:>19}',f'{"|":>19}')
        return ""
    def searchByArtist(self):
        artistPick = input(("\t|\tEnter Artist name: "))
        for index, tup in enumerate(self.song):
            if artistPick == tup[1]:
                self.song = tup[0]
                self.artist = tup[1]
                self.genre = tup[2]
                self.year = tup[3]
                self.album = tup[4]
                self.duration = tup[5]
                self.stream = tup[6]
                print("\t|",f'{self.song:^42}', f'{self.artist:^25}', f'{self.genre:^25}', f'{self.year:>8}', f'{self.album:^42}', f'{self.duration:>15}', f'{self.stream:>19}',f'{"|":>9}')
        return ""
    
    def searchByGenre(self):
        genrePick = input(("\t|\tEnter Genre: "))
        for index, tup in enumerate(self.song):
            if genrePick == tup[2]:
                self.song = tup[0]
                self.artist = tup[1]
                self.genre = tup[2]
                self.year = tup[3]
                self.album = tup[4]
                self.duration = tup[5]
                self.stream = tup[6]
                print("\t|",f'{self.song:^42}', f'{self.artist:^25}', f'{self.genre:^25}', f'{self.year:>8}', f'{self.album:^42}', f'{self.duration:>15}', f'{self.stream:>19}',f'{"|":>9}')
        return ""

    def searchByYear(self):
        yearPick = input(("\t|\tEnter Year: "))
        for index, tup in enumerate(self.song):
            if yearPick == tup[3]:
                self.song = tup[0]
                self.artist = tup[1]
                self.genre = tup[2]
                self.year = tup[3]
                self.album = tup[4]
                self.duration = tup[5]
                self.stream = tup[6]
                print("\t|",f'{self.song:^42}', f'{self.artist:^25}', f'{self.genre:^25}', f'{self.year:>8}', f'{self.album:^42}', f'{self.duration:>15}', f'{self.stream:>19}',f'{"|":>9}')
        return ""

    def searchByAlbum(self):
        albumPick = input(("\t|\tEnter Album: "))
        for index, tup in enumerate(self.song):
            if albumPick == tup[4]:
                self.song = tup[0]
                self.artist = tup[1]
                self.genre = tup[2]
                self.year = tup[3]
                self.album = tup[4]
                self.duration = tup[5]
                self.stream = tup[6]
                print("\t|",f'{self.song:^42}', f'{self.artist:^25}', f'{self.genre:^25}', f'{self.year:>8}', f'{self.album:^42}', f'{self.duration:>15}', f'{self.stream:>19}',f'{"|":>9}')
        return ""
