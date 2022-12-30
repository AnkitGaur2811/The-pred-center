from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from apis.general_pages.forms_data import LaptopPriceform,laptoppricecal
# from fastapi.routing import url_for

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
    return templates.TemplateResponse("gernal_pages/laptoppricepred.html",{"request":request,"Result":0})

@general_pages_router.post("/laptoppricepredsubmit")
async def laptoppricepredsubmit(request:Request):
    data =  request
    # Company = data.Company
    # TypeName = data.TypeName
    # Ram = data.Ram
    # Weight= data.Weight
    # touchScreen: data.TouchScreen
    # ips = data.IPS
    # ScreenSize = data.ScreenSize
    # Resolution = data.Resolution
    # Cpubrand = data.Cpu_brand
    # hdd = data.HDD
    # ssd = data.SSD
    # Gpubrand =data.Gpu_brand
    # os = data.os
    # price = laptoppricecal(Company,TypeName,Ram,Weight,touchScreen,ips,ScreenSize,Resolution,Cpubrand,hdd,ssd,Gpubrand,os)
    return {"message": request.keys()}