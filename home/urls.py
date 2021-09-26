from django.conf.urls import patterns, url

from home import views

urlpatterns = patterns(
    '',

    # url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^login/$', views.login, name='login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    # url(r'^password_change/$', password_change, name='password_change'),
    # url(r'^NotFound/$', handler404, name='handler404'),
)