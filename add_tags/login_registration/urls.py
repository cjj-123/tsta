from django.urls import path
from login_registration import views


urlpatterns = [
    path('login/', views.login_logic),
    path('register/', views.register_logic),
    path('about/', views.about_clause)
]