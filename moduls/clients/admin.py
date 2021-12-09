from django.contrib import admin
from .models import * 
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from moduls.clients.models import Client

# Register your models here.
admin.site.register(Client)