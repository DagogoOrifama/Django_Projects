from django.contrib import admin
from .models import Item # same as from food.models import Item

# Register your models here.
admin.site.register(Item)