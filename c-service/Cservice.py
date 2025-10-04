# service_c.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/")
async def read_root():
    return {"message": "Hello from Service C!"}
