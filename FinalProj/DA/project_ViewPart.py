import csv 

class viewTrack:
    def __init__(self,song,artist,genre,year,album,duration,stream):
        self.song = song
        self.artist = artist
        self.genre = genre 
        self.year = year
        self.album = album
        self.duration = duration
        self.stream = stream

    def assign(self):
        #the programmer is using hadoop linux directory #change the directory for convenience
        with open('/home/hduser/localrepo/kivy/hive/CPE106L/Project/FinalProj/BL/MUSIC-DATASET.csv', 'r') as playlist:
            reader = csv.reader(playlist, delimiter=",")
            print("\n------------------------------------------------------------------------------SOUNDTRACKS-------------------------------------------------------------------------------------------------------------------")
            for i in reader:
                self.song = i[0]
                self.artist = i[1] 
                self.genre = i[2] 
                self.year = i[3]
                self.album = i[4]
                self.duration = i[5] 
                self.stream = i[6] 
                print(f'{"|":<}',f'{self.song:<40}', f'{self.artist:^25}', f'{self.genre:^25}', f'{self.year:^20}', f'{self.album:^43}', f'{self.duration:^20}', f'{self.stream:^20}',f'{"|":>3}')
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                


