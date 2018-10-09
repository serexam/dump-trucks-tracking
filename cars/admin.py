from django.contrib import admin
from .models import DumpTruck, DumpTruckModel

admin.site.register(DumpTruck)
class DumpTruckAdmin(admin.ModelAdmin):
    list_display = ('number',)
    



admin.site.register(DumpTruckModel)
