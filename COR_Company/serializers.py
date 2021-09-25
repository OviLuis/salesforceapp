import datetime
import re

from rest_framework import serializers

from .models import Company, CompanyUsers


class CompanySerializer(serializers.ModelSerializer):

    def validate(self, data):
        if data.get('company_type') == Company.OWNER_COMPANY:
            if data.get('owner') is None:
                raise serializers.ValidationError('el propietaria no puede ser null')

            if data.get('father_company'):
                raise serializers.ValidationError('Una empresa propietaria no puede tener compañia padre')

        else:
            if data.get('father_company') is None:
                raise serializers.ValidationError('Una empresa cliente debe tener una compañia padre asociada')

        if data.get('web_site'):
            pattern = re.compile('(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}')
            match = pattern.match(data.get('web_site'))
            if not match:
                raise serializers.ValidationError('la url no es valida.')

        return data

    def create(self, validated_data):

        if Company.objects.filter(company_nit=validated_data.get('company_nit')).exists():
            raise serializers.ValidationError('Ya existe una empresa con el mismo nit')

        return Company.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if instance.company_type == Company.OWNER_COMPANY:
            if instance.company_nit != validated_data.get('company_nit'):
                raise serializers.ValidationError('No se permite actualizar el nit de la empresa propietaria')
            if instance.company_type != validated_data.get('company_type'):
                raise serializers.ValidationError('No se permite modificar el tipo de empresa')
            if instance.owner != validated_data.get('owner'):
                raise serializers.ValidationError('No se permite modificar el propietario de una empresa propetaria')
        return Company.objects.get(pk=instance.pk).update(**validated_data)

    class Meta:
        model = Company
        exclude = ('created_by', 'created_date', 'updated_by', 'updated_date')


class CompanyUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyUsers
        exclude = ('created_date', 'updated_date')