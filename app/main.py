from fastapi import FastAPI

app = FastAPI(title="Example API")

@app.get("/")
def health_check():
    return{"status": "running"}
