from django.contrib import admin

from .models import Book, Audio


admin.site.register(Book)
admin.site.register(Audio)