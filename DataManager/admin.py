from django.contrib import admin

# Register your models here.
from .models import Client, Bank, Bill

admin.site.register(Client)
admin.site.register(Bank)
admin.site.register(Bill)