import httpx
from urllib.parse import urlencode

from app.activity_provider.base import ActivityProvider
from app.core.config import settings


class StravaProvider(ActivityProvider):
    authorization_url = "https://www.strava.com/oauth/authorize"
    token_url = "https://www.strava.com/oauth/token"

    @property
    def name(self) -> str:
        return "strava"

    def build_authorization_url(self) -> str:
        query_parameters = {
            "client_id": settings.strava_client_id,
            "redirect_uri": settings.strava_redirect_uri,
            "response_type": "code",
            "approval_prompt": "auto",
            "scope": "activity:read_all",
        }

        return f"{self.authorization_url}?{urlencode(query_parameters)}"

    def exchange_authorization_code(self, code: str) -> dict:
        response = httpx.post(
            url=self.token_url,
            data={
                "client_id": settings.strava_client_id,
                "client_secret": settings.strava_client_secret,
                "code": code,
                "grant_type": "authorization_code",
            }
        )

        response.raise_for_status()
        return response.json()
