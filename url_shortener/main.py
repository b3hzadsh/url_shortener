from fastapi import FastAPI
from models.url_model import Link, LinkIn
from routers.shortner import router as shortner_router

app = FastAPI()


# ctrl + : => a :: run all test
@app.get("/test")
def test():
    return {"msg": "it's work"}


app.include_router(shortner_router)
