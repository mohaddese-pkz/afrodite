from django.urls import path
from . import api_view

urlpatterns = [
    path('create/', api_view.TicketCreate.as_view(), name='ticket_create'),
    path('list/details/<int:id>', api_view.TicketDetailsList.as_view(), name='ticket_details'),
    path('create/message/', api_view.TicketMessageCreate.as_view(), name='ticket_create_message'),
    path('list/message/<int:id>', api_view.TicketMessagesList.as_view(), name='ticket_list_message'),
    path('message/details/<int:id>', api_view.TicketMessagesDetails.as_view(), name='ticket_message_details'),
]