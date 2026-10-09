from django.contrib import admin
from .models import Menu, MenuItem, Component
from django.contrib.admin.models import LogEntry

# Register your models here.

admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(Component)
admin.site.register(LogEntry)
