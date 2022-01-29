from django.contrib import admin
from .models import *

class AlbumModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["name"]
    search_fields = ["name"]
    class Meta:
        model = Album

admin.site.register(Album, AlbumModelAdmin)

