from sqlalchemy.orm import sessionmaker
from models import User, engine

def get_session():
    Session = sessionmaker(bind=engine)
    return Session()

def add_test_data():
    session = get_session()
    session.add(User(id = 1, tg_id = "@Iamuniicorn", accept_pc=True, phone = '+79175680112'))
    session.commit()

def get_data_user():
    session = get_session()
    users = session.query(User).all()
    for user in users:
        print(user.__dict__)