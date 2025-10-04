# service_b.py
from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/")
async def read_root():
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get("http://c-service:8080/")
        return {"message": f"Hello from Service B! C says: {r.text}"}
    except:
        return {"message": "Hello from Service B! C unreachable"}
