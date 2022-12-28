from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
general_pages_router = APIRouter()

@general_pages_router.get("/")
async def home(request:Request):
    return templates.TemplateResponse("gernal_pages/homepage.html",{"request":request})

@general_pages_router.get("/caloriesburnt")
async def caloriesburnt(request:Request):
    return templates.TemplateResponse("gernal_pages/caloriesburntpred.html",{"request":request})

@general_pages_router.get("/diabetese")
async def diabetese(request:Request):
    return templates.TemplateResponse("gernal_pages/diabetesepred.html",{"request":request})

@general_pages_router.get("/laptopprice")
async def laptopprice(request:Request):
    return templates.TemplateResponse("gernal_pages/laptoppricepred.html",{"request":request})