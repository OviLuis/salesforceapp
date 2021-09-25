from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include('COR_Company.urls', namespace="Company_API", app_name="Company_API")),
    url(r'^api/', include('COR_Customer.urls', namespace="Customer_API", app_name="Customer_API")),

]
