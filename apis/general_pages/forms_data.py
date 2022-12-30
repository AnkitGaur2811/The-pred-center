from pydantic import BaseModel
import numpy as np

class LaptopPriceform(BaseModel):
    Company: str
    TypeName: str
    Ram:int 
    Weight: float
    TouchScreen: int
    IPS: int
    ScreenSize: int
    Resolution: str
    Cpu_brand: str
    HDD: int
    SSD: int
    Gpu_brand: str
    os: str

class diabeteseform(BaseModel):
    pass
class calburnform(BaseModel):
    pass

def laptoppricecal(Company: str, TypeName: str, Ram:int, Weight: float,TouchScreen: int,IPS: int,ScreenSize: int,Resolution: str,Cpu_brand: str,HDD: int,SSD: int,Gpu_brand: str,os: str):
    X_res = int(Resolution.split('x')[0])
    Y_res = int(Resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/ScreenSize
    query = np.array([Company,TypeName,Ram,Weight,TouchScreen,IPS,ppi,Cpu_brand,HDD,SSD,Gpu_brand,os])
    result = 10
    return result