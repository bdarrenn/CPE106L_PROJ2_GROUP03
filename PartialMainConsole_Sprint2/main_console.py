from project_ViewPart import *
from deleteTrack import *
from C_SEARCH import *
from C_INSERT import *

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
    print("\n\t--------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t|\tTAKE NOTE:                                                                                                                               |")
    print("\t|\t\tProperly enter the exact Song, Artist, Genre, Year, and Album to avoid problems.                                                 |")
    print("\t|\t\tThe program is key sensitive!                                                                                                    |")
    print("\t|\t\tIf you type the wrong option. You will be directed to the Main Option.                                                           |")
    print("\t|\t\t\t\t                                                                                                                 |")
    print("\t|\tSearch Options:                                                                                                                          |")
    print("\t|\t\t1. Search Song.                                                                                                                  |")
    print("\t|\t\t2. Search Artist.                                                                                                                |")
    print("\t|\t\t3. Search Genre.                                                                                                                 |")
    print("\t|\t\t4. Search Year.                                                                                                                  |")
    print("\t|\t\t5. Search Album.                                                                                                                 |")
    print("\t|\t\t\t\t                                                                                                                 |")
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
    print("\t--------------------------------------------------------------------------------------------------------------------------------------------------")
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
    print("\t|\t\t|\t\t5. Soundtrack Ranking        |              |")
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
        6: quitProgram
    }
    
    finalChoice = choices.get(choice, wrongChoice)()
    
    print(finalChoice)
    
    
if __name__ == "__main__":
    main()