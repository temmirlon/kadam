from fastapi import FastAPI

from app.api.routes import router as api_routes
from app.activities.routes import router as activities_router
from app.core.config import settings

app = FastAPI(title=settings.app_name)

app.include_router(api_routes)
app.include_router(activities_router)