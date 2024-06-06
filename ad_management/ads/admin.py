from django.contrib import admin

from ads.models import AdLocation, AdSpend, BusinessCrypto
# Register your models here.

admin.site.register(AdLocation)
admin.site.register(AdSpend)
admin.site.register(BusinessCrypto)

