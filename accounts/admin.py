from django.contrib import admin
from .models import *

class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "mail"]
    list_display_links = ["name"]
    search_fields = ["name"]
    class Meta:
        model = Profile

admin.site.register(Profile, ProfileModelAdmin)

