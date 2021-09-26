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