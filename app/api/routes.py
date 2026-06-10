from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": f"{settings.app_name} API is running"}

@router.get("/health")
def health_check():
    return {"status": "ok"} 
