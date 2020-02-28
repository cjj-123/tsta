from django.urls import path
from update_tags import views


urlpatterns = [
    path('sharing_url/', views.get_sharing_url),
    path('add_tags/', views.add_tags_one),
]