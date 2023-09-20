from django.contrib import admin
from .models import Place, Comment


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
    list_display = ("place_name", "created_on", "number_of_times_favourited")
    search_fields = ("place_name",)


admin.site.register(Place, PlaceAdmin)
admin.site.register(Comment,)
