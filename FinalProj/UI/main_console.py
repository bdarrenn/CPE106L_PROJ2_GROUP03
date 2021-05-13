import sys
#the programmer is using hadoop linux directory #change the directory for convenience
sys.path.append('/home/hduser/localrepo/kivy/hive/CPE106L/Project/FinalProj/DA')

from C_INSERT import *
from C_SEARCH import *
from deleteTrack import *
from project_ViewPart import *
from sortingPlaylist import *

def viewSoundtrack():
    songList = viewTrack("", "", "", "", "", "", "")
    songList.assign()
    main()
    return ""

def delSong():
    songList = deleteTrack()
    songList.remove_Song()
    main()
    return ""

def addSoundtrack():
    inserting = Insert()
    inserting.insertTrack()
    main()
    return ""

def searching():
    searchM = Search()
    print("\n\t--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t|\tTAKE NOTE:\t\t\t\t\t\t                                                                                                                                 |")
    print("\t|\t\tProperly enter the exact Song, Artist, Genre, Year, and Album to avoid problems.\t\t\t\t\t\t                                                 |")
    print("\t|\t\tThe program is key sensitive!\t\t\t\t\t\t                                                                                                         |")
    print("\t|\t\tIf you type the wrong option. You will be directed to the Main Option.\t\t\t\t\t\t                                                                 |")
    print("\t|\t\t\t\t\t\t\t\t\t\t                                                                                                                 |")
    print("\t|\tSearch Options:\t\t\t\t\t\t                                                                                                                                 |")
    print("\t|\t\t1. Search Song.\t\t\t\t\t\t                                                                                                                         |")
    print("\t|\t\t2. Search Artist.\t\t\t\t\t\t                                                                                                                 |")
    print("\t|\t\t3. Search Genre.\t\t\t\t\t\t                                                                                                                 |")
    print("\t|\t\t4. Search Year.\t\t\t\t\t\t                                                                                                                         |")
    print("\t|\t\t5. Search Album.\t\t\t\t\t\t                                                                                                                 |")
    print("\t|\t\t\t\t\t\t\t\t\t\t                                                                                                                 |")
    searchChoice = int(input("\t|\tEnter choice: "))

    searchChoices = {
        1: searchM.searchBySong,
        2: searchM.searchByArtist,
        3: searchM.searchByGenre,
        4: searchM.searchByYear,
        5: searchM.searchByAlbum
    }

    finalSearchChoice = searchChoices.get(searchChoice, wrongSearchChoice)()
    print("\t\t", finalSearchChoice)
    print("\t--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    main()
    return ""


def sortTrack():

    sortingTracks = sortPlaylist()
    print("\n--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t-----------------------------------------------------------------")
    print("\t\t| Options:                                                      |")
    print("\t\t|\t1. Sorting the songs by Ascending or Descending order.  |")
    print("\t\t|\t2. Setting a no. of songs to rank.                      |")
    print("\t\t-----------------------------------------------------------------\n")
    pickSort = input("\tEnter Sort Option: ")

    if pickSort == '1':
        sortingTracks.sortSongs()
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        main()
    elif pickSort == '2':
        print("\n--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        sortingTracks.sortRankings()
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        main()
    else:
        wrongSortChoice()
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        main()
    
   
    return ""

def wrongSortChoice():
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n\tInvalid choice. Choice another option in the Main Option.\n")
    main()
    return "" 

def wrongSearchChoice():
    print("\t--------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n\tInvalid choice. Choice another option in the Main Option.\n")
    main()
    return "" 

def wrongChoice():
    print("\n\tInvalid choice. Choice another option.\n")
    main()
    return "" 

def quitProgram():
    print("\n\tThank you for using the program. Have a nice day and goodbye!")
    return "" 

def main(): 
    print("\t-----------------------------------------------------------------------------")
    print("\t|\t\t\t   Welcome to Soundtrack Library                    |")
    print("\t|\t\t\t We have list of songs from 2010 - 2019             |")
    print("\t|\t\t\t\t                                            |")
    print("\t|\t\t\t\t                                            |")
    print("\t|\t\t----------------------------------------------              |")
    print("\t|\t\t|\tOptions:                             |              |")
    print("\t|\t\t|\t\t1. View Sountrack            |              |")
    print("\t|\t\t|\t\t2. Add Soundtrack            |              |")
    print("\t|\t\t|\t\t3. Delete Soundtrack         |              |")
    print("\t|\t\t|\t\t4. Search Soundtrack         |              |")
    print("\t|\t\t|\t\t5. Sorting or Ranking        |              |")
    print("\t|\t\t|\t\t6. Quit                      |              |")
    print("\t|\t\t----------------------------------------------              |")
    print("\t|\t\t\t\t                                            |")
    choice = int(input("\t|\tEnter choice: "))
    print("\t-----------------------------------------------------------------------------")
    choices = {
        1: viewSoundtrack,
        2: addSoundtrack,
        3: delSong,
        4: searching,
        5: sortTrack,
        6: quitProgram
    }
    
    finalChoice = choices.get(choice, wrongChoice)()
    print(finalChoice)
    

    
if __name__ == "__main__":
    main()