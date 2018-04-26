from django.contrib import admin

# Register your models here.
from django.db import models
from .models import Post
# from markdownx.admin import MarkdownxModelAdmin
from martor.widgets import AdminMartorWidget


# class PostModelAdmin(admin.ModelAdmin, MarkdownxModelAdmin):
#     list_display = ["title", "updated", "timestamp"]
#     list_display_links = ["updated"]
#     list_editable = ["title"]
#     list_filter = ["updated", "timestamp"]
#     search_fields = ["title", "content"]
#
#     class Meta:
#         model = Post

class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }


admin.site.register(Post, YourModelAdmin)
