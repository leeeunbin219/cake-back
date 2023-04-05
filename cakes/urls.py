from django.urls import path
from . import views

urlpatterns = [
    path("", views.UserCreateCake.as_view()),
    path("<int:pk>/", views.CakeBaseDetailViews.as_view()),
    path("deco/", views.DecoCakeViews.as_view()),
    path("deco/<int:pk>/", views.DecoDetailView.as_view()),
]
