from fastapi import FastAPI, Path
from typing import Annotated

users = {'1': 'Имя: Example, возраст: 18'}

app = FastAPI()


@app.get('/users/')
async def main_page() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def add_user(username: Annotated[str, Path(min_length=3, max_length=20, description="Enter Username")],
                   age: Annotated[int, Path(ge=18, le=120, description="Enter age")], ) -> str:
    current_row = str(int(max(users.keys())) + 1)
    users[current_row] = 'Имя: {username}, возраст: {age}'.format(username=username, age=age)
    return 'user {} added'.format(current_row)


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID")],
                      username: Annotated[str, Path(min_length=3, max_length=20, description="Enter Username")],
                      age: Annotated[int, Path(ge=18, le=120, description="Enter age")], ) -> str:
    users[str(user_id)] = 'Имя: {username}, возраст: {age}'.format(username=username, age=age)
    return 'user {} updated'.format(user_id)


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID")], ) -> str:
    del users[str(user_id)]
    return 'user {} deleted'.format(user_id)
