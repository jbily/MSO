from django.contrib import admin

from .models import Actus, PageBase


@admin.register(Actus)
class ActusAdmin(admin.ModelAdmin):
    search_fields = ['title', 'writer_by']


class ActusInline(admin.TabularInline):
    fields = ["title", "resume", "created_at", "publish"]
    verbose_name = "Actuality"
    verbose_name_plural = "Actualities"


@admin.register(PageBase)
class PageBaseAdmin(admin.ModelAdmin):
    fields = ["title", "body", "page_concept", "resume"]
