from app.analysis.ai.base import AIProvider
from app.analysis.ai.fake import FakeAIProvider

def get_ai_provider(provider_name: str) -> AIProvider:
    if provider_name == "fake":
        return FakeAIProvider()
    
    raise ValueError(f"Unsupported AI Provider: {provider_name}")