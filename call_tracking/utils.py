from django.conf import settings
from twilio.rest import TwilioRestClient

import os

# Uses credentials defined in TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN
# environment variables
client = TwilioRestClient()

def get_twilio_application():
    """
    Gets the Twilio Application that will be used to configure all newly
    purchased phone numbers. Creates a sample Twilio Application if none
    is specified.
    """
    # Check if the TWILIO_APPLICATION_SID environment variable is set
    application_sid = os.environ.get('TWILIO_APPLICATION_SID', None)

    # If an Application SID is defined in the environment, use it
    if application_sid:
        application = client.applications.get(application_sid)
        return application

    # Check if a Twilio Application already exists with the name
    # "Call Tracking Demo"
    applications = client.applications.list(friendly_name='Call Tracking Demo')

    # If we found a Twilio Application in this account already, use it
    if len(applications) > 0:
        return applications[0]

    # We didn't find an Application defined in the environment or on the account
    # so we'll create one and use it
    application = client.applications.create(
        friendly_name='Call Tracking Demo',
        voice_url='http://www.example.com/call-tracking/forward-call')
    return application

def search_phone_numbers(area_code=None):
    """Queries the Twilio REST API to get phone numbers available for puchase"""
    # You can change the country argument to search outside the US
    numbers = client.phone_numbers.search(area_code=area_code, country='US')

    # Returns 30 by default - let's trim the list for UX purposes
    return numbers[:10]

def purchase_phone_number(phone_number, application_sid):
    """Purchases a new phone number from the Twilio API"""
    # Use a Twilio Application SID so all our numbers use the same voice URL
    number = client.phone_numbers.purchase(
        phone_number=phone_number,
        voice_application_sid=application_sid)

    return number
