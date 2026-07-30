class UnsupportedAIProviderError(Exception):
    def __init__(self, provider_name: str):
        self.provider_name = provider_name