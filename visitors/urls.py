from django.urls import path
from . import views

urlpatterns = [
    path("",views.VisitorView.as_view()),
]