from django.contrib import admin

from blog.models import User, Tag, Category, Post, PostTag, PostCategory, PostComment


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'email',)
    search_fields = ('firstName', 'email',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('author', 'createdAt',)


admin.site.register(User, UserAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

