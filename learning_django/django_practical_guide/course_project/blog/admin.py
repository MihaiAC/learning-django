from django.contrib import admin
from .models import Post, Tag, Author, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("post_title",)}
    list_display = ("post_title", "date", "author")
    list_filter = ("author", "date", "tag")

class TagAdmin(admin.ModelAdmin):
    list_display = ("caption", )

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment)
