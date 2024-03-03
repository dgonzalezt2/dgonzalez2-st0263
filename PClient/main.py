from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
templates = Jinja2Templates(directory="templates")

url = "http://pserver"


@app.get("/", response_class=HTMLResponse)
async def list_files(request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{url}/list_files/")
        files_data = response.json()

    return templates.TemplateResponse(
        "list_files.html", {"request": request, "files_data": files_data}
    )
