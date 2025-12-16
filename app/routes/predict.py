from fastapi import APIRouter, UploadFile, File
from app.services.model import predict

router = APIRouter()

@router.post("/predict")
async def run_prediction(file: UploadFile= File(...)):
    result = predict(file)
    return result

