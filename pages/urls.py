from django.urls import path
from .views import HomePageFeed, PostDetailView, PostCreateView
urlpatterns = [
    path('', HomePageFeed.as_view(), name='home'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/new/', PostCreateView.as_view(), name = 'post_new'),
]