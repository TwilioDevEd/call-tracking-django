from django.db import models
from django.db.models import Count
from django.utils.encoding import python_2_unicode_compatible
from phonenumber_field.modelfields import PhoneNumberField


@python_2_unicode_compatible
class LeadSource(models.Model):
    name = models.CharField(max_length=100, blank=True, help_text='E.g. "Downtown billboard"')
    incoming_number = PhoneNumberField(unique=True)
    forwarding_number = PhoneNumberField(blank=True, help_text='People who call this lead source will be connected with this phone number. Must include international prefix - e.g. +1 555 555 55555')

    def __str__(self):
        if self.name:
            return '{0} - {1}'.format(self.name, self.incoming_number)
        else:
            return '(not yet named) - {0}'.format(self.incoming_number)

    @classmethod
    def get_leads_per_source(cls):
        """Get the number of leads for each lead source"""
        # Use Django's annotate feature to include the number of leads
        # on each lead source
        queryset = cls.objects.annotate(Count('lead')).order_by('name')

        # Extract the source names and lead counts and make them a regular list
        data = list(queryset.values('name', 'lead__count'))

        return data


@python_2_unicode_compatible
class Lead(models.Model):
    source = models.ForeignKey(LeadSource)
    phone_number = PhoneNumberField()
    timestamp = models.DateTimeField(auto_now_add=True)

    # A couple examples of fields you could track for each incoming call
    # See https://www.twilio.com/docs/api/twiml/twilio_request for more
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)

    def __str__(self):
        return '{0}, {1} at {2}'.format(self.city, self.state, self.timestamp)

    @classmethod
    def get_leads_per_city(cls):
        """Get the number of leads for each city"""
        # Use Django's annotate feature to include the number of leads
        # from each distinct city
        queryset = cls.objects.values('city').annotate(Count('id')).order_by('city')

        # Extract the cities and lead counts and make them a regular list
        data = list(queryset.values('city', 'id__count'))

        return data
