import re
from .base import BaseAdapter

class BalancedScorecardAdapter(BaseAdapter):
    def __init__(self):
        super().__init__('Balanced Scorecard')

    SEGMENTS = ["FINANCIAL_PERSPECTIVE", "CUSTOMER_PERSPECTIVE", "INTERNAL_BUSINESS_PROCESS_PERSPECTIVE", "LEARNING_AND_GROWTH_PERSPECTIVE"]