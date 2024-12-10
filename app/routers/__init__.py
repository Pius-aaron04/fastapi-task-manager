from .auth import router as auth_router
from .user import router as user_router
from .task import router as task_router
from .task_list import router as task_list_router


__all__ = ["auth_router", "user_router", "task_router",
           "task_list_router"]
