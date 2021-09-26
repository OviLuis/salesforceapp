from django.conf.urls import include, url
from django.contrib import admin

from home import views
urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^home/', include('home.urls', namespace='home', app_name='home')),
    url(r'^company/', include('COR_Company.urls', namespace="Company", app_name="Company")),

    # API
    url(r'^api/', include('COR_Company.urls', namespace="Company_API", app_name="Company_API")),
    url(r'^api/', include('COR_Customer.urls', namespace="Customer_API", app_name="Customer_API")),

]
