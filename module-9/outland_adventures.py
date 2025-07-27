""" import statements """
import mysql.connector # to connect
from mysql.connector import errorcode
from tabulate import tabulate

import dotenv # to use .env file
from dotenv import dotenv_values

# using our .env file
secrets = dotenv_values(".env")

""" database config object """
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],    # using the outland database
    "raise_on_warnings": True
}



try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the movies database 

    cursor = db.cursor()    # create a cursor from the database

    # output the connection status 
    print("\n  Database user {} connected to MySQL on host {} with database {}\n".format(config["user"], config["host"], config["database"]))


    def show_all_tables(cursor):
        # get list of all tables
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        for (table_name,) in tables:
            cursor.execute(f"select * from {table_name}")
            rows = cursor.fetchall()

            # get column names for table headers
            headers = [col[0] for col in cursor.description]

            print(f"\n-- {table_name.upper()} Table Data --")
            if rows:
                print(tabulate(rows, headers, tablefmt="grid"))
            else:
                print("\nNo data available")

    show_all_tables(cursor)

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
