from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from .services import IeltsGraderService


# Create your views here.
class WritingView(APIView):
    def post(self, request, format=None):
        data = request.data
        try:

            question = data['question']
            answer = data['answer']
        except:
            return Response({
                "message": "missing fields"
            }, status=status.HTTP_400_BAD_REQUEST)
        service = IeltsGraderService('writing')
        responses = service.generate_review(question=question, answer=answer)
        return Response({
            "data": responses,
        })