from django.urls import path
from . import views

urlpatterns = [
    path("record/", views.RecordAPIView.as_view()),
    path("record/<int:record_pk>/", views.RecordDetailAPIView.as_view()),
    path("avatar", views.AvatarAPIView.as_view()),
    path("avatar/<int:avatar_pk>", views.AvatarDetailAPIView.as_view()),
]