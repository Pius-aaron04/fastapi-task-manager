''' User data schema'''

from pydantic import BaseModel
from datetime import datetime


class UserResponse(BaseModel):
    id: str
    username: str
    email: str
    created_at: datetime
    updated_at: datetime
