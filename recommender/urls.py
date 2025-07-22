# recommender/urls.py
from django.urls import path
from .views import RecommendView

urlpatterns = [
    path('<int:id>/', RecommendView.as_view(), name='recommend'),
]
