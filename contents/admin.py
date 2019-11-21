from django.contrib import admin

from contents.models import Gram, Image


class ImageInline(admin.TabularInline):
    model = Image


class GramAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ["id", "title", "updated_at"]


admin.site.register(Gram, GramAdmin)
admin.site.register(Image)
