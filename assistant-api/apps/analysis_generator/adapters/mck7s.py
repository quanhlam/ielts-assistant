import re
from .base import BaseAdapter

class Mck7sAdapter(BaseAdapter):
    def __init__(self):
        super().__init__('McKinsey 7s')

    SEGMENTS = ["STRATEGY", "STRUCTURE", "SYSTEMS", "SHARED_VALUES", "SKILLS", "STAFF", "STYLE" ]