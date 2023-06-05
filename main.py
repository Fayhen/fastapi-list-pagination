from fastapi import FastAPI
from fastapi.responses import Response
from core.assets import get_list


app = FastAPI()


@app.get("/")
def home():
    return Response(status_code=200)


@app.get("/range")
def get_range(limit: int = 10, page: int = 1):
    my_range = get_list(limit, page)
    print(limit, page)
    return my_range
