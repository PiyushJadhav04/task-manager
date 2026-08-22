from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI()
tasks_db = {0: {"id": 0, "title": "homework", "done": False}}
next_id = 1


class CreateTask(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    done: bool = False

class UpdateTask(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    done: bool = False

class TaskOut(BaseModel):
    id: int 
    title: str
    done: bool


@app.get("/")
def root(): 
    return {"message": "Healthy!"}

@app.get("/tasks")
def get_all_tasks():
    return tasks_db 

@app.post("/tasks", response_model=TaskOut)
def create_task(task: CreateTask):
    global next_id
    new_task = {"id": next_id, "title": task.title, "done": task.done}
    tasks_db[next_id] = new_task
    next_id += 1
    return new_task

@app.get("/tasks/{id}", response_model=TaskOut)
def get_specific_task(id: int):
    if id not in tasks_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return tasks_db[id]

@app.put("/tasks/{id}", response_model=TaskOut)
def edit_task(id: int, task: UpdateTask):
    if id not in tasks_db:
        raise HTTPException(status_code=404, detail="Item not found")
    updated_task = {'id': id, 'title': task.title, 'done': task.done}
    tasks_db[id] = updated_task
    return updated_task

@app.delete("/tasks/{id}")
def delete_task(id: int):
    if id not in tasks_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del tasks_db[id]
    return {"message": "Deleted task"}
