from django.contrib import admin
from .models import Project
from .models import AccountingItem

admin.site.register(Project)
admin.site.register(AccountingItem)