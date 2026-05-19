from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

with open("tasks.json", "r", encoding="utf-8") as f:
    tasks = json.load(f)

@app.get("/tasks")
def task_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html", 
        context={"tasks": tasks}
    )

@app.post("/add")
def add_task(request: Request, task: str = Form(), priority: str = Form()):
    tasks.append(
        {
            "title": task,
            "priority": priority
        }
    )

    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

    return RedirectResponse(
        url="/tasks",
        status_code=303
    )

@app.post("/delete")
def delete_task(request: Request, task: str = Form(), priority: str = Form()):
    tasks.remove(
        {
            "title": task,
            "priority": priority
        }
    )

    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)
    
    return RedirectResponse(
        url="/tasks",
        status_code=303
    )
        
