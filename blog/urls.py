from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    # NB: no '/' before 'post/...' needed!:
    path('post/<int:pk>/', BlogDetailView.as_view(), name='view_post'),
    path('post/create/', BlogCreateView.as_view(), name='create_post'),
    path('post/edit/<int:pk>/', BlogUpdateView.as_view(), name='update_post'),
]
