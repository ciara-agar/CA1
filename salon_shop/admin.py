from django.contrib import admin
from .models import Category, Style 

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)

class StyleAdmin(admin.ModelAdmin):
    list_display = ['name','description', 'category',  'price', 'time_cost',]
    list_editable = ['price',]
    list_per_page = 20

admin.site.register(Style, StyleAdmin)