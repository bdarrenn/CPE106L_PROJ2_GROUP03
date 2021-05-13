import csv

class deleteTrack():
    def __init__(self):
        lines = list()

    def remove_Song(self):
        lines = list()
        print("\n\t------------------------------------------------------------------------------------------------------")
        print("\t|\tTAKE NOTE:                                                                                   |")
        print("\t|\t\tProperly enter the exact name and capitalization of the song.                        |")
        print("\t|\t\tThe program is key sensitive!                                                        |")
        print("\t|\t\tIf the song/artist is not properly typed, the song/artist soundtrack                 |")
        print("\t|\t\twill not be deleted.                                                                 |")
        print("\t|\t\tIf you type the name of the artist, all the songs of the artist will be deleted.     |")
        print("\t|\t\t\t\t                                                                     |")
        deleteVar= input("\t|\tEnter song/artist name to be deleted: ")
        print("\t------------------------------------------------------------------------------------------------------\n")
        with open('MUSIC-DATASET.csv', 'r', encoding="Latin-1") as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)   
                for field in row:
                    if field == deleteVar:
                        lines.remove(row)
                        

        with open('MUSIC-DATASET.csv', 'w', newline='', encoding="Latin-1") as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
            
