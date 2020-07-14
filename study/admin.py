from django.contrib import admin

from .models import *


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'is_published')
    list_display_links = ('id', 'name')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'is_published')
    list_display_links = ('id', 'name')


admin.site.register(Review, ReviewAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Question, QuestionAdmin)
