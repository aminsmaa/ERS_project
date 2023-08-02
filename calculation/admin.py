from django.contrib import admin

from .models import Calculation


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'name', 'date_modified')

admin.site.register(Calculation, PostAdmin)
