import numpy as np
import pickle

Model = pickle.load(open("MachineModels/Laptop Prize prediction/LaptopPriceModel.pkl","rb"))


def laptoppricecal(Company: str, TypeName: str, Ram:int, Weight: float,TouchScreen: int,IPS: int,ScreenSize: int,Resolution: str,Cpu_brand: str,HDD: int,SSD: int,Gpu_brand: str,os: str):
    X_res = int(Resolution.split('x')[0])
    Y_res = int(Resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/ScreenSize
    query = np.array([Company,TypeName,Ram,Weight,TouchScreen,IPS,ppi,Cpu_brand,HDD,SSD,Gpu_brand,os])
    query = query.reshape(1,12)
    result = str(int(np.exp(Model.predict(query)[0])))
    return result

# def caloriesburncal():
#     pass
# def diabetesecal():
#     pass
