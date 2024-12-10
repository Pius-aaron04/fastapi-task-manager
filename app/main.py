'''entry point'''

from fastapi import FastAPI
from .routers import auth_router, user_router, task_router, task_list_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(task_router)
app.include_router(task_list_router)




if __name__ == 'main':
    import uvicorn

    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)

