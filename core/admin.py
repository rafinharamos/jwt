from django.contrib import admin
from .models import Sales, Administration


class SalesAdmin(admin.ModelAdmin):
    pass


class AdministrationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Sales, SalesAdmin)
admin.site.register(Administration, AdministrationAdmin)
