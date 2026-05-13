from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

tasks = [
            "Python勉強",
            "ガンプラ",
            "買い物"
        ]

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

    return templates.TemplateResponse(
        request = request,
        name="index.html",
        context={"tasks": tasks}
    )
        
