import datetime


from rest_framework import generics, permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User


from .models import Company, CompanyUsers
from .serializers import CompanySerializer, CompanyUsersSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('-id')
    serializer_class = CompanySerializer
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

    def update(self, request, *args, **kwargs):
        print()
        updated_by = User.objects.get_by_natural_key('logonzalez')
        data = self.request.data

        serializer = self.get_serializer(self.get_object(), data=data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['updated_by'] = updated_by
        self.perform_update(serializer)
        headers = self.get_success_headers(serializer.data)
        final_status = status.HTTP_200_OK
        return Response(status=final_status, template_name=None, content_type=None)


class CompanyUsersViewSet(viewsets.ModelViewSet):
    queryset = CompanyUsers.objects.all().order_by('-id')
    serializer_class = CompanyUsersSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        id_company = self.kwargs.get('id_company')
        if id_company:
            return CompanyUsers.objects.filter(id_company__id=id_company)
        return self.queryset

    def create(self, request, *args, **kwargs):
        data = self.request.data
        serializer = CompanyUsersSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        # serializer.validated_data['updated_by'] = updated_by
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        final_status = status.HTTP_200_OK
        return Response(status=final_status, template_name=None, content_type=None)

    def destroy(self, request, *args, **kwargs):
        print(self.get_object())

        instance = self.get_object()

        instance.status = CompanyUsers.INACTIVE_STATUS
        instance.updated_date = datetime.datetime.today()
        instance.save()

        final_status = status.HTTP_200_OK
        return Response(status=final_status, template_name=None, content_type=None)
