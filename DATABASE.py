import sqlite3
import csv

connection = sqlite3.connect("music.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS MUSIC")

musicTable = '''CREATE TABLE MUSIC(
    SONG CHAR(50) , ARTIST CHAR(50), 
    GENRE CHAR(50), YEAR INT, ALBUM CHAR(50), 
    DURATION INT, STREAMS INT
)'''
cursor.execute(musicTable)

with open('MUSIC-DATASET.csv', encoding="utf8") as main_file:
    rows = csv.reader(main_file)
    cursor.executemany("INSERT INTO MUSIC VALUES (?,?,?,?,?,?,?)", rows)

    cursor.execute("SELECT * FROM MUSIC")
    print(cursor.fetchall())

connection.commit()
connection.close()
