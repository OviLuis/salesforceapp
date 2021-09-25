from rest_framework import serializers

from COR_Company.models import Company

from .models import Contact, BusinessOpportunity


class ContactSerializer(serializers.ModelSerializer):
    def validate(self, attrs):

        if attrs.get('id_company'):
            company = attrs.get('id_company')
            if company.company_type != Company.CUSTOMER_COMPANY:
                raise serializers.ValidationError('La compania asociada no es una compañia cliente')

        return attrs

    class Meta:
        model = Contact
        exclude = ('created_by', 'created_date', 'updated_by', 'updated_date')


class BusinessOpportunitytSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessOpportunity
        exclude = ('created_by', 'created_date', 'updated_by', 'updated_date')