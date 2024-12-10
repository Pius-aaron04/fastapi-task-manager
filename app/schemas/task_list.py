'''Task list request and response payload schemas'''
from datetime import datetime
from pydantic import BaseModel


class TaskListCreateRequest(BaseModel):
    '''Task list create request schema'''

    name: str
    description: str | None = None



class TaskListGetResponse(BaseModle):
    ''' task list get response schema'''
    name: str
    description: str
    parentId: str
    sub_lists: list[str] = []
