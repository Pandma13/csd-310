# Megan Wheeler
# Assignment 8.2
# 30 November 2024

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

def show_films(cursor, title):
    # method to execute an inner join on all tables,
    #   iterate over the dataset and output the results to the terminal window.

    # inner join query
    cursor.execute("Select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")

    # get the results from the cursor object
    films = cursor.fetchall()

    print("\n  -- {} --".format(title))

    # iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

show_films(cursor, "DISPLAYING FILMS")

# insert new film into table
cursor.execute("INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES ('Jurassic Park', '1993', '127', 'Steven Spielberg', '3', '2')")

show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

# change genre for Alien
cursor.execute("UPDATE film SET genre_id = '1' WHERE film_name = 'Alien'")

show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

# delete film Gladiator
cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")

show_films(cursor, "DISPLAYING FILMS AFTER DELETE")