from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from COR_Company.foms import InviteUserForms


@login_required
def create_owner_company(request):

    template = 'company/createCompany.html'
    parameters = {
        'title': 'Crear Empresa'
    }
    return render(request, template, parameters)


@login_required
def edit_owner_company(request, pk):
    template = 'company/createCompany.html'
    parameters = {
        'title': 'Editar Empresa',
        'company_id': pk
    }
    return render(request, template, parameters)


@login_required
def invite_users(request, company_id):

    form = InviteUserForms()

    template = 'company/InviteUsers.html'
    parameters = {
        'form': form,
        'title': 'Editar Empresa',
        'company_id': company_id
    }
    return render(request, template, parameters)


@login_required
def detail_owner_company(request, pk):
    template = 'company/DetailOwnerCompany.html'
    parameters = {
        'pk': pk
    }
    return render(request, template, parameters)


@login_required
def create_customer_company(request, owner_company):
    template = 'company/createCustomerCompany.html'
    parameters = {
        'title': 'Crear Empresa Cliente',
        'owner_company': owner_company
    }
    return render(request, template, parameters)


@login_required
def edit_customer_company(request, owner_company, pk):
    template = 'company/createCustomerCompany.html'
    parameters = {
        'title': 'Editar Empresa Cliente',
        'owner_company': owner_company,
        'company_id': pk
    }
    return render(request, template, parameters)


@login_required
def create_contact(request, customer_company_id):
    template = 'company/createContact.html'
    parameters = {
        'title': 'Crear Contacto',
        'customer_company_id': customer_company_id
    }
    return render(request, template, parameters)


@login_required
def list_contacts(request, customer_company_id):
    template = 'company/ListContact.html'
    parameters = {
        'title': 'Editar Contacto',
        'customer_company_id': customer_company_id
    }
    return render(request, template, parameters)


@login_required
def edit_contact(request, customer_company_id, pk):
    template = 'company/createContact.html'
    parameters = {
        'title': 'Editar Contacto',
        'customer_company_id': customer_company_id,
        'contact_id': pk
    }
    return render(request, template, parameters)


@login_required
def list_opportunities(request, customer_company_id):
    template = 'company/ListOpportunities.html'
    parameters = {
        'title': 'Editar Contacto',
        'customer_company_id': customer_company_id
    }
    return render(request, template, parameters)


@login_required
def create_opportunity(request, customer_company_id):
    template = 'company/createOpportunity.html'
    parameters = {
        'title': 'Crear Oportunidad',
        'customer_company_id': customer_company_id
    }
    return render(request, template, parameters)


@login_required
def edit_opportunity(request, customer_company_id, pk):
    template = 'company/createOpportunity.html'
    parameters = {
        'title': 'Editar Oportunidad',
        'customer_company_id': customer_company_id,
        'opportunity_id': pk
    }
    return render(request, template, parameters)