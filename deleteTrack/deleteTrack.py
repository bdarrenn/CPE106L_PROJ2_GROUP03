import csv

class deleteTrack():
    def __init__(self):
        lines = list()

    def remove_Song(self):
        lines = list()
        deleteVar= input("Please enter a song's name or Author's name for the songs to be deleted: ")
        with open('MUSIC-DATASETF.csv', 'r', encoding="Latin-1") as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == deleteVar:
                        lines.remove(row)

        with open('MUSIC-DATASETF.csv', 'w', newline='', encoding="Latin-1") as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
            
def main():
    songList = deleteTrack()
    songList.remove_Song()

if __name__ == "__main__":
    main()