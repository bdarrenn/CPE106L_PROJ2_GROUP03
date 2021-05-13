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
        #using hadoop linux directory #change the directory for convenience
        with open('/home/hduser/localrepo/kivy/hive/CPE106L/Project/MUSIC-DATASET.csv', 'r') as playlist:
            reader = csv.reader(playlist, delimiter=",")
            print(reader)
            print("-----------------------------------------------------------------------------SOUNDTRACKS------------------------------------------------------------------------------------------------------------------")
            for i in reader:
                self.song = i[0]
                self.artist = i[1] 
                self.genre = i[2] 
                self.year = i[3]
                self.album = i[4]
                self.duration = i[5] 
                self.stream = i[6] 
                '''print(f'{self.song:<40}', f'{self.artist:^25}', f'{self.genre:^25}', f'{self.year:^20}', f'{self.album:^40}', f'{self.duration:^20}', f'{self.stream:^20}'"\n")
            print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                '''
def main(): 
    songList = viewTrack("", "", "", "", "", "", "")
    songList.assign()




if __name__ == "__main__":
    main()
    

