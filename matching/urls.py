from django.urls import path
from . import views

urlpatterns = [
    path('upload/<int:job_id>/', views.upload_resume, name='upload_resume'),
]