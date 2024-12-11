'''Auth service to manage auth related operations'''

from ..models import User
from ..utils.database import db
from ..utils.auth import Hasher


class AuthService:
    '''Authentication service'''

    @staticmethod
    def register_user(user: dict) -> User:
        '''creates a user instance and'''

        user_obj = User(**user)
        user_obj.password = Hasher.hash_password(user['password'])

        db.new(user_obj)
        db.save()

        return user_obj

    @staticmethod
    def login_user(cred: dict) -> dict:
        '''logs in user'''

        user = db.session.query(User).filter_by(email=cred['email']).first()
        if not user:
            return None

        print(type(user.password))
        print(cred['password'])

        verified = Hasher.check_pwd(cred['password'], user.password)

        if not verified:
            return None
        return user.to_dict()
