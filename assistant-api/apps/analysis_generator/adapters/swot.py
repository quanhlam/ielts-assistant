import re
from .base import BaseAdapter

class SwotAdapter(BaseAdapter):

    def __init__(self):
        super().__init__('SWOT')

    SEGMENTS = ["STRENGTHS", "WEAKNESSES", "OPPORTUNITIES", "THREATS"]