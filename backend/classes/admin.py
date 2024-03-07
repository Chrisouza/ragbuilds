from django.contrib import admin
from classes.models import Classes


class ClassesAdmin(admin.ModelAdmin):
    list_display = ["nome", "pk"]


admin.site.register(Classes, ClassesAdmin)
