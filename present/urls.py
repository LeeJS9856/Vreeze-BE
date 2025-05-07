from django.urls import path
from . import views

urlpatterns = [
    path("", views.PresentAPIView.as_view()),
    path("<int:present_id>/", views.PresentDetailAPIView.as_view()),
    path("user/<int:user_pk>/", views.UserPresentAPIView.as_view()),

    path("card/", views.CardAPIView.as_view()),
    path("card/<int:card_pk>/", views.CardDetailAPIView.as_view()),
]