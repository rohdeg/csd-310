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

    cursor = db.cursor()    # create a cursor from the database

    # output the connection status 
    print("\n  Database user {} connected to MySQL on host {} with database {}\n".format(config["user"], config["host"], config["database"]))


    def show_films(cursor, title):
        # method to execute an inner join on all tables,
        #   iterate over dataset and output results in terminal window

        # inner join query
        cursor.execute("""
            select film_name Name, film_director Director, genre_name Genre, studio_name 'Studio Name'
            from film f inner join genre g on f.genre_id = g.genre_id inner join studio s on f.studio_id = s.studio_id;
        """)

        # get results
        films = cursor.fetchall()

        # display the results
        print("\n -- {} --".format(title))
        print(tabulate(films, headers=["Name", "Director", "Genre", "Studio Name"]))


    # step 5: display films
    show_films(cursor, "DISPLAYING FILMS")

    # step 6: insert into film
    cursor.execute("""
        insert into film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
            values ("Insidious", "2011", 103, "James Wan", 2, 1)
    """)

    # step 7: display films after insert
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # step 8: update Alien to be a horror film
    cursor.execute("""
        update film
        set genre_id = 1
        where film_id = 2;
    """)

    # step 9: display films after update
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")

    # step 10: delete Gladiator
    cursor.execute("delete from film where film_id = 1;")

    # step 11: display film after deletion
    show_films(cursor, "DISPLAYING FILMS AFTER DELETION")

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
