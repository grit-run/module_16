from fastapi import FastAPI, Path, HTTPException, Body
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    age: int


users: List[User] = []


@app.get('/users/')
async def main_page() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def add_user(username: Annotated[str, Path(min_length=3, max_length=20, description="Enter Username")],
                   age: Annotated[int, Path(ge=18, le=120, description="Enter age")], ) -> User:
    current_id = users[-1].id + 1 if users else 1
    users.append(User(id=current_id, username=username, age=age))
    return User(id=current_id, username=username, age=age)


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(description="real user ID")],
                      username: Annotated[str, Path(min_length=3, max_length=20, description="Enter Username")],
                      age: Annotated[int, Path(ge=18, le=120, description="Enter age")]) -> User:
    try:
        user = (user for user in users if user.id == user_id).__next__()
        user.username = username
        user.age = age
        return user
    except StopIteration:
        raise HTTPException(status_code=404, detail="User was not exist")


@app.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[int, Path(description="real user ID")]) -> User:
    try:
        user = (user for user in users if user.id == user_id).__next__()
        users.remove(user)
        return user
    except StopIteration:
        raise HTTPException(status_code=404, detail="User was not exist")
