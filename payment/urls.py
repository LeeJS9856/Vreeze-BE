from django.urls import path
from . import views

urlpatterns = [
    path("", views.PaymentAPIView.as_view()),
    path("<int:payment_pk>/", views.PaymentDetailAPIView.as_view()),
    path("user/<int:user_pk>/", views.UserPaymentAPIView.as_view()),
]