# service_a.py
from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/")
async def read_root():
    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            r = await client.get("http://b-service:8080/")
        return {"message": f"Hello from Service A! B says: {r.text}"}
    except:
        return {"message": "Hello from Service A! B unreachable"}
