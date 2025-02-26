# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .serializers import UserSerializer
from .models import User
# Create your views here.l

class UserAPIView(APIView) :
    # 모든 유저 조회
    def get(self, request):
        if request.user.is_superuser == False:
            raise PermissionDenied("권한이 없습니다.")
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    # 회원가입
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class UserDetailAPIView(APIView) :
    #본인 확인 메서드
    def get_object(self, user_pk, request):
        user = get_object_or_404(User, id=user_pk)
        if request.user.id != user_pk:
            raise PermissionDenied("권한이 없습니다.")
        return user
    
    # 프로필 조회
    def get(self, request, user_pk):
        user = self.get_object(user_pk, request)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    # 계정 정보 수정
    def put(self, request, user_pk):
        user = self.get_object(user_pk, request)
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    # 계정 삭제
    def delete(self, request, user_pk):
        user = self.get_object(user_pk, request)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    