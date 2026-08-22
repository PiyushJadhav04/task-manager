from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from database import get_db, init_db, Task as TaskModel
from sqlalchemy.orm import Session

#initializes database
init_db()

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
def get_all_tasks(db: Session = Depends(get_db)):
    tasks = db.query(TaskModel).all()
    return tasks 

@app.post("/tasks")
def create_task(task: CreateTask, db: Session = Depends(get_db)):
    new_task = TaskModel(title=task.title, done=task.done)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task 

@app.get("/tasks/{id}", response_model=TaskOut)
def get_specific_task(id: int, db: Session = Depends(get_db)):
    result_task = db.query(TaskModel).filter(TaskModel.id == id).first() 
    if result_task is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return result_task

@app.put("/tasks/{id}", response_model=TaskOut)
def edit_task(id: int, task: UpdateTask, db: Session = Depends(get_db)):
    searched_task = db.query(TaskModel).filter(TaskModel.id == id).first()
    if searched_task is None:
        raise HTTPException(status_code=404, detail="Item not found")

    searched_task.title = task.title
    searched_task.done = task.done

    db.commit()
    db.refresh()
    return searched_task
    

@app.delete("/tasks/{id}")
def delete_task(id: int, db: Session = Depends(get_db)):
    searched_task = db.query(TaskModel).filter(TaskModel.id == id).first()
    if searched_task is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(searched_task)
    db.commit()
    return {"message": "Deleted Task"}
