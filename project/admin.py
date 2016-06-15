from django.contrib import admin
from .models import Project
from .models import AccountingItem
from .models import ItemInProject

admin.site.register(Project)
admin.site.register(AccountingItem)
admin.site.register(ItemInProject)