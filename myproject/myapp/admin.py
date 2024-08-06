from django.contrib import admin

# Register your models here.
from .models import Game

class GameAdmin(admin.ModelAdmin):
    list_display = ['type', 'teamone', 'teamtwo', 'gametime']

admin.site.register(Game, GameAdmin)