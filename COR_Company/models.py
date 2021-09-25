from django.db import models

from django.contrib.auth.models import User


class Company(models.Model):

    OWNER_COMPANY = 1
    CUSTOMER_COMPANY = 2

    COMPANY_TYPE_CHOICES = (
        (OWNER_COMPANY, 'PROPIETARIA'),
        (CUSTOMER_COMPANY, 'CLIENTE')
    )

    id = models.AutoField(primary_key=True, verbose_name="ID")
    owner = models.ForeignKey(User, verbose_name='Propietario', related_name='company_owner', on_delete=models.PROTECT, null=True, blank=True)
    company_nit = models.IntegerField(verbose_name='NIT')
    company_name = models.CharField(verbose_name='Nombre Empresa', max_length=200)
    commercial_name = models.CharField(verbose_name='Nombre Comercial', max_length=200)
    address = models.CharField(verbose_name='Direccion', max_length=200)
    phone_number = models.CharField(verbose_name='Telefono', max_length=20)
    email = models.EmailField(verbose_name='Correo Electronico', null=True, blank=True)
    web_site = models.CharField(verbose_name='Sitio Web', null=True, blank=True, max_length=200)
    country = models.CharField(verbose_name='Pais', max_length=100)
    state = models.CharField(verbose_name='Estado/Departamento', max_length=100)
    city = models.CharField(verbose_name='Ciudad', max_length=100)
    company_type = models.IntegerField(verbose_name='Tipo Empresa', choices=COMPANY_TYPE_CHOICES)
    father_company = models.ForeignKey('self', verbose_name='Empresa Padre', blank=True, null=True)
    created_by = models.ForeignKey(User, db_column='created_by', related_name='company_created_by',
                                   on_delete=models.PROTECT, verbose_name='Creado por')
    created_date = models.DateField(auto_now=True, editable=False, verbose_name='Fecha Creacion')
    updated_by = models.ForeignKey(User, blank=True, null=True, db_column='updated_by',
                                   related_name='company_updated_by',
                                   on_delete=models.PROTECT, verbose_name='Modificado por')
    updated_date = models.DateField(blank=True, null=True, verbose_name='Fecha Modificacion')

    def __str__(self):
        return '%d-%s' % (self.id, self.company_name)

    class Meta:
        managed = True
        db_table = 'company'
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'


class CompanyUsers(models.Model):
    ACTIVE_STATUS = 'S'
    INACTIVE_STATUS = 'N'

    id = models.AutoField(primary_key=True, verbose_name="ID")
    id_company = models.ForeignKey(Company, verbose_name='Empresa', on_delete=models.PROTECT)
    id_user = models.ForeignKey(User, verbose_name='Usuario', on_delete=models.PROTECT)
    status = models.CharField(verbose_name='Estado', default=ACTIVE_STATUS, max_length=5)
    created_date = models.DateField(auto_now=True, editable=False, verbose_name='Fecha Creacion')
    updated_date = models.DateField(blank=True, null=True, verbose_name='Fecha Modificacion')

    def __str__(self):
        return '%d' % self.id

    class Meta:
        managed = True
        db_table = 'company_users'
        verbose_name = 'Usuario Invitado'
        verbose_name_plural = 'Usuarios Invitados'
