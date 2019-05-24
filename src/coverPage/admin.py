"""Cover page config for Django Admin"""
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin

from .models import CoverPage

admin.site.register(CoverPage, PageAdmin)
