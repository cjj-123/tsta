from django.urls import path
from control_models import views


urlpatterns = [
    path('choice/', views.choice_object)
]