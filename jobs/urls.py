from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list_view, name='job_list'),
    path('create/', views.job_create, name='job_create'),
    path('job/<int:job_id>/candidates/', views.job_candidates, name='job_candidates'),
    
]