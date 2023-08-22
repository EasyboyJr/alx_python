"""
A script that takes 3 argument: mysql username, mysql password and database name,
And list all states from the database.
"""
# import needed modules
import MySQLdb
import sys

if __name__ == "__main__":
    # Get necessary details from the argument provide by user
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # connect to MySQL
    database = MySQLdb.connect(host='localhost', port=3306, user=user, passwd=password, db=db_name)

    # Create cursor
    cur = database.cursor()

    # Time to execute our main task
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # fetch results
    result = cur.fetchall()

    for i in result:
        print(i)
    
    # close connections
    cur.close()
    database.close()