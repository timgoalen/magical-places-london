from django.contrib import admin
from .models import Place, Comment, Favourite


class CommentInline(admin.StackedInline):
    # could change to '(admin.TabularInline)' if needed to display more
    model = Comment
    extra = 0


# class CommentAdmin(admin.StackedInline):
#     model = Comment
#     extra = 0


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        # CommentAdmin,
        CommentInline,
    ]
    list_display = ("place_name", "created_on", "contributer")
    search_fields = ("place_name", "created_on", "contributer")


class FavouriteAdmin(admin.ModelAdmin):
    list_display = ("place", "user", "favourited_on")
    search_fields = ("place", "user", "favourited_on")


admin.site.register(Place, PlaceAdmin)
admin.site.register(
    Comment,
)
admin.site.register(Favourite, FavouriteAdmin)
