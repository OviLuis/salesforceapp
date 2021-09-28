from rest_framework import serializers

from COR_Company.models import Company

from .models import Contact, BusinessOpportunity

from Util.utilities import validate_phone_number


class ContactSerializer(serializers.ModelSerializer):
    def validate(self, attrs):

        if attrs.get('id_company'):
            company = attrs.get('id_company')
            if company.company_type != Company.CUSTOMER_COMPANY:
                raise serializers.ValidationError('La compania asociada no es una compañia cliente')

        if attrs.get('phone_number'):
            if not validate_phone_number(attrs.get('phone_number')):
                raise serializers.ValidationError('Debe ingresar un numero de telefono valido para Colombia. Debe incluir el código de area +57')
        if attrs.get('mobile_phone_number'):
            if not validate_phone_number(attrs.get('mobile_phone_number')):
                raise serializers.ValidationError('Debe ingresar un numero de celular valido para Colombia. Debe incluir el código de area +57')

        return attrs

    class Meta:
        model = Contact
        exclude = ('created_by', 'created_date', 'updated_by', 'updated_date')


class BusinessOpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessOpportunity
        exclude = ('created_by', 'created_date', 'updated_by', 'updated_date')