from django.contrib import admin

from  .models import Bookmark, Tag


class BookmarkAdmin(admin.ModelAdmin):
	list_display = ('title', 'owner')


class TagAdmin(admin.ModelAdmin):
	list_display = ('name',)

admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Tag, TagAdmin)
