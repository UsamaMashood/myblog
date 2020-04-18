from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('', BlogListView.as_view(), name = 'home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name = 'post_detail'),
    path('post/new/', PostCreateView.as_view(), name = 'post_new'),
    path('post/<int:pk>/edit', PostUpdateView.as_view(), name = 'post_update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name = 'post_delete')
]
