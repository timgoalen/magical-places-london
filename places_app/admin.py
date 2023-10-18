from django.contrib import admin
from .models import Place, Comment, Favourite


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("place_name", "created_on", "contributer")
    search_fields = ("place_name", "created_on", "contributer")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("place", "comment", "author", "created_on")
    search_fields = ("place", "comment", "author", "created_on")


@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ("place", "user", "favourited_on")
    search_fields = ("place", "user", "favourited_on")
