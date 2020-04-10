from django.contrib import admin 
from .models import Quote

class QuoteAdmin(admin.ModelAdmin):
    list_display = ("id", "subject", "author", "quote")

admin.site.register(Quote, QuoteAdmin)

