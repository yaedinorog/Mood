from sqlalchemy.orm import sessionmaker
from models import User, engine, user_pair
from sqlalchemy import and_

def get_session():
    Session = sessionmaker(bind=engine)
    return Session()

def add_test_data():
    session = get_session()
    session.add(User(tg_id = "@Iamuniicorn", accept_pc=True, phone = '+79171310112'))
    session.add(User(tg_id="@Bebricks", accept_pc=True, phone='+79173540112'))
    session.commit()

def get_data_user():
    session = get_session()
    users = session.query(User).all()
    for user in users:
        print(user.__dict__)

def checkIfUserExists(tg_id):
    session = get_session()
    existing_user = session.query(User.tg_id).filter(User.tg_id.in_([tg_id])).all()
    return [user for user in existing_user]

def Login(tg_id):
    session = get_session()
    if tg_id[0] != '@':
        raise TypeError
    is_in_db = checkIfUserExists(tg_id)
    if is_in_db:
        print("User correct")
    else:
        raise TypeError

def Registration(tg_id, phone):
    session = get_session()
    if tg_id[0] != '@':
        raise TypeError
    is_in_db = checkIfUserExists(tg_id)
    if is_in_db:
        raise TypeError
    else:
        session.add(User(tg_id=tg_id, accept_pc=True, phone=phone))
        session.commit()
        print("Successfully added")

def AddNewChat(user_id1, user_id2):
    user_id1, user_id2 = min(user_id1, user_id2), max(user_id1, user_id2)
    session = get_session()

    exists = session.query(user_pair).filter(
        and_(
            user_pair.user1_id == user_id1,
            user_pair.user2_id == user_id2
        )
    ).first()

    if not exists:
        # If not exists, insert the pair
        new_pair = user_pair(user_id1=user_id1, user_id2=user_id2)
        session.add(new_pair)
        session.commit()
        print("Pair added to the database.")
    else:
        print("Pair already exists in the database.")