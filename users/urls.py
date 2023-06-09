from django.urls import path
from . import views

urlpatterns = [
    path("", views.Signup.as_view()),
    path("<int:pk>/", views.UserDetail.as_view()),
    path("mypage/", views.Mypage.as_view()),
    path("login/", views.Login.as_view()),
    path("logout/", views.Logout.as_view()),
]
