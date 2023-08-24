"""
A script that lists all State objects that contain
the letter a from the database
Database entered by user.
"""
# import needed modules
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == "__main__":
    # get database details from user
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # connect to the database using create engine
    database = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user,
                                                                password,
                                                                db_name)
    engine = create_engine(database)

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # execute query
    main_query = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id).all()

    for item in main_query:
        print("{}: {}".format(item.id, item.name))

    # close session
    session.close()
