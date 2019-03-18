from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect

from rest_framework import viewsets
from .serializers import BookmarkSerializer, TagSerializer

from .forms import BookmarkForm
from .models import Bookmark, Tag


def bookmark_list(request):
    bookmarks = Bookmark.public.all()
    context = {'bookmarks': bookmarks}
    return render(request, 'web/bookmark_list.html', context)


def bookmark_user(request, username):
    user = get_object_or_404(User, username=username)
    
    if request.user == user:
        bookmarks = user.bookmarks.all()
    else:
        bookmarks = Bookmark.public.filter(owner__username=username)
    
    context = {'bookmarks': bookmarks, 'owner': user}
    return render(request, 'web/bookmark_user.html', context)


@login_required
def bookmark_create(request):
    if request.method == 'POST':
        form = BookmarkForm(data=request.POST)
        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.owner = request.user
            bookmark.save()
            form.save_m2m()
            return redirect('web-bookmark-user', 
                username=request.user.username)
    else:
        form = BookmarkForm()
    
    context = {'form': form, 'create': True}
    return render(request, 'web/form.html', context)


@login_required
def bookmark_edit(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    if bookmark.owner != request.user and not request.user.is_superuser:
        raise PermissionDenied
    
    if request.method == 'POST':
        form = BookmarkForm(instance=bookmark, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('web-bookmark-user', username=request.user.username)
    else:
        form = BookmarkForm(instance=bookmark)
    
    context = {'form': form, 'created': False}
    return render(request, 'web/form.html', context)

class BookmarkView(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()


class TagView(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
