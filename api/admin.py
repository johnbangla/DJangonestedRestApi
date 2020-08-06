from django.contrib import admin

# Register your models here.

from .models import Task, Item, Category, Album, IImage, Location

admin.site.register(Task)
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Album)
admin.site.register(IImage)
admin.site.register(Location)
