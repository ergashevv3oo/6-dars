from typing import Annotated
from fastapi import FastAPI, Path, Body

import uvicorn

app = FastAPI()

users = [
    {"id": 1, "name": "Ali", "age": 18, "address": "Fergana"},
    {"id": 2, "name": "Vali", "age": 19, "address": "Andijan"},
    {"id": 3, "name": "Toxir", "age": 20, "address": "Namangan"},
    {"id": 4, "name": "Eshmat", "age": 21, "address": "Tashkent"},
    {"id": 5, "name": "Toshmat", "age": 21, "address": "Navoiy"},

]

@app.get("/users/")
def show_users():
    return users

@app.get("/users/{user_id}/")
def get_id(user_id: Annotated[int, Path]) -> dict:
    for user in users:
        if user.get("id") == user_id:
            return user


@app.get("/users/address/{address}")
def get_address(address : Annotated[str, Path]) -> dict:
    for address in users[address]:
        if address == users[address]:
            return address


@app.post("/users/")
def create_user(name: str, age: int, address: str) -> dict:
    users.append(
        {
            "id": len(users) + 1,
            "name": name,
            "age": age,
            "address": address
        }
    )
    return {"message": "User created successully"}