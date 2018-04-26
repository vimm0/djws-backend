from django.db import models
from django.contrib import admin

from martor.widgets import AdminMartorWidget

from .models import Post


class PostModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

    list_display = ["title", "updated", "timestamp"]
    list_display_links = ["updated"]
    list_editable = ["title"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
