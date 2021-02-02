
from django.urls import path, include

from .views import UserListView, UserDetailtView

urlpatterns = [
    path('user/', UserListView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserDetailtView.as_view(), name='user_detail'),
]
