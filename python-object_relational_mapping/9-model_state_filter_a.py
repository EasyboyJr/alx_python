"""
A script that lists all State objects that contain
the letter a from the database
Database entered by user.
"""
# import needed modules
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    # get database details from user
    user = argv[1]
    password = argv[2]
    db_name = argv[3]

    # connect to the database using create engine
    database = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user,
                                                                password,
                                                                db_name)
    engine = create_engine(database)

    # create session
    Session = sessionmaker(bind=engine)
    session = Session

    # execute query
    main_query = session.query(State).filter(State.name.contains('a')).order_by(State.id).all()

    for state in main_query:
        print("{}: {}".format(state.id, state.name))

    # close session
    session.close()
