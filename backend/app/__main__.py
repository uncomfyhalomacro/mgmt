import uvicorn
from app.core.config import settings

if __name__ == "__main__":
    uvicorn.run(app='app:app', host=settings.host, port=settings.port, reload=True)
