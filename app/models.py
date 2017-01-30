# 3p
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app import app #, db



engine = create_engine('sqlite:////database.db', echo=True)

db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def get_or_create(model, **kwargs):
    """SqlAlchemy implementation of Django's get_or_create.
    """
    session = db.session()
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance

import pdb
pdb.set_trace()
class users(Base):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128))
    name = db.Column(db.String(128))
    surname = db.Column(db.String(128))

    def __init__(self, name=None, email=None, surname=None):
        self.email = email
        self.name = name
        self.surname = surname


class accounts(Base):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(128))
    oauth_token = db.Column(db.String(128))
    user = db.Column(db.Integer, db.ForeignKey(users.id))

    def __init__(self, type=None, oauth_token=None, user=None):
        self.type = type
        self.oauth_token = oauth_token
        self.user = user


class friends(Base):
    __tablename__ = 'friends'

    user_one = db.Column(db.Integer, db.ForeignKey(users.id), primary_key=True)
    user_two = db.Column(db.Integer, db.ForeignKey(users.id), primary_key=True)

    def __init__(self, user_one=None, user_two=None):
        self.user_two = user_two
        self.user_two = user_two

pdb.set_trace()

# Create tables.
Base.metadata.create_all(bind=engine)



