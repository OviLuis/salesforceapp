import random

from django.http import HttpResponseRedirect
from django.core.urlresolvers import resolve, reverse
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from urllib.parse import urlparse


from .forms import SignUpForm
from COR_Company.models import Company, CompanyUsers


def index(request):

    print('index........................')
    title = ''
    create_company_url = reverse('Company:create_owner_company')
    user_list = None
    if Company.objects.filter(owner=request.user):
        create_company_url = reverse('Company:create_owner_company')
        title = 'Empresas Propietarias'
        user_list = User.objects.filter(is_sttaf=0)

    elif CompanyUsers.objects.filter(id_user=request.user):
        create_company_url = None
        title = 'Empresas que me invitaron'

    template = 'index.html'
    parameters = {
        'create_company_url': create_company_url,
        'title': title,
        'user_list': user_list
    }
    return render(request, template, parameters)


def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    template = 'login.html'

    try:
        user_tmp = User.objects.get(email=email)
        user_name = user_tmp.username
    except User.DoesNotExist:
        user_name = None

    user = auth.authenticate(username=user_name, password=password)

    if request.method.upper() == 'POST':
        if user is not None and user.is_active:
            auth.login(request, user)
            return render(request, 'index.html')
        else:
            messages.add_message(request, messages.WARNING, 'Nombre de usuario o Contraseña incorrectos')

    return render(request, template)


def logout(request):
    request.session['redirect_to'] = None
    request.META['HTTP_REFERER'] = None
    auth.logout(request)
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            partitioned_email = email.partition('@')[0]
            random_num = random.randint(1, 999)
            username = '{}{}'.format(partitioned_email, random_num)
            form.instance.username = username
            form.save()
            # username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = auth.authenticate(username=username, password=raw_password)
            auth.login(request, user)
            return render(request, 'index.html')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})
