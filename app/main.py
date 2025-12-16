from fastapi import FastAPI

from app.routes.predict import router as predict_router

app = FastAPI(title="Example API")

@app.get("/")
def health_check():
    return{"status": "running"}

app.include_router(predict_router)
