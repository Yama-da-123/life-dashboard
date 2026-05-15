from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import json

app = FastAPI()

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
def add_task(request: Request, task: str = Form()):
    tasks.append(task)

    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

    return templates.TemplateResponse(
        request = request,
        name="index.html",
        context={"tasks": tasks}
    )
        
