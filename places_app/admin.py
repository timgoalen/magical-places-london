from django.contrib import admin
from .models import Place, Comment


class CommentInline(admin.StackedInline):
    # could change to '(admin.TabularInline)' if needed to display more
    model = Comment
    extra = 0


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Place, PlaceAdmin)
admin.site.register(Comment)
