"""
A script that takes in the name of a state as an argument
and lists all cities of that state, using the database
"""
# import needed modules
import MySQLdb
import sys

if __name__ == "__main__":
    # Get details from user arguments.
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # connect to MySQL
    database = MySQLdb.connect(host='localhost',
                               port=3306,
                               user=user,
                               passwd=password,
                               db=db_name
                               )

    # create cursor
    cursor = database.cursor()

    # executing main task
    main_query = ("SELECT cities.name FROM cities\
                  JOIN states ON cities.state_id = states.id\
                  WHERE states.name LIKE %s\
                  ORDER BY cities.id ASC"
    )
    cursor.execute(main_query, (state_name))

    # return results
    result = cursor.fetchall()
    list = []

    for item in result:
        list.append(result[0])
    print(", ".join(list))

    # close connections
    cursor.close()
    database.close()
