#!/usr/bin/env python3
'''
database.py
storage connection set up
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from .models import User, TaskFolder, Task, Base


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
    

    def reload(self):
        """
        loads data from database.
        """

        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)
