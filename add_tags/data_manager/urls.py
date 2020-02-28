from django.urls import path
from data_manager import views

urlpatterns = [
    path('get_tags/', views.get_tags),
    path('update_tags/', views.update_tags),
    path('label_prompt/', views.label_prompt),
]