from django.contrib import admin

from .models import(Artist, Album, Image, Tag)


admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Image)
admin.site.register(Tag)


