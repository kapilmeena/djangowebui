from django.contrib import admin
from .models import Page
# Register your models here.


@admin.register(Page)
class PageModel(admin.ModelAdmin):
    pass
# admin.site.register(Page)
