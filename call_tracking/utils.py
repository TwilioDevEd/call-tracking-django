from django.conf import settings
from twilio.rest import Client


# Uses credentials defined in TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN
# environment variables
client = Client()

def search_phone_numbers(area_code=None):
    """Queries the Twilio REST API to get phone numbers available for puchase"""
    # You can change the country argument to search outside the US
    # area_code is an optional parameter
    country_list = client.available_phone_numbers.get('US')
    numbers = country_list.local.list(area_code=area_code)

    # Returns 30 by default - let's trim the list for UX purposes
    return numbers[:10]

def purchase_phone_number(phone_number):
    """Purchases a new phone number from the Twilio API"""
    # Use a TwiML Application SID so all our numbers use the same voice URL
    number = client.incoming_phone_numbers.create(
        phone_number=phone_number,
        voice_application_sid=settings.TWIML_APPLICATION_SID)

    return number
