from django.urls import path
from . import views

urlpatterns = [
    path('writing', views.WritingView.as_view()),
]
