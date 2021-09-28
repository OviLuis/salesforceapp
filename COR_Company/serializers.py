import datetime
import re

from rest_framework import serializers

from Util.utilities import validate_phone_number

from .models import Company, CompanyUsers


class CompanySerializer(serializers.ModelSerializer):

    def validate(self, data):
        if data.get('company_type') == Company.OWNER_COMPANY:
            if data.get('owner') is None:
                raise serializers.ValidationError('el propietario no puede ser null')

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

        if data.get('phone_number'):
            if not validate_phone_number(data.get('phone_number')):
                raise serializers.ValidationError('Debe ingresar un numero de telefono valido para Colombia. Debe incluir el código de area +57')

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
                raise serializers.ValidationError('No se permite modificar el propietario de una empresa propietaria')

        instance.company_name = validated_data.get('company_name')
        instance.commercial_name = validated_data.get('commercial_name')
        instance.address = validated_data.get('address')
        instance.phone_number = validated_data.get('phone_number')
        instance.email = validated_data.get('email')
        instance.web_site = validated_data.get('web_site')
        instance.country = validated_data.get('country')
        instance.state = validated_data.get('state')
        instance.city = validated_data.get('city')
        instance.updated_by = validated_data.get('updated_by')
        instance.updated_date = datetime.datetime.today()
        instance.save()
        return instance

    class Meta:
        model = Company
        exclude = ('created_by', 'created_date', 'updated_by', 'updated_date')


class CompanyUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyUsers
        exclude = ('created_date', 'updated_date')