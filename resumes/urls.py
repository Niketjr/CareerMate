from django.urls import path
from .views import ResumeUploadView, ResumeDetailView, ResumeUpdateView, ResumeDeleteView

urlpatterns = [
    path('upload/', ResumeUploadView.as_view(), name='resume-upload'),
    path('<int:pk>/', ResumeDetailView.as_view(), name='resume-detail'),
    path('<int:pk>/update/', ResumeUpdateView.as_view(), name='resume-update'),
    path('<int:pk>/delete/', ResumeDeleteView.as_view(), name='resume-delete'),
]
