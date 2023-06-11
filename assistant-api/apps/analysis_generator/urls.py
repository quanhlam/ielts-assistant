from django.urls import path
from . import views

urlpatterns = [
    path('swot', views.SwotView.as_view()),
    path('canvas', views.BusinessCanvas.as_view()),
    path('mck7s', views.Mck7s.as_view()),
    path('balanced-scorecard', views.BalancedScorecard.as_view()),
]
