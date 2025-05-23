#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base
from user import User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ adds a user to the DB
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwords) -> User:
        """ finds user by an arbitrary keyword
        """
        result = self._session.query(User).filter_by(**kwords).one()
        return result

    def update_user(self, user_id: int, **kwords) -> None:
        """ update users by id
        """
        col_names = User.__table__.columns.keys()
        for key in kwords.keys():
            if key not in col_names:
                raise ValueError

        user = self.find_user_by(id=user_id)
        for key, val in kwords.items():
            setattr(user, key, val)
        self._session.commit()
        return None
