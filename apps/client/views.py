from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from apps.client.models import Contact
from apps.client.serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):

    model = Contact
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [AllowAny, ]
