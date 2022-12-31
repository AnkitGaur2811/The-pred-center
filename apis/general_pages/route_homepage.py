from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from apis.general_pages.forms_data import laptoppricecal
from pydantic import ValidationError

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
    return templates.TemplateResponse("gernal_pages/laptoppricepred.html",{"request":request,"Result":-1})

# @general_pages_router.post("/caloriesburnsubmit")
# async def caloriesburnsubmit(request:Request):
#     try:
#         data = await request.form()

#         return templates.TemplateResponse("gernal_pages/laptoppricepred.html",{"request":request,"Result":price})
#     except ValidationError as e:
#         return {"message": "Invalid input"+e }

# @general_pages_router.post("/diabetesesubmit")
# async def caloriesburnsubmit(request:Request):
#     try:
#         data = await request.form()

#         return templates.TemplateResponse("gernal_pages/laptoppricepred.html",{"request":request,"Result":price})
#     except ValidationError as e:
#         return {"message": "Invalid input"+e }


@general_pages_router.post("/laptoppricepredsubmit")
async def laptoppricepredsubmit(request:Request):
    try:
        data = await request.form()
        Company = data["Brand"]
        TypeName = data["Type"]
        Ram = int(data["RAM"])
        Weight= float(data["Weight"])
        touchScreen= int(data["TouchScreen"])
        ips = int(data["IPS"])
        ScreenSize = float(data["ScreenSize"])
        Resolution = data["Resolution"]
        Cpubrand = data["CPU"]
        hdd = int(data["HDD"])
        ssd = int(data["SSD"])
        Gpubrand = data["GPU"]
        os = data["OS"]
        price = laptoppricecal(Company,TypeName,Ram,Weight,touchScreen,ips,ScreenSize,Resolution,Cpubrand,hdd,ssd,Gpubrand,os)
        return templates.TemplateResponse("gernal_pages/laptoppricepred.html",{"request":request,"Result":price})
    except ValidationError as e:
        return {"message": "Invalid input"+e }