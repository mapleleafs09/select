import psycopg2
import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://py47:123456@localhost:5432/py47_db')
connection = engine.connect()

year_2018 = connection.execute("""SELECT name, year FROM Albuminfo
    WHERE year = 2018; 
    """).fetchall()
# print(year_2018)

longest_track = connection.execute("""SELECT name, duration FROM Trackinfo
    ORDER BY duration DESC; 
    """).fetchone()
# print(longest_track)

track_more_3_minute_50_sec = connection.execute("""SELECT name, duration FROM Trackinfo
    WHERE duration > '00:03:50' ; 
    """).fetchall()
# print(track_more_3_minute_50_sec)

collections_2018_2020 = connection.execute("""SELECT name FROM Collectioninfo
    WHERE year BETWEEN 2018 AND 2020 ; 
    """).fetchall()
# print(collections_2018_2020)

singername_one_word = connection.execute("""SELECT name FROM Singerinfo
    WHERE name  NOT LIKE '%% %%' ; 
    """).fetchall()
# print(singername_one_word)

track_with_my = connection.execute("""SELECT name FROM Trackinfo
    WHERE name iLIKE '%%my%%' ; 
    """).fetchall()
print(track_with_my)


