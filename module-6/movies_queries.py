
# Mollee Beck
# November 19, 2026
# Assignment: Movies - Table Queries
# Purpose: Connect to the MySQL movies database and retrieve
# studio, genre, film, and director information using SQL queries.

""" Import statements """
import mysql.connector
from mysql.connector import errorcode

import dotenv
from dotenv import dotenv_values


""" Using our .env file """
secrets = dotenv_values("../module-5/.env")


""" Database configuration """
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}


""" Connect to the movies database """
db = None

try:
    db = mysql.connector.connect(**config)

    print("\n  Successfully connected to the movies database!")

    # Query 1: Display all studio records
    print("\n--- STUDIO TABLE ---")

    cursor = db.cursor()
    cursor.execute("SELECT * FROM studio")

    studios = cursor.fetchall()

    for studio in studios:
        print("Studio ID: {}\nStudio Name: {}\n".format(
            studio[0], studio[1]
        ))

    # Query 2: Display all genre records
    print("\n--- GENRE TABLE ---")

    cursor.execute("SELECT * FROM genre")

    genres = cursor.fetchall()

    for genre in genres:
        print("Genre ID: {}\nGenre Name: {}\n".format(
            genre[0], genre[1]
        ))

    # Query 3: Display movies with a runtime under two hours
    print("\n--- MOVIES UNDER TWO HOURS ---")

    cursor.execute(
        "SELECT film_name, film_runtime FROM film "
        "WHERE film_runtime < 120"
    )

    movies = cursor.fetchall()

    for movie in movies:
        print("Movie: {}\nRuntime: {} minutes\n".format(
            movie[0], movie[1]
        ))

    # Query 4: Display movie names and directors grouped by director
    print("\n--- MOVIES GROUPED BY DIRECTOR ---")

    cursor.execute(
        "SELECT film_name, film_director FROM film "
        "ORDER BY film_director"
    )

    films = cursor.fetchall()

    for film in films:
        print("Movie: {}\nDirector: {}\n".format(
            film[0], film[1]
        ))

except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  Invalid username or password")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    # Close the database connection
    if db is not None and db.is_connected():
        db.close()
        print("\n  MySQL connection closed.")