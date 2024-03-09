from django.contrib import admin
from builds.models import Builds

class BuildsAdmin(admin.ModelAdmin):
    list_display = ['nome', 'classe']


admin.site.register(Builds, BuildsAdmin)