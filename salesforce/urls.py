from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),

    url(r'^Company/api/', include('COR_Company.urls', namespace="Company_API", app_name="Company_API")),
]
