# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied, AuthenticationFailed
from .serializers import RecordSerializer, AvatarSerializer
from .models import Record, Avatar
# Create your views here.l

class RecordAPIView(APIView) :
    # 모든 녹음 조회
    def get(self, request):
        if request.user.is_superuser == False:
            raise PermissionDenied("권한이 없습니다.")
        record = Record.objects.all()
        serializer = RecordSerializer(record, many=True)
        return Response(serializer.data)
    
    # 녹음
    def post(self, request):
        serializer = RecordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class RecordDetailAPIView(APIView) :
    #로그인 여부 확인
    def get_object(self, record_pk, request):
        if not request.user.is_authenticated:
            raise AuthenticationFailed("로그인이 필요합니다.")
        record = get_object_or_404(Record, id=record_pk)
        return record
    
    # 레코드 조회
    def get(self, request, record_pk):
        record = self.get_object(record_pk, request)
        serializer = RecordSerializer(record)
        return Response(serializer.data)

    # 레코드 삭제
    def delete(self, request, record_pk):
        record = self.get_object(record_pk, request)
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class AvatarAPIView(APIView) :
    # 모든 아바타 조회
    def get(self, request):
        if request.user.is_superuser == False:
            raise PermissionDenied("권한이 없습니다.")
        avatar = Avatar.objects.all()
        serializer = AvatarSerializer(avatar, many=True)
        return Response(serializer.data)
    
    # 아바타 등록
    def post(self, request):
        serializer = AvatarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class AvatarDetailAPIView(APIView) :
    # 로그인 여부 조회
    def get_object(self, avatar_pk, request):
        if not request.user.is_authenticated:
            raise AuthenticationFailed("로그인이 필요합니다.")
        avatar = get_object_or_404(Avatar, id=avatar_pk)
        return avatar
    
    # 아바타 조회
    def get(self, request, avatar_pk):
        avatar = self.get_object(avatar_pk, request)
        serializer = AvatarSerializer(avatar)
        return Response(serializer.data)

    # 아바타 삭제
    def delete(self, request, avatar_pk):
        avatar = self.get_object(avatar_pk, request)
        avatar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    