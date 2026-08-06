from fastapi import FastAPI

from app.api.routes import router as api_routes
from app.activities.routes import router as activities_router
from app.core.config import settings

from app.activity_provider.strava.routes import router as strava_router

app = FastAPI(title=settings.app_name)

app.include_router(api_routes)
app.include_router(activities_router)
app.include_router(strava_router)