#!/usr/bin/env python3
'''
database.py
storage connection set up
'''

from ..models import User, Task, TaskList
from ..models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DB():
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('sqlite:///database.db')
   

    @property
    def engine(self):
        return self.__engine


    @property
    def session(self):
        return self.__session

    
    def new(self, obj):
        '''Stages a new object to db'''

        if obj.__class__ not in (Task, User, TaskList):
            raise Exception('DBError: Unsupported object type')
        self.session.add(obj)


    def find_object_by_id(self, cls, _id):
        
        if cls not in (Task, User, TaskList):
            raise Exception('DBError: Unsupported object type')
        return self.session.query(cls).filter_by(id=_id).first()


    def get_all(self, cls):
        
        if cls not in (Task, User, TaskList):
            raise Exception('DBError: Unsupported object type')

        session.query(cls).all()


    def save(self):
        ''' commits changes to the db'''

        self.session.commit()


    def delete(self, obj):
        self.session.remove(obj)
        self.session.commit()


    def reload(self):
        """
        loads data from database.
        """

        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)


db = DB()
db.reload()
