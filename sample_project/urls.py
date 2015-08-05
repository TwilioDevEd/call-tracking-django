from django.conf.urls import include, url
from django.contrib import admin

from call_tracking.views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^call-tracking', include('call_tracking.urls')),

    # Include the Django admin
    url(r'^admin/', include(admin.site.urls)),
]
