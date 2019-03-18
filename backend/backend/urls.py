"""bookmark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include, reverse_lazy

from rest_framework import routers

from bookmark import views

router = routers.DefaultRouter()
router.register(r'bookmarks', views.BookmarkView, 'bookmark')
router.register(r'tags', views.TagView, 'tag')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookmark.urls')),
    path('login/', auth_views.LoginView.as_view(), {'template_name': 'login.html'},
        name='web-bookmark-login'),
    path('logout/', auth_views.LogoutView.as_view(),
        {'next_page': reverse_lazy('web-bookmark-list')}, name='web-bookmark-logout'),
    
    # DJANGO REST FRAMEWORK
    path('api/', include(router.urls))
]
