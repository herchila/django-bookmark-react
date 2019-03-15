from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    path('user/<username>/', login_required(bookmark_user), name='web-bookmark-user'),
    path('create/', bookmark_create, name='web-bookmark-create'),
    path('edit/<pk>/', bookmark_edit, name='web-bookmark-edit'),
    path('', bookmark_list, name='web-bookmark-list'),
]
