from app.analysis.ai.base import AIProvider
from app.analysis.ai.fake import FakeAIProvider
from app.analysis.ai.exceptions import UnsupportedAIProviderError

def get_ai_provider(provider_name: str) -> AIProvider:
    if provider_name == "fake":
        return FakeAIProvider()
    
    raise UnsupportedAIProviderError(provider_name)