from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.core.mail import send_mail, EmailMessage
from .serializers import NewsEmailsSerializer, NewsLetterMessagesSerializer
from .models import NewsEmails, NewsLetterMessage
from config import settings


class NewsLetterEmailCreate(generics.CreateAPIView):
    serializer_class = NewsEmailsSerializer
    queryset = NewsEmails.objects.all()


class NewsLetterEmailList(generics.ListAPIView):
    serializer_class = NewsEmailsSerializer
    permission_classes = [IsAdminUser]
    def get_queryset(self):
        return NewsEmails.objects.all()


class NewsLetterCreate(generics.CreateAPIView):
    serializer_class = NewsLetterMessagesSerializer
    permission_classes = [IsAdminUser]
    queryset = NewsLetterMessage.objects.all()



class NewsLetterList(generics.ListAPIView):
    serializer_class = NewsLetterMessagesSerializer
    permission_classes = [IsAdminUser]
    def get_queryset(self):
        return NewsLetterMessage.objects.all()


class UpdateNewsLetters(generics.UpdateAPIView):
    serializer_class = NewsLetterMessagesSerializer
    permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        data = NewsLetterMessagesSerializer(data=request.data)
        if data.is_valid():
            NewsLetter = NewsLetterMessage.objects.filter(id=self.kwargs['id']).first()

            if NewsLetter is not None:
                data.update(NewsLetter, data.validated_data)
                return Response({'message': 'News letter update'})

            else:
                return Response({'message': 'not found'})

        else:
            return Response(data.errors)




@api_view()
def SendEmail (request):
    letter = NewsLetterMessage.objects.filter(id=request.GET.get('id'), publish=True).first()
    emails = NewsEmails.objects.all()
    if letter is not None:
        subject = letter.subject
        body = letter.body
        if letter.attachment:
            attach = letter.attachment

        else:
            attach = None

        if emails is not None:

            for email in emails:
                mail = EmailMessage(subject, body, settings.EMAIL_HOST_USER, [email.Email])

                if attach is not None:
                    mail.attach(attach.name, attach.read())

                mail.send()

        else:
            return Response({'message': 'there isnt any email'})
    else:
        return Response({'message': 'id is invalid'})

    return Response({'message': 'email sent'})
