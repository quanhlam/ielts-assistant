from apps.analysis_generator.adapters.swot import SwotAdapter
from apps.analysis_generator.adapters.mck7s import Mck7sAdapter
from apps.analysis_generator.adapters.canvas import CanvasAdapter
from apps.analysis_generator.adapters.balanced_scorecard import BalancedScorecardAdapter

class ApiAdapterFactory:
    def __init__(self, business_model):
        self.business_model = business_model
    def create_adapter(self):
        if self.business_model == "swot":
            return SwotAdapter()
        elif self.business_model == 'canvas':
            return CanvasAdapter()
        elif self.business_model == 'mck7s':
            return Mck7sAdapter()
        elif self.business_model == 'balanced_scorecard':
            return BalancedScorecardAdapter()
