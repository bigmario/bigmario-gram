from django.urls import path
from posts import views

urlpatterns = [
    path("", views.list_posts, name="feed"),
]
