from django.db import models

from django.contrib.auth.models import User

from COR_Company.models import Company


class Contact(models.Model):
    ACTIVE_STATUS = 'S'
    INACTIVE_STATUS = 'N'

    id = models.AutoField(primary_key=True, verbose_name="UUID")
    first_name = models.CharField(verbose_name='Primer nombre', max_length=100)
    middle_name = models.CharField(verbose_name='Segundo Nombre', blank=True, null=True, max_length=100)
    last_name = models.CharField(verbose_name='Apellidos', max_length=200)
    email = models.EmailField(verbose_name='Correo Electronico', null=True, blank=True)
    phone_number = models.CharField(verbose_name='Telefono', max_length=20)
    mobile_phone_number = models.CharField(verbose_name='Celular', null=True, blank=True, max_length=20)
    id_company = models.ForeignKey(Company, verbose_name='ID Empresa')
    status = models.CharField(verbose_name='Estado', default=ACTIVE_STATUS, max_length=5)
    created_by = models.ForeignKey(User, db_column='created_by', related_name='contact_created_by',
                                   on_delete=models.PROTECT, verbose_name='Creado por')
    created_date = models.DateField(auto_now=True, editable=False, verbose_name='Fecha Creacion')
    updated_by = models.ForeignKey(User, blank=True, null=True, db_column='updated_by',
                                   related_name='contact_updated_by',
                                   on_delete=models.PROTECT, verbose_name='Modificado por')
    updated_date = models.DateField(blank=True, null=True, verbose_name='Fecha Modificacion')

    def __str__(self):
        return '%d' % self.id

    class Meta:
        managed = True
        db_table = 'contact'
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'


class BusinessOpportunity(models.Model):
    ACTIVE_STATUS = 'S'
    INACTIVE_STATUS = 'N'

    PROCESS_STATUS = 'P'
    ACCEPTED_STATUS = 'W'
    NO_ACCEPTED_STATUS = 'NW'
    CANCEL_STATUS = 'D'

    OPPORTUNITY_CHOICES = (
        (PROCESS_STATUS, 'EN PROCESO'),
        (ACCEPTED_STATUS, 'GANADA'),
        (NO_ACCEPTED_STATUS, 'NO GANADA'),
        (CANCEL_STATUS, 'CANCELADA')
    )

    id = models.AutoField(primary_key=True, verbose_name="UUID")
    id_company = models.ForeignKey(Company, verbose_name='Empresa')
    id_contact = models.ForeignKey(Contact, verbose_name='Contacto')
    opportunity_name = models.CharField(verbose_name='Nombre', max_length=100)
    opportunity_value = models.IntegerField(verbose_name='Monto')
    status = models.CharField(verbose_name='Estado', choices=OPPORTUNITY_CHOICES, max_length=5)
    active = models.CharField(verbose_name='Activo/Inactivo', default=ACTIVE_STATUS, max_length=5)
    created_by = models.ForeignKey(User, db_column='created_by', related_name='opportunity_created_by',
                                   on_delete=models.PROTECT, verbose_name='Creado por')
    created_date = models.DateField(auto_now=True, editable=False, verbose_name='Fecha Creacion')
    updated_by = models.ForeignKey(User, blank=True, null=True, db_column='updated_by',
                                   related_name='opportunity_updated_by',
                                   on_delete=models.PROTECT, verbose_name='Modificado por')
    updated_date = models.DateField(blank=True, null=True, verbose_name='Fecha Modificacion')

    def __str__(self):
        return '%d' % self.id

    class Meta:
        managed = True
        db_table = 'business_opportunity'
        verbose_name = 'Oportunidad de Negocio'
        verbose_name_plural = 'Oportunidades de Negocio'
