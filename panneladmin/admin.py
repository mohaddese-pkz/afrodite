from django.contrib import admin
from .models import *


admin.site.register(WholeBuyerUser)
@admin.register(SettleMent)
class SettleMentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'date')
