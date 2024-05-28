from django.contrib import admin
from .models import Apps


class AppAdmin(admin.ModelAdmin):
    list_display = ("title","description")
    search_fields = ("title",)


admin.site.register(Apps, AppAdmin)