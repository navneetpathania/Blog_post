from django.urls import path
from . import views

from .views import PostListView, PostDetaileView, CreatePostView, PostUpdateView, PostDeleteView,UserPostListView
urlpatterns = [
    # path('', views.home, name='home'),
    path('',PostListView.as_view(), name='home'),
    path('user/<str:username>',UserPostListView.as_view(), name='user-post'),
    path('post/<int:pk>',PostDetaileView.as_view(), name='post-detaile'),
    path('post/<int:pk>/update',PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(), name='post-delete'),
    path('post/new',CreatePostView.as_view(), name='new-post'),
    path('about/',views.about,name='about')
]