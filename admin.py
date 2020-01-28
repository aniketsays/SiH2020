from django.contrib import admin
from .models import Farmer, Financial, NonFinancial, inputCrops

admin.site.register(Farmer)
#admin.site.register(Financial)
#admin.site.register(NonFinancial)
admin.site.register(inputCrops)