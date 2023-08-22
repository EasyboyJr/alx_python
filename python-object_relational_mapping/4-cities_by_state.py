"""
A script that lists all cities from the database.
"""
# import required moduled
import MySQLdb
import sys

if __name__ == "__main__":
    # retrieve details from user argument
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

    # execute main task
    cursor.execute(
        """SELECT cities.id, cities.name, states.name
        FROM cities, states
        WHERE states.id = state_id
        ORDER BY cities.id ASC"""
    )

    # return results
    result = cursor.fetchall()

    for item in result:
        print(item)

    # close connections
    cursor.close()
    database.close()
