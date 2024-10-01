from django.urls import path
from . import views
from .views import story_list_view

urlpatterns = [
    path('', views.index, name='index'),  # Trang chính
    path('stories/', story_list_view, name='story_list'),  # Danh sách câu chuyện
]
