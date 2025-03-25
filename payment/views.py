# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied, AuthenticationFailed
from .serializers import PaymentSerializer
from .models import Payment
# Create your views here.l

class PaymentAPIView(APIView) :
    # 결재
    def post(self, request):
        if not request.user.is_authenticated:
            raise AuthenticationFailed("로그인이 필요합니다.")
        serializer = PaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
class PaymentDetailAPIView(APIView) :
    # 해당 결재 내역 조회
    def get(self, request, payment_pk):
        payment = get_object_or_404(Payment, id=payment_pk)
        if payment.user != request.user:
            raise PermissionDenied("이 결제 내역을 조회할 권한이 없습니다.")
        serializer = PaymentSerializer(payment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserPaymentAPIView(APIView) :
    # 해당 유저 전체 결재 내역 조회
    def get(self, request, user_pk):
        if request.user.pk != user_pk:
            raise PermissionDenied("이 결제 내역을 조회할 권한이 없습니다.")
        payments = Payment.objects.filter(user_id=user_pk)
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    