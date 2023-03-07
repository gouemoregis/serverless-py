import os
from src.env import config

from fastapi import FastAPI

# MODE=os.getenv("MODE", "dev")
# MODE=os.environ.get("MODE") or "abc"
MODE = config("MODE", default="test")

app = FastAPI()


@app.get("/") # GET -> HTTP METHOD
def home_page():
    # for API services
    # JSON-ready dict -> json.dumps({'Hello': 'World'})
    return {"Hello": "World", "mode": MODE}


# @app.post("/") # POST -> HTTP METHOD
# def home_handle_data_page():
#     # for API services
#     # JSON-ready dict -> json.dumps({'Hello': 'World'})
#     return {"Hello": "World"}


