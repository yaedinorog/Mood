from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date, create_engine

DATABASE_URL = "sqlite:///example.db"

engine = create_engine(DATABASE_URL)

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    tg_id = Column(String)
    accept_pc = Column(Boolean)
    phone = Column(String)

class user_pair(Base):
    __tablename__ = 'user_pair'

    id = Column(Integer, primary_key=True)
    user_id1 = Column(Integer, ForeignKey('User.id'))
    user_id2 = Column(Integer, ForeignKey('User.id'))

class mood(Base):
    __tablename__ = 'mood'

    id = Column(Integer, primary_key=True)
    name = Column(String)

class chat(Base):
    __tablename__ = 'chat'

    id = Column(Integer, primary_key=True)
    user_pair_id = Column(Integer, ForeignKey('user_pair.id'))
    mood_id = Column(Integer, ForeignKey('mood.id'))

class history_mood(Base):
    __tablename__ = 'history_name'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    chat_id = Column(Integer, ForeignKey('chat.id'))
    mood_id = Column(Integer, ForeignKey('mood.id'))

class attach_type(Base):
    __tablename__ = 'attach_type'

    id = Column(Integer, primary_key=True)
    name = Column(String)

class attach(Base):
    __tablename__ = 'attach'

    id = Column(Integer, primary_key=True)
    attach_type_id = Column(Integer, ForeignKey('attach_type.id'))
    file_path = Column(String)

class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, ForeignKey('chat.id'))
    sender_id = Column(Integer, ForeignKey('User.id'))
    text = Column(String)
    attach_id = Column(Integer, ForeignKey('attach.id'))

def create_tables():
    Base.metadata.create_all(engine)