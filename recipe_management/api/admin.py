from django.contrib import admin
from .models import Ingredient,Recipe,Comment

# Register your models here.
admin.register(Ingredient)
admin.register(Recipe)
admin.register(Comment)