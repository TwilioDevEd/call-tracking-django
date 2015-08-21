from django.conf.urls import include, url
from django.contrib import admin

from call_tracking.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^call-tracking', include('call_tracking.urls')),

    # Include the Django admin
    url(r'^admin/', include(admin.site.urls)),
]
