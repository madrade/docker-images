from datetime import datetime
import json

import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_303_SEE_OTHER
from pydantic import BaseModel

DATA = 'data/data.json'

class Payload(BaseModel):
    temperature: float
    created: datetime = datetime.now().isoformat()


app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def view_dashboard(request: Request):
    data = json.load(open(DATA))

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "title": "My Magic Dashboard!",
            "temperature": data['temperature'],
            "timestamp": data['created']
        }
    )

# install package "python-multipart"
@app.get("/form", response_class=HTMLResponse)
def view_form(request: Request):
    return templates.TemplateResponse(
        "form.html",
        { "request": request }
    )

@app.post("/form")
def process_form(request: Request, temperature: float = Form(...)):
    now = datetime.now()
    data = {
        'temperature': temperature,
        'created': now.strftime("%d.%m.%Y %H:%M:%S")
    }

    with open(DATA, 'w+') as file:
        json.dump(data, file)

    return RedirectResponse(url='/', status_code=HTTP_303_SEE_OTHER)


@app.get('/api/temp')
def get_latest_value():
    """
    Returns last measurement
    """
    file = open(DATA)
    data = json.load(file)
    return data


@app.post('/api/temp', status_code=201)
def add_new_value(data: Payload):
    with open(DATA) as file:
        json.dump(data.dict(), file)
    return data


if __name__ == "__main__":
    uvicorn.run('dashboard:app',
                host="0.0.0.0",
                port=5000,  # default port is 8000
                reload=True)
