from django.urls import path
from . import views

urlpatterns = [
    path("", views.UserAPIView.as_view()),
    path("<int:user_pk>/", views.UserDetailAPIView.as_view()),
]