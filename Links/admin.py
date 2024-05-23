from django.contrib import admin
from . models import Links
from . models import Category
from .models import UserProfile

# Register your models here.

class LinksAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)
admin.site.register(Links, LinksAdmin)

class CategoryAdmin(admin.ModelAdmin):
    filter_horizontal = ('user',)
admin.site.register(Category, CategoryAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'package')

admin.site.register(UserProfile, UserProfileAdmin)