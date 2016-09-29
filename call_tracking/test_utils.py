from django.conf import settings
from django.test import TestCase

from .utils import search_phone_numbers, purchase_phone_number

# Import Mock if we're running on Python 2
import six

if six.PY3:  # pragma: no cover
    from unittest.mock import patch
else:  # pragma: no cover
    from mock import patch


class SearchPhoneNumbersTest(TestCase):

    def test_search_phone_numbers(self):
        # Act
        with patch('twilio.rest.api.v2010.account.available_phone_number.local.LocalList.list') as mock:
            search_phone_numbers()

        # Assert
        self.assertTrue(mock.called)
        mock.assert_called_with(area_code=None)

    def test_search_phone_numbers_with_area_code(self):
        # Act
        with patch('twilio.rest.api.v2010.account.available_phone_number.local.LocalList.list') as mock:
            search_phone_numbers(415)

        # Assert
        self.assertTrue(mock.called)
        mock.assert_called_with(area_code=415)


class PurchasePhoneNumberTest(TestCase):

    def test_purchase_phone_number(self):
        # Act
        with patch('twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberList.create') as mock:
            purchase_phone_number(phone_number='+15555555555')

        # Assert
        self.assertTrue(mock.called)
        mock.assert_called_with(
            phone_number='+15555555555',
            voice_application_sid=settings.TWIML_APPLICATION_SID)
