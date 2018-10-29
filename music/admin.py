from django.contrib import admin

# Register your models here.
from .models import Album, songs

admin.site.register(Album)
admin.site.register(songs)