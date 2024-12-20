from sqlalchemy.orm import sessionmaker
from models import User, engine, user_pair, chat, mood, Message, attach_type, attach
from sqlalchemy import and_, or_

def get_session():
    Session = sessionmaker(bind=engine)
    return Session()

def add_test_data():
    Registration("@Iamuniicorn", '+75681249530')
    Registration("@Bebricks", '+75681249531')
    Registration("@Vasiliy", '+75681249532')
    AddNewChat(1, 2),
    AddMood("Добрый")
    AddMood("Счастливый")
    AddAttachType("Изображение")
    AddMessage("Дарова, как дела?", 1, 1)

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
            user_pair.user_id1 == user_id1,
            user_pair.user_id2 == user_id2
        )
    ).first()

    if not exists:
        new_pair = user_pair(user_id1=user_id1, user_id2=user_id2)
        session.add(new_pair)
        new_pair_id = session.query(user_pair.id).order_by(user_pair.id.desc()).first()[0]
        new_chat = chat(user_pair_id=new_pair_id, mood_id=None)
        session.add(new_chat)
        session.commit()
        print("Pair added to the database.")

    else:
        print("Pair already exists in the database.")

def GetUserChats(user_id):
    session = get_session()

    pairs = session.query(user_pair.id).filter(
        or_(
            user_pair.user_id1 == user_id,
            user_pair.user_id2 == user_id
        )
    ).all()
    print([i[0] for i in pairs])

def RemoveUserTgId(user_tg_id):
    session = get_session()
    user = session.query(User).filter(User.tg_id == user_tg_id).first()
    if user:
        session.delete(user)
        session.commit()
        print("User deleted.")
    else:
        print("User not found.")

def RemoveUserPhone(phone):
    session = get_session()
    user = session.query(User).filter(User.phone == phone).first()
    if user:
        session.delete(user)
        session.commit()
        print("User deleted.")
    else:
        print("User not found.")

def AddMood(mood_name):
    session = get_session()
    new_mood = mood(name=mood_name)
    session.add(new_mood)
    session.commit()
    print("Mood added.")

def RemoveChatUser(user_id, user_tg_id):
    session = get_session()
    user_id2 = session.query(User).filter(User.tg_id == user_tg_id).first()[0]
    user_pair_to_delete = session.query(user_pair).filter(and_(user_pair.user_id1 == min(user_id, user_id2), user_pair.user_id2 == max(user_id, user_id2))).first()
    chat_to_delete = session.query(chat).filter(chat.user_pair_id == user_pair_to_delete.id).first()
    session.delete(user_pair_to_delete)
    session.delete(chat_to_delete)
    session.commit()

def GetAllMood():
    session = get_session()
    moods = session.query(mood).all()
    for i in moods:
        mod = i.__dict__
        del mod['_sa_instance_state']
        print(mod)

def AddMessage(text, chat_id, user_id, attach_id=None):
    session = get_session()
    if attach_id:
        new_message = Message(text=text, chat_id=chat_id, sender_id=user_id, attach_id=attach_id)
    else:
        new_message = Message(text=text, chat_id=chat_id, sender_id=user_id)
    session.add(new_message)
    session.commit()
    print("Message added.")

def RemoveMessage(message_id):
    session = get_session()
    message = session.query(Message).filter(Message.id == message_id).first()
    if message:
        session.delete(message)
        session.commit()
        print("Message deleted.")
    else:
        print("Message not found.")

def GetChatMessages(chat_id):
    session = get_session()
    messages = session.query(Message.sender_id, Message.text).filter(Message.chat_id == chat_id).all()
    for i in messages:
        msg = i.__dict__
        del msg['_sa_instance_state']
        print(msg)

def AddAttachType(name):
    session = get_session()
    new_attach_type = attach_type(name=name)
    session.add(new_attach_type)
    session.commit()
    print("Attach type added.")

def AddAttachment(file_path, att_type):
    session = get_session()
    new_attach = attach(file_path=file_path, attach_type_id=att_type)
    session.add(new_attach)
    session.commit()
    print("Attach added.")

def RemoveAttachment(attach_id):
    session = get_session()
    att = session.query(attach).filter(attach.id == attach_id).first()
    if att:
        session.delete(att)
        session.commit()
        print("Attach deleted.")
    else:
        print("Attach not found.")