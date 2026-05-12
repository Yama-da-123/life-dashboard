from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/tasks")
def task_page(request: Request):
    tasks = [
        "Python勉強",
        "ガンプラ",
        "買い物"
    ]

    return templates.TemplateResponse(
        request=request,
        name="index.html", 
        context={"tasks": tasks}
    )