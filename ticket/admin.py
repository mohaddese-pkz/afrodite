from django.contrib import admin
from .models import *

admin.site.register(Section)
admin.site.register(Ticket)
admin.site.register(TicketMessages)


# class TicketMessages(admin.TabularInline):
#     model = TicketMessages
#
# @admin.register(Ticket)
# class Ticket(admin.ModelAdmin):
#     # list_display = ('title',)
#     list_display = [field.name for field in Ticket._meta.get_fields()]
#
#     inlines = [TicketMessages]