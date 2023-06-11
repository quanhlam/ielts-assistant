import os
import logging
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")



class OpenAiService:

    def generate_answer_chat_gpt(self, prompt):
        model = os.getenv("DEFAULT_MODEL")
        response = openai.ChatCompletion.create(model=model, messages=prompt)
        logging.info(f"Open AI Response: {response}")
        answer_content = response["choices"][0]["message"]["content"]
        return answer_content