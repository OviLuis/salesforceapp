import datetime

from rest_framework import generics, permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from django.contrib.auth.models import User

from .models import Contact, BusinessOpportunity
from .serializers import ContactSerializer, BusinessOpportunitytSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('-id')
    serializer_class = ContactSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        created_by = User.objects.get_by_natural_key('logonzalez')
        data = self.request.data

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['created_by'] = created_by
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        final_status = status.HTTP_200_OK
        return Response(status=final_status, template_name=None, content_type=None)

    def destroy(self, request, *args, **kwargs):
        print(self.get_object())

        instance = self.get_object()

        instance.status = Contact.INACTIVE_STATUS
        instance.updated_date = datetime.datetime.today()
        instance.save()

        final_status = status.HTTP_200_OK
        return Response(status=final_status, template_name=None, content_type=None)


class BusinessOpportunityViewSet(viewsets.ModelViewSet):
    queryset = BusinessOpportunity.objects.all().order_by('-id')
    serializer_class = BusinessOpportunitytSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        created_by = User.objects.get_by_natural_key('logonzalez')
        data = self.request.data

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['created_by'] = created_by
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        final_status = status.HTTP_200_OK
        return Response(status=final_status, template_name=None, content_type=None)

    def destroy(self, request, *args, **kwargs):
        print(self.get_object())

        instance = self.get_object()

        instance.active = BusinessOpportunity.INACTIVE_STATUS
        instance.updated_date = datetime.datetime.today()
        instance.save()

        final_status = status.HTTP_200_OK
        return Response(status=final_status, template_name=None, content_type=None)


@api_view(['GET'])
def contacts_by_company(request, customer_company):

    qs = Contact.objects.filter(id_company__pk=customer_company)

    serializer = ContactSerializer(qs, many=True)
    data = serializer.data

    return Response(data=data, status=status.HTTP_200_OK)
