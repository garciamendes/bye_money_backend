from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'user', 'theme']
    search_fields = ['uuid', 'user']


admin.site.register(Profile, ProfileAdmin)
