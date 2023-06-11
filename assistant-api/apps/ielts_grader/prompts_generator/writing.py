from .base import BaseAdapter

class IeltsWritingGrader(BaseAdapter):
    def __init__(self):
        super().__init__('writing')

    SEGMENTS = ["Task Response", "Coherence and Cohesion", "Lexical Resource", "Grammatical Range and Accuracy", "Overall Score"]

    def add_segment(self):
        pass

    def load_segment(self):
        pass

    def delete_segment(self):
        pass