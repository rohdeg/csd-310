""" import statements """
import mysql.connector # to connect
from mysql.connector import errorcode
from tabulate import tabulate

import dotenv # to use .env file
from dotenv import dotenv_values

#using our .env file
secrets = dotenv_values(".env")

""" database config object """
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True #not in .env file
}

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the movies database 
    
    # output the connection status 
    print("\n  Database user {} connected to MySQL on host {} with database {}\n".format(config["user"], config["host"], config["database"]))

    """ #1: query the studio records """
    print("\n-- Displaying Studio Records --")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM studio;")
    studios = cursor.fetchall()
    print(tabulate(studios, headers=["Studio ID", "Studio Name"]))
    # Without tabulate: for studio in studios: print(f"Studio ID: {studio[0]}\nStudio Name: {studio[1]}\n")

    """ #2: query the genre records """
    print("\n-- Displaying Genre Records --")
    cursor.execute("SELECT * FROM genre;")
    genres = cursor.fetchall()
    print(tabulate(genres, headers=["Genre ID", "Genre Name"]))

    """ #3: movies with runtime < 2 hours """
    print("\n-- Displaying Short Film Records --")
    cursor.execute("""
                   SELECT film_name, film_runtime 
                   FROM film
                   WHERE film_runtime < 120;
                   """)
    films = cursor.fetchall()
    print(tabulate(films, headers=["Film Name", "Runtime"]))

    """ #4: list of film names, and directors grouped by director """
    print("\n-- Displaying Director Records in Order --")
    cursor.execute("""
                   SELECT film_name, film_director 
                   FROM film
                   ORDER BY film_director;
                   """)
    directors = cursor.fetchall()
    print(tabulate(directors, headers=["Film Name", "Director"]))

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)


finally:
    """ close the connection to MySQL """

    db.close()
