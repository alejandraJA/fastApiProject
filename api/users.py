from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    lastName: str
    age: str


user_list = [User(id=1, name="Ale", lastName="JA", age=23),
             User(id=2, name="Ale2", lastName="JA", age=23),
             User(id=3, name="Ale3", lastName="JA", age=23)]


@app.get("/user/")
async def get_all():
    return {"result": user_list}


# Path
@app.get("/user/{id_user}")
async def get_by_path(id_user: int):
    return {"result": get_user(id_user)}


# Query
@app.get("/user")
async def get_by_query(id_user: int):
    return {"result": get_user(id_user)}


@app.post("/user")
async def add(user: User):
    if get_user(user.id) == user:
        return {"result": "User already exist"}
    else:
        user_list.append(user)
        return {"result": "User created!"}


@app.put("/user")
async def update(user: User):
    result = False
    for index, saved_user in enumerate(user_list):
        if saved_user.id == user.id:
            user_list[index] = user
            result = True
    if result:
        return {"result": user}
    else:
        return {"result": "User does not update"}


@app.delete("/user/{id_user}")
async def delete(id_user: int):
    result = False
    for index, saved_user in enumerate(user_list):
        if saved_user.id == id_user:
            del user_list[index]
            result = True
    if result:
        return {"result": "User delete"}
    else:
        return {"result": "User does not exist"}


# Function used by filter Users by id
def get_user(id_user):
    users = filter(lambda user: user.id == id_user, user_list)
    try:
        return list(users)[0]
    except:
        return "User does not exist."
