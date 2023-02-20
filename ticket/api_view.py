import random
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import *
from .models import *
from customaccount.models import Profile

class TicketCreate(generics.CreateAPIView):
    serializer_class = TicketSerializer
    def post(self, request, *args, **kwargs):
        data = TicketSerializer(data=self.request.data)
        if data.is_valid():
            data.save()
            flag = 0
            code = 0
            while flag != 1:
                code = random.randint(10000, 100000)
                check = Ticket.objects.filter(code=code).first()
                if check == None:
                    flag = 1
            data.instance.code = code
            data.save()
            return Response({'message': 'done'})
        else:
            return Response(data.errors)


class TicketMessageCreate(generics.CreateAPIView):
    serializer_class = TicketMessagesSerializer
    queryset = TicketMessages.objects.all()



class TicketDetailsList(generics.ListAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        id = self.kwargs['id']
        return Ticket.objects.filter(user_id=id)


class TicketMessagesList(generics.ListAPIView):
    serializer_class = TicketMessagesSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return TicketMessages.objects.filter(ticket_id=id)

class TicketMessagesDetails(generics.ListAPIView):
    serializer_class = TicketMessagesSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return TicketMessages.objects.filter(id=id)
