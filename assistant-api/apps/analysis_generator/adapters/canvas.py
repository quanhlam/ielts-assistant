import re
from .base import BaseAdapter

class CanvasAdapter(BaseAdapter):
    def __init__(self):
        super().__init__('Business Canvas')

    SEGMENTS = ["CUSTOMER_SEGMENTS", "VALUE_PROPOSITIONS", "CHANNELS", "CUSTOMER_RELATIONSHIPS", "REVENUE_STREAMS", "KEY_RESOURCES",
                "KEY_ACTIVITIES", "KEY_PARTNERSHIPS", "COST_STRUCTURE" ]