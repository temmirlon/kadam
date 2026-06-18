from pydantic import BaseModel

class ActivityAnalysis(BaseModel):
    activity_id: int
    summary: str
    positives: list[str]
    improvements: list[str]
    recommendation: str