from app.analysis.ai.base import AIProvider

class FakeAIProvider(AIProvider):
    def generate_text(self, prompt: str) -> str:
        return (
            "Это fake-ответ от AI provider.\n\n"
            "В будущем здесь будет ответ от реальной модели.\n\n"
            "Prompt, который был бы отправлен модели:\n\n"
            f"{prompt}"
        )