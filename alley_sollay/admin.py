from django.contrib import admin
from .models import Black
# Register your models here.
class BlackAdmin(admin.ModelAdmin):
    list_display = ['Tshirt', 'Size', 'Color']

admin.site.register(Black,BlackAdmin)