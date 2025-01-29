from fastapi import FastAPI

from url_shortener.routers.shortner import router as shortner_router

app = FastAPI()


# ctrl + : => a :: run all test
# f5 run server from config in launch.json
@app.get("/test")
def test():
    return {"msg": "it's work"}


@app.get("/")
def root():
    return {"msg": "it's work"}


app.include_router(shortner_router)
