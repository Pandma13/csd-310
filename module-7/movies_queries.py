# Megan Wheeler
# Assignment 7.2
# 11 November 2024

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "GraMoChroiJan10",
    'host': "127.0.0.1",
    "database": 'movies',
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config['database']))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)


cursor = db.cursor()

# Populate studio table
# sql_studio = "INSERT INTO studio (studio_name) VALUES (%s)"

# val_studio = [
#     ['20th Century Fox'],
#     ['Blumhouse Productions'],
#     ['Universal Pictures']
# ]

# cursor.executemany(sql_studio, val_studio)

#db.commit()


# Populate genre table
# sql_genre = "INSERT INTO genre (genre_name) VALUES (%s)"

# val_genre = [
#     ['Horror'],
#     ['SciFi'],
#     ['Drama']
# ]

# cursor.executemany(sql_genre, val_genre)

#db.commit()


# Populate film table
# sql_film = "INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES (%s, %s, %s, %s, %s, %s)"

# val_film = [
#     ('Alien', '1979', '117', 'Ridley Scott', '1', '2'), # SciFi
#     ('Get Out', '2017', '104', 'Jordan Peele', '2', '1'), # Horror
#     ('Gladiator', '2000', '155', 'Ridley Scott', '3', '3') # Drama
# ]

# cursor.executemany(sql_film, val_film)

# db.commit()


# Studio Table
cursor.execute("SELECT studio_id, studio_name FROM studio")

studios = cursor.fetchall()

print("-- DISPLAYING Studio RECORDS --")

for studio in studios:

    print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))


# Genre Table
cursor.execute("SELECT genre_id, genre_name FROM genre")

genres = cursor.fetchall()

print("-- DISPLAYING Genre RECORDS --")

for genre in genres:

    print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))


# Short Film
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")

short_films = cursor.fetchall()

print("-- DISPLAYING Short Film RECORDS --")

for film in short_films:

    print("Film Name: {}\nRuntime: {}\n".format(film[0], film[1]))
    

# Directors in order
cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")

directors = cursor.fetchall()

print("-- DISPLAYING Director RECORDS in Order --")

for film in directors:

    print("Film Name: {}\nDirector: {}\n".format(film[0], film[1]))


db.close()