from django.contrib.auth import views as auth_views


from django.urls import path
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]


from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]



# Add Comment URLs
from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_new'),  # Adding new comment path
    path('post/<int:post_pk>/comment/new/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),  # Updating comment path
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]



# Add tagging and search URLs in urls.py:


from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('search/', views.post_search, name='post_search'),  # Search URL
    path('tags/<slug:tag>/', views.posts_by_tag, name='posts_by_tag'),  # Filter posts by tag
]





# ..............
from django.shortcuts import render
from .models import Post

def posts_by_tag(request, tag):
    posts = Post.objects.filter(tags__name=tag)
    return render(request, 'blog/posts_by_tag.html', {'tag': tag, 'posts': posts})

