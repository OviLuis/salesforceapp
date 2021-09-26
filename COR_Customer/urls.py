from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns


from .api_views import ContactViewSet, BusinessOpportunityViewSet, contacts_by_company


contact_list = ContactViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
contact_detail = ContactViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

business_opportunity_list = BusinessOpportunityViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
business_opportunity_detail = BusinessOpportunityViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    url(r'^v1/contacts/$', contact_list, name='contact_list'),
    url(r'^v1/contacts/(?P<pk>-?\d+)/$', contact_detail, name='contact_detail'),
    url(r'^v1/contacts/customer-company/(?P<customer_company>-?\d+)/$', contacts_by_company, name='contacts_by_company'),
    url(r'^v1/opportunities/$', business_opportunity_list, name='business_opportunity_list'),
    url(r'^v1/opportunities/(?P<pk>-?\d+)/$', business_opportunity_detail, name='business_opportunity_detail'),

]


urlpatterns = format_suffix_patterns(urlpatterns)
