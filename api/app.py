from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    salary: int
    bonus: int
    taxes: int



@app.get("/items/{salary, bonus,taxes}")
def count_net():
    return {"result": 2300 // salary + bonus - taxes}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"result": item_name, "item_id": item_id}