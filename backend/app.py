import string
from fastapi import FastAPI, HTTPException


app = FastAPI()
tasks_list = {0 : 'homework'}
num = 1


@app.get("/")
def root(): 
    return {"message": "Healthy!"}


@app.get("/tasks")
def get_all_tasks():
    return tasks_list 

@app.post("/tasks")
def create_task(task: str):
    global num
    tasks_list[num] = task
    num += 1
    return {"message": "Task Created"}

@app.get("/tasks/{id}")
def get_specific_task(id: int):
    if id not in tasks_list:
        raise HTTPException(status_code=404, detail="Item not found")
    return tasks_list[id]

@app.put("/tasks/{id}")
def edit_task(id: int, message: str):
    if id not in tasks_list:
        raise HTTPException(status_code=404, detail="Item not found")
    tasks_list[id] = message 
    return {"message": "Edited"}

@app.delete("/tasks/{id}")
def delete_task(id: int):
    if id not in tasks_list:
        raise HTTPException(status_code=404, detail="Item not found")
    del tasks_list[id]
    return {"message": "Deleted task"}
