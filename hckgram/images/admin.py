from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):

    list_display_links =(
        'location',
    )    

    search_fields = (
        'location',
        'caption',
    )

    list_filter = (
        'location',
        'creator'
    )

    list_display = (
        'file',
        'location',
        'caption',
        'creator',
        'creat_at',
        'update_at',
    )

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    
    list_display = (
        'creator',
        'image',
        'creat_at',
        'update_at',
    )

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    
    list_display = (
        'message',
        'creator',
        'image',
        'creat_at',
        'update_at',
    )