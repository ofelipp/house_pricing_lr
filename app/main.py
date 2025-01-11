from fastapi import FastAPI

api = FastAPI()


@api.get(path="/")
def root():
    return {"message": "Hello World"}
