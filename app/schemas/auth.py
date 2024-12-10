'''Auth related data schemas for requests and responses'''

from datetime import datetime
from pydantic import BaseModel, EmailStr


# Request schemas
class LoginCreds(BaseModel):
    '''
    User login credential schema download
    '''

    email: EmailStr
    password: str


class RegisCred(BaseModel):
    ''' User account creation credentials'''

    email: EmailStr
    password: str
    username: str


# Response Schemas
class LoginSuccess(BaseModel):
    ''' Login payload schema'''

    id: str
    email: EmailStr
    username: str
    access_token: str
