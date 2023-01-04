import numpy as np
import pickle

Model = pickle.load(open("MachineModels\Laptop Prize prediction\LaptopPriceModel.pkl","rb"))
Model2 = pickle.load(open("MachineModels\Calories Burnt Prediction\CalBurnModel.pkl","rb"))
Model3 = pickle.load(open("MachineModels\Diabetes prediction\DiabeteseModel.pkl","rb"))


def laptoppricecal(Company: str, TypeName: str, Ram:int, Weight: float,TouchScreen: int,IPS: int,ScreenSize: int,Resolution: str,Cpu_brand: str,HDD: int,SSD: int,Gpu_brand: str,os: str):
    X_res = int(Resolution.split('x')[0])
    Y_res = int(Resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/ScreenSize
    query = np.array([Company,TypeName,Ram,Weight,TouchScreen,IPS,ppi,Cpu_brand,HDD,SSD,Gpu_brand,os])
    query = query.reshape(1,12)
    result = str(int(np.exp(Model.predict(query)[0])))
    return result

def caloriesburncal(gender: int, age: int,height: float, Weight: float, duration: float, heartrate: float, bodytemp: float):
# Gender	Age	Height	Weight	Duration	Heart_Rate	Body_Temp
    query = np.array([gender,age,height,Weight,duration,heartrate,bodytemp])
    query = query.reshape(1,7)
    result = str(round(Model2.predict(query)[0], 3))
    return result

def diabetesecal(Pregnancies:int, Glucose:int, BloodPressure:int, SkinThickness:int, Insulin:int, BMI:float, DPFunction:float,	Age:int):
#  Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age	Outcome
    query = np.array([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DPFunction,Age])
    query = query.reshape(1,8)
    if Model3.predict(query)[0]==0:
        result = "Non - Diabetic" 
    else:
        result = "Diabetic"
    return result
