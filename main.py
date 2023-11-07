from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sample import generate_script

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "script": None})

@app.post("/generate-script", response_class=HTMLResponse)
async def generate_script_endpoint(request: Request):
    script = generate_script()
    script = script[0]



    # Replace \n characters with <br> elements
    script = script.replace('\n', '<br>')

    
    print(script)  # Check the string extracted from the list


    return templates.TemplateResponse("index.html", {"request": request, "script": script})
