from django.contrib import admin
from .models import *


@admin.register(User)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['email', 'username']