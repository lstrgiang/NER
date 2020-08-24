from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .ner import NER
from requests.exceptions import ConnectionError
app = FastAPI()

templates = Jinja2Templates(directory="app/static/templates")

@app.post("/", response_class=HTMLResponse)
async def root(request: Request, data: str = Form(...)):
    ner = NER(data)
    try:
        result = ner.result()
    except ConnectionError:
        if not result:
            return templates.TemplateResponse("error.html", {
                "request": request,
                "data": data, 
                "error": "Unable to connect to one of NLP servers",
            })
    print(result)

    # return {"result": ner.result()}
    return templates.TemplateResponse("result.html", {
        "request": request,
        "data": data, 
        "result": result,
    })


@app.get("/")
async def main():
    return FileResponse("app/static/index.html")

