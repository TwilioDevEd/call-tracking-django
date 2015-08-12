from django.conf.urls import url

from .views import list_numbers, purchase_number, forward_call, LeadSourceUpdateView, leads_by_source, leads_by_city

urlpatterns = [
    # URLs for searching for and purchasing a new Twilio number
    url(r'^/list-numbers$', list_numbers, name='list_numbers'),
    url(r'^/purchase-number$', purchase_number, name='purchase_number'),

    # Endpoint Twilio will use for incoming calls
    url(r'^/forward-call$', forward_call, name='forward_call'),

    # Lead Source edit and delete views
    url(r'^/(?P<pk>[0-9]+)/edit$',
        LeadSourceUpdateView.as_view(),
        name='edit_lead_source'),

    # JSON URLs for the bar chart data
    url(r'^/leads-by-source$', leads_by_source, name='leads_by_source'),
    url(r'^/leads-by-city$', leads_by_city, name='leads_by_city')
]
