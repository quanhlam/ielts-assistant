
from .prompts_generator.factory import PromptGeneratorFactory
from ..open_ai.services import OpenAiService



class IeltsGraderService:
    def __init__(self, skill):
        self.skill = skill

    def generate_review(self, *args, **kwargs):
        openai_service = OpenAiService()
        factory = PromptGeneratorFactory("ielts_writing_grader")
        prompt_generator = factory.create_generator()
        prompt = prompt_generator.get_prompt("2", kwargs["question"], kwargs["answer"])
        response = openai_service.generate_answer_chat_gpt(prompt)
        response_formatted = prompt_generator.parse(response)

        return response_formatted
