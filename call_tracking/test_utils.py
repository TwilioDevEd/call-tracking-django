from django.test import TestCase

from .utils import search_phone_numbers, purchase_phone_number, get_twilio_application

# Import Mock if we're running on Python 2
import six

if six.PY3: # pragma: no cover
    from unittest.mock import patch
else: # pragma: no cover
    from mock import patch


class SearchPhoneNumbersTest(TestCase):

    def test_search_phone_numbers(self):
        # Act
        with patch('twilio.rest.resources.phone_numbers.AvailablePhoneNumbers.list') as mock:
            search_phone_numbers()

        # Assert
        self.assertTrue(mock.called)
        mock.assert_called_with(area_code=None, country='US')

    def test_search_phone_numbers_with_area_code(self):
        # Act
        with patch('twilio.rest.resources.phone_numbers.AvailablePhoneNumbers.list') as mock:
            search_phone_numbers(415)

        # Assert
        self.assertTrue(mock.called)
        mock.assert_called_with(area_code=415, country='US')


class PurchasePhoneNumberTest(TestCase):

    def test_purchase_phone_number(self):
        # Act
        with patch('twilio.rest.resources.phone_numbers.PhoneNumbers.purchase') as mock:
            purchase_phone_number(
                phone_number='+15555555555',
                application_sid='testsid')

        # Assert
        self.assertTrue(mock.called)
        mock.assert_called_with(
            phone_number='+15555555555',
            voice_application_sid='testsid')

class TwilioApplicationTest(TestCase):

    def test_app_sid_found_in_environment(self):
        # Arrange
        mock_application = object()

        # Act
        with patch('os.environ.get', return_value='testsid') as environ_mock:
            with patch('twilio.rest.resources.applications.Applications.get', return_value=mock_application) as twilio_mock:
                application = get_twilio_application()

        # Assert
        self.assertTrue(twilio_mock.called)
        twilio_mock.assert_called_with('testsid')
        self.assertEqual(application, mock_application)

    def test_app_found_in_list(self):
        # Arrange
        mock_application = object()
        mock_app_list = [mock_application]

        # Act
        with patch('os.environ.get', return_value=None):
            with patch('twilio.rest.resources.applications.Applications.list', return_value=mock_app_list) as twilio_mock:
                application = get_twilio_application()

        # Assert
        self.assertTrue(twilio_mock.called)
        twilio_mock.assert_called_with(friendly_name='Call Tracking Demo')
        self.assertEqual(application, mock_application)

    def test_create_new_application(self):
        # Arrange
        mock_application = object()

        # Act
        with patch('os.environ.get', return_value=None):
            with patch('twilio.rest.resources.applications.Applications.list', return_value=[]):
                with patch('twilio.rest.resources.applications.Applications.create', return_value=mock_application) as twilio_mock:
                    application = get_twilio_application()

        # Assert
        self.assertTrue(twilio_mock.called)
        twilio_mock.assert_called_with(
            friendly_name='Call Tracking Demo',
            voice_url='http://www.example.com/call-tracking/forward-call')
        self.assertEqual(application, mock_application)

