import datetime


from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User


from .models import Company, CompanyUsers
from .serializers import CompanySerializer, CompanyUsersSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('-id')
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        created_by = request.user
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
        updated_by = request.user
        data = self.request.data

        serializer = self.get_serializer(self.get_object(), data=data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['updated_by'] = updated_by
        self.perform_update(serializer)
        headers = self.get_success_headers(serializer.data)
        final_status = status.HTTP_200_OK
        return Response(status=final_status, template_name=None, content_type=None)

    def get_queryset(self):

        # Muestra las companias propietarias creadas por el usuario autenticado
        if not self.request.user.is_staff:
            return Company.objects.filter(owner=self.request.user, company_type=Company.OWNER_COMPANY)

        return self.queryset

    def destroy(self, request, *args, **kwargs):
        print(self.get_object())

        instance = self.get_object()

        instance.status = 'N'
        instance.updated_date = datetime.datetime.today()
        instance.updated_by = request.user
        instance.save()

        final_status = status.HTTP_200_OK
        return Response(status=final_status, template_name=None, content_type=None)


@api_view(['GET'])
def customer_companies_by_user(request, user_id):
    """
    Obtener el listado de companias por usuario propietario
    :param request:
    :param user_id: id del usauario propietario
    :return:
    """
    print('request.kwargs..............')
    print(request.GET)
    # user_id = request.GET.get('user_id')
    print(user_id)
    try:
        user_obj = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        data = {'message': 'El id del usuario incorrecto'}
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    qs = Company.objects.filter(created_by=user_obj, company_type=Company.CUSTOMER_COMPANY)

    serializer = CompanySerializer(qs)
    data = serializer.data

    return Response(data=data, status=status.HTTP_200_OK)


class CompanyUsersViewSet(viewsets.ModelViewSet):
    queryset = CompanyUsers.objects.all().order_by('-id')
    serializer_class = CompanyUsersSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        id_company = self.kwargs.get('id_company')
        if id_company:
            return CompanyUsers.objects.filter(id_company__id=id_company, status='S')
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

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        data = {}
        if qs:
            users_by_company = []
            for user in qs:
                obj = {
                    'id': user.id,
                    'status': user.status,
                    'id_company': user.id_company.pk,
                    'comp_name': user.id_company.commercial_name,
                    'id_user': user.id_user.pk,
                    'user_name': user.id_user.get_full_name(),
                    'las_login': user.id_user.last_login

                }
                users_by_company.append(obj)

            data = users_by_company
        final_status = status.HTTP_200_OK
        return Response(data=data, status=final_status, template_name=None, content_type=None)