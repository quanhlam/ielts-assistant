import os
import logging

from django.conf import settings
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT

from .openai_service import OpenAiService
from apps.analysis_generator.api_adapter_factory import ApiAdapterFactory

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

class AnalysisGeneratorService:
    def __init__(self, business_model, business_statement):
        self.business_model = business_model
        self.business_statement = business_statement

    def generate_answer(self):
        cache_key = self.business_model + "-" + self.business_statement.lower()
        cached_response = cache.get(cache_key)
        logging.info(f"Cache data: {cached_response}")
        if cached_response:
            return cached_response

        openai_service = OpenAiService()
        api_factory = ApiAdapterFactory(self.business_model)
        adapter = api_factory.create_adapter()
        prompt = adapter.get_prompt(self.business_statement)
        answer = openai_service.generate_answer_chat_gpt(prompt)

        response = adapter.parse(answer)

        cache.set(cache_key, response, timeout=CACHE_TTL)

        return response