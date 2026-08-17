import string
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI()
tasks_list = {0: {"id": 0, "title": "homework", "done": False}}
num = 1


class CreateTask(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    done: bool = False

class UpdateTask(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    done: bool = False

class TaskDone(BaseModel):
    id: int 
    title: str
    done: bool


@app.get("/")
def root(): 
    return {"message": "Healthy!"}


@app.get("/tasks")
def get_all_tasks():
    return tasks_list 

@app.post("/tasks")
def create_task(task: CreateTask):
    global num
    new_task = {"id": num, "title": task.title, "done": task.done}
    tasks_list[num] = new_task
    num += 1
    return new_task

@app.get("/tasks/{id}")
def get_specific_task(id: int):
    if id not in tasks_list:
        raise HTTPException(status_code=404, detail="Item not found")
    return tasks_list[id]

@app.put("/tasks/{id}")
def edit_task(id: int, task: UpdateTask):
    if id not in tasks_list:
        raise HTTPException(status_code=404, detail="Item not found")
    updated_task = {'id': id, 'title': task.title, 'done': task.done}
    tasks_list[id] = updated_task
    return updated_task

@app.delete("/tasks/{id}")
def delete_task(id: int):
    if id not in tasks_list:
        raise HTTPException(status_code=404, detail="Item not found")
    del tasks_list[id]
    return {"message": "Deleted task"}
