from django.conf import settings
from twilio.rest import TwilioRestClient

import os

# Uses credentials defined in TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN
# environment variables
client = TwilioRestClient()


def search_phone_numbers(area_code=None):
    """Queries the Twilio REST API to get phone numbers available for puchase"""
    # You can change the country argument to search outside the US
    numbers = client.phone_numbers.search(area_code=area_code, country='US')

    # Returns 30 by default - let's trim the list for UX purposes
    return numbers[:10]


def purchase_phone_number(phone_number):
    """Purchases a new phone number from the Twilio API"""
    # Use a Twilio Application SID so all our numbers use the same voice URL
    number = client.phone_numbers.purchase(
        phone_number=phone_number,
        voice_application_sid=settings.TWILIO_APPLICATION_SID)

    return number
