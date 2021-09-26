from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns


from .api_views import CompanyViewSet, CompanyUsersViewSet, customer_companies_by_user, companies_by_invited_user
from .views import create_owner_company, edit_owner_company, invite_users, create_customer_company, edit_customer_company, create_contact, \
    create_opportunity, edit_contact, edit_opportunity, detail_owner_company


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
    url(r'^v1/companies/invited-users/(?P<invited_user_id>-?\d+)/$', companies_by_invited_user, name='companies_by_invited_user'),
    url(r'^v1/companies/customers/(?P<user_id>-?\d+)/$', customer_companies_by_user, name='customer_companies_by_user'),


    url(r'^v1/companyUsers/$', company_users, name='company_users'),
    url(r'^v1/users-by-company/(?P<id_company>-?\d+)/$', users_by_company, name='users_by_company'),
    url(r'^v1/companyUsers/(?P<pk>-?\d+)/$', company_user_detail, name='company_user_detail'),

    # Empresas propietaria
    url(r'^CreateOwnerCompany/$', create_owner_company, name='create_owner_company'),
    url(r'^EditOwnerCompany/(?P<pk>-?\d+)/$', edit_owner_company, name='edit_owner_company'),
    url(r'^InviteUser/(?P<company_id>-?\d+)/$', invite_users, name='invite_users'),
    url(r'^DetailOwnerCompany/(?P<pk>-?\d+)/$', detail_owner_company, name='detail_owner_company'),



    # Empresas cliente
    url(r'^CreateCustomerCompany/(?P<owner_company>-?\d+)$', create_customer_company, name='create_customer_company'),
    url(r'^EditCustomerCompany/(?P<owner_company>-?\d+)/(?P<pk>-?\d+)/$', edit_customer_company, name='edit_owner_company'),
    url(r'^CreateContact/(?P<company_id>-?\d+)/$', create_contact, name='invite_users'),

]


urlpatterns = format_suffix_patterns(urlpatterns)
