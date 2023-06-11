from rest_framework.views import APIView
from rest_framework.response import Response

from .services import AnalysisGeneratorService

# Create your views here.
class SwotView(APIView):
    def post(self, request, format=None):
        data = request.data
        statement = data['statement']
        service = AnalysisGeneratorService('swot', statement)
        responses = service.generate_answer()
        return Response({
            "data": responses,
        })


class Mck7s(APIView):
    def post(self, request, format=None):
        data = request.data
        statement = data['statement']
        service = AnalysisGeneratorService('mck7s', statement)
        responses = service.generate_answer()
        return Response({
            "data": responses,
        })

class BusinessCanvas(APIView):
    def post(self, request, format=None):
        data = request.data
        statement = data['statement']
        service = AnalysisGeneratorService('canvas', statement)
        responses = service.generate_answer()
        return Response({
            "data": responses,
        })

class BalancedScorecard(APIView):
    def post(self, request, format=None):
        data = request.data
        statement = data['statement']
        service = AnalysisGeneratorService('balanced_scorecard', statement)
        responses = service.generate_answer()
        return Response({
            "data": responses,
        })