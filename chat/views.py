from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from .models import UserQuestion
from .serializers import UserQuestionSerializer
from .ai import ai_chat

class ChatAPIView(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            raise AuthenticationFailed("로그인이 필요합니다.")
        question = request.data.get('question')
        
        if not request.session.session_key:
            request.session.create()
        session_id = request.session.session_key

        if not question:
            return Response({"error": "질문을 입력해주세요."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            answer = ai_chat(question,session_id)
            question_instance = UserQuestion.objects.create(
                question=question,
                answer=answer,
                session_id=session_id
            )
            return Response(
                UserQuestionSerializer(question_instance).data,
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)