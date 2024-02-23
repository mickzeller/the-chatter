from contextlib import asynccontextmanager
from router import message
import uvicorn
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(_app: FastAPI):
    print("Initializing resources...")
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def index():
    return {"message": "Hello, World!"}


app.include_router(message.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9090)
