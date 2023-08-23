"""
A script that prints the first State object from the database
Database to be entered by user.
"""
# import required modules
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == "__main__":
    # get details from user arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # connect to database using create_engine
    database = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user,
                                                                password,
                                                                db_name)
    engine = create_engine(database)

    # create a session for database
    Session = sessionmaker(bind=engine)
    session = Session()

    # execute query
    main_query = session.query(State).order_by(State.id).first()

    if main_query:
        print("{}: {}".format(main_query.id, main_query.name))
    else:
        print("Nothing")

    # close session
    session.close()
