# This file is the starting point of whole application
#============================================================================================
# Importing the Libraires
from fastapi import FastAPI
from core.config import settings
from fastapi import staticfiles
from apis.general_pages.route_homepage import general_pages_router


def start_app():
    # Making the app
    app = FastAPI(title=settings.PROJECTNAME,version=settings.PROJECTVERSION)
    include_router(app)
    return app

def include_router(app):
    app.include_router(general_pages_router)

def config_static(app):
    app.mount("/static",staticfiles(directory = "static"), name = "static")

    
app = start_app()

# Home route
@app.get("/")
def home():
    return {"Message":"Helloworld"}

# 