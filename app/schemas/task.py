'''Task request and response schemas'''

from datetime import datetime
from pydantic import BaseModel



class TaskCreateRequest(BaseModel):
    '''
    Task create payload schema'''

    description: str
    status: Literal['pending', 'in progress',  'completed'] = 'pending'


class TaskPutRequest(BaseModel):
    description: str | None = None
    status: str | None = None
    parent_id: str | None = None


class TaskResponse(BaseModel):
    '''Task ressponsde schdma'''

    id: str
    description: str
    status: str
    parent_id: str
    created_at: datetime
    updated_at: datetime | None = None
