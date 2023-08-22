"""
a script that lists all states with a name starting with N.
"""
# import required modules
import MySQLdb
import sys

if __name__ == "__main__":
    # retrieve details from user argument.
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    
    # connect to MySQL
    database = MySQLdb.connect(host='localhost',
                               port=3306,
                               user=user,
                               passwd=password,
                               db=db_name)
    
    # create a cursor
    cursor = database.cursor()

    # select states that start with N
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Return results
    result = cursor.fetchall()

    for item in result:
        print(item)
    
    # close connections
    cursor.close()
    database.close()
