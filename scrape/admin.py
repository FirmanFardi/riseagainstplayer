from django.contrib import admin
from .models import Scraper
# Register your models here.

"""
class ScraperAdmin(admin.ModelAdmin):
    list_display('title1','image1','url1')
"""
admin.site.register(Scraper)