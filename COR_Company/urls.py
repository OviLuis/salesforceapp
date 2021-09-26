from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns


from .api_views import CompanyViewSet, CompanyUsersViewSet, customer_companies_by_user
from .views import create_owner_company, edit_owner_company, invite_users


company_list = CompanyViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
company_detail = CompanyViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

companies_by_user_owner = CompanyViewSet.as_view({
    'get': 'list'
})

company_users = CompanyUsersViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

users_by_company = CompanyUsersViewSet.as_view({
    'get': 'list',
})

company_user_detail = CompanyUsersViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy',

})


urlpatterns = [
    url(r'^v1/companies/$', company_list, name='company_list'),
    url(r'^v1/companies/(?P<pk>-?\d+)/$', company_detail, name='company_detail'),
    url(r'^v1/companies/customers/(?P<user_id>-?\d+)/$', customer_companies_by_user, name='customer_companies_by_user'),


    url(r'^v1/companyUsers/$', company_users, name='company_users'),
    url(r'^v1/users-by-company/(?P<id_company>-?\d+)/$', users_by_company, name='users_by_company'),
    url(r'^v1/companyUsers/(?P<pk>-?\d+)/$', company_user_detail, name='company_user_detail'),

    url(r'^CreateOwnerCompany/$', create_owner_company, name='create_owner_company'),
    url(r'^EditOwnerCompany/(?P<pk>-?\d+)/$', edit_owner_company, name='edit_owner_company'),
    url(r'^InviteUser/(?P<company_id>-?\d+)/$', invite_users, name='invite_users'),

]


urlpatterns = format_suffix_patterns(urlpatterns)
