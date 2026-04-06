from fastapi import FastAPI
app = FastAPI(root_path="/api")


@app.get("/healthz")
async def check_endpoint():
    return {"message": "Hello, World"}

