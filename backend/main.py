from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from database import get_db, init_db, Task as TaskModel, Project as ProjectModel
from sqlalchemy.orm import Session

#initializes database
init_db()

app = FastAPI()

class CreateTask(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    done: bool = False
    project_id: int

class UpdateTask(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    done: bool = False

class TaskOut(BaseModel):
    id: int 
    title: str
    done: bool
    project_id: int

    class Config:
        from_attributes = True

class ProjectCreate(BaseModel):
    name: str = Field(min_length=1, max_length=200)

class ProjectOut(BaseModel):
    id: int
    name: str

    class Config:
            from_attributes = True


@app.get("/")
def root(): 
    return {"message": "Healthy!"}

@app.get("/tasks", response_model=list[TaskOut])
def get_all_tasks(db: Session = Depends(get_db)):
    tasks = db.query(TaskModel).all()
    return tasks 

@app.post("/tasks")
def create_task(task: CreateTask, db: Session = Depends(get_db)):
    new_task = TaskModel(title=task.title, done=task.done, project_id=task.project_id)
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
    db.refresh(searched_task)
    return searched_task
    

@app.delete("/tasks/{id}")
def delete_task(id: int, db: Session = Depends(get_db)):
    searched_task = db.query(TaskModel).filter(TaskModel.id == id).first()
    if searched_task is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(searched_task)
    db.commit()
    return {"message": "Deleted Task"}


# project endpoints
@app.get("/projects", response_model=list[ProjectOut])
def get_projects(db: Session = Depends(get_db)):
    all_projects = db.query(ProjectModel).all()
    return all_projects


@app.post("/projects", response_model=ProjectOut)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    new_project= ProjectModel(name=project.name)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

@app.get("/projects/{id}/tasks", response_model=list[TaskOut])
def get_specific_project_tasks(id: int, db: Session = Depends(get_db)):
    project = db.query(ProjectModel).filter(ProjectModel.id == id).first()
    if project is None:
        raise HTTPException(status_code=404, detail="Item not found")
    specific_project_tasks = db.query(TaskModel).filter(TaskModel.project_id == id).all()
    return specific_project_tasks

