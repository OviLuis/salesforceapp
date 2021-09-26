from django.shortcuts import render

from COR_Company.foms import InviteUserForms


def create_owner_company(request):

    template = 'company/createCompany.html'
    parameters = {
        'title': 'Crear Empresa'
    }
    return render(request, template, parameters)


def edit_owner_company(request, pk):
    template = 'company/createCompany.html'
    parameters = {
        'title': 'Editar Empresa',
        'company_id': pk
    }
    return render(request, template, parameters)


def invite_users(request, company_id):

    form = InviteUserForms()

    template = 'company/InviteUsers.html'
    parameters = {
        'form': form,
        'title': 'Editar Empresa',
        'company_id': company_id
    }
    return render(request, template, parameters)


def detail_owner_company(request, pk):
    template = 'company/DetailOwnerCompany.html'
    parameters = {
        'pk': pk
    }
    return render(request, template, parameters)


def create_customer_company(request, owner_company):
    template = 'company/createCustomerCompany.html'
    parameters = {
        'title': 'Crear Empresa Cliente',
        'owner_company': owner_company
    }
    return render(request, template, parameters)


def edit_customer_company(request, owner_company, pk):
    template = 'company/createCustomerCompany.html'
    parameters = {
        'title': 'Editar Empresa Cliente',
        'owner_company': owner_company,
        'company_id': pk
    }
    return render(request, template, parameters)


def create_contact(request):
    template = 'company/createContact.html'
    parameters = {
        'title': 'Crear Contacto'
    }
    return render(request, template, parameters)


def edit_contact(request):
    template = 'company/createContact.html'
    parameters = {
        'title': 'Editar Contacto'
    }
    return render(request, template, parameters)


def create_opportunity(request):
    template = 'company/createOpportunity.html'
    parameters = {
        'title': 'Crear Oportunidad'
    }
    return render(request, template, parameters)


def edit_opportunity(request):
    template = 'company/createOpportunity.html'
    parameters = {
        'title': 'Editar Oportunidad'
    }
    return render(request, template, parameters)