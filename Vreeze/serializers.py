from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from user.models import User
from django.contrib.auth.hashers import check_password


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        username = attrs['username']
        password = attrs['password']
        try:
            user = User.objects.get(username=username)
        except:
            raise ValidationError({"detail": "아이디가 틀렸습니다"})

        if not check_password(password, user.password):
            raise ValidationError({"detail": "비밀번호가 틀렸습니다."})

        return super().validate(attrs)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token
