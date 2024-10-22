from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def main_page() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def admin_page() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def user_page(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID")], ) -> dict:
    return {"message": "Вы вошли как пользователь № {}".format(user_id)}


@app.get("/user/{username}/{age}")
async def any_user_page(username: Annotated[str, Path(min_length=3, max_length=20, description="Enter Username")],
                        age: Annotated[int, Path(ge=18, le=120, description="Enter age")], ) -> dict:
    return {"message": "Вы вошли как пользователь {} в возрасте {}".format(username, age)}
