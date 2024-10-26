from fastapi import FastAPI, Path, HTTPException, Body, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int
    username: str
    age: int


users: List[User] = []


@app.get('/', response_class=HTMLResponse)
async def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get('/user/{user_id}', response_class=HTMLResponse)
async def get_single_user(request: Request, user_id: Annotated[int, Path(ge=1, le=100)]) -> HTMLResponse:
    return templates.TemplateResponse("user.html", {"request": request, "user": users[user_id]})


@app.post('/user/{username}/{age}')
async def add_user(username: Annotated[str, Path(min_length=3, max_length=20, description="Enter Username")],
                   age: Annotated[int, Path(ge=18, le=120, description="Enter age")], ) -> User:
    current_id = users[-1].id + 1 if users else 1
    users.append(User(id=current_id, username=username, age=age))
    return User(id=current_id, username=username, age=age)
