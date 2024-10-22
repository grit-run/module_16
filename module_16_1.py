from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main_page() -> dict:
    return ({"message": "Главная страница"})


@app.get("/user")
async def any_user_page(username: str = "Аноним",user_id: int = 0, ) -> dict:
    return {"message": "Вы вошли как пользователь {} № {}".format(username, user_id)}


@app.get("/user/admin")
async def admin_page() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def user_page(user_id: int) -> dict:
    return {"message": "Вы вошли как пользователь № {}".format(user_id)}
