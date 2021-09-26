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
    if Company.objects.filter(owner=request.user):
        create_company_url = reverse('Company:create_owner_company')
        title = 'Empresas Propietarias'

    elif CompanyUsers.objects.filter(id_user=request.user):
        create_company_url = None

    else:
        create_company_url = None

    template = 'index.html'
    parameters = {
        'create_company_url': create_company_url,
        'title': title
    }
    return render(request, template, parameters)


def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    template = 'login.html'
    if 'HTTP_REFERER' in request.META:
        referer_url = request.META['HTTP_REFERER']
        url_rq_from = urlparse(referer_url)[2]

        if request.GET.get('next'):
            request.session['redirect_to'] = request.GET.get('next')
        elif request.path != url_rq_from:
            request.session['redirect_to'] = url_rq_from

    try:
        user_tmp = User.objects.get(email=email)
        user_name = user_tmp.username
    except User.DoesNotExist:
        user_name = None

    user = auth.authenticate(username=user_name, password=password)

    if request.method.upper() == 'POST':
        if user is not None and user.is_active:
            auth.login(request, user)
            if request.session.get('redirect_to'):
                return HttpResponseRedirect(request.session.get('redirect_to'))
            else:
                return HttpResponseRedirect(reverse('home:index'))
        else:
            messages.add_message(request, messages.WARNING, 'Nombre de usuario o Contraseña incorrectos')

    return render(request, template)


def logout(request):
    request.session['redirect_to'] = None
    request.META['HTTP_REFERER'] = None
    auth.logout(request)
    return HttpResponseRedirect(reverse('home:index'))


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
            return HttpResponseRedirect(reverse('home:index'))
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})
