import csv
import pandas as pd

class sortPlaylist:
    def __init__(self):
        df = None
    
    def sortSongs(self):
        pd.set_option('display.max_rows', None)
        print("\n\t\t---------------------------------------")
        print("\t\t|   Options:\t                      |")
        print("\t\t|\t1. Ascending Order.           |")
        print("\t\t|\t2. Descending Order.          |")
        print("\t\t---------------------------------------\n")
        x = input("\tEnter choice: ")

        #the programmer is using hadoop linux directory #change the directory for convenience
        df = pd.read_csv('/home/hduser/localrepo/kivy/hive/CPE106L/Project/FinalProj/BL/MUSIC-DATASET.csv')
        print("\n--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        if x == '1':
            df = df.sort_values('Song', ascending=True)
            print(df)
        
        elif x == '2':
            df = df.sort_values('Song', ascending=False)
            print(df)

        else:
            print("Invalid Input. Try Again.")
            
        #the programmer is using hadoop linux directory #change the directory for convenience     
        df.to_csv('/home/hduser/localrepo/kivy/hive/CPE106L/Project/FinalProj/BL/MUSIC-DATASET.csv', index=False)
        return ""

    def sortRankings(self):
        pd.set_option('display.max_rows', None)
        x = int(input('\tEnter the no. of songs you want to rank: '))
        print("\n")

        #the programmer is using hadoop linux directory #change the directory for convenience
        df = pd.read_csv('/home/hduser/localrepo/kivy/hive/CPE106L/Project/FinalProj/BL/MUSIC-DATASET.csv')
        df = df.sort_values('Streams', ascending=False)
        print(df.head(x))
        return ""