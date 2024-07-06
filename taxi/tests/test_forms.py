from django.test import TestCase

from taxi.forms import DriverCreationForm, DriverLicenseUpdateForm


class FormTest(TestCase):
    def test_driver_creation_form_with_license_number(self):
        form_date = {
            "username": "TestDriver",
            "first_name": "TestFirst",
            "last_name": "TestLast",
            "password1": "Test123.",
            "password2": "Test123.",
            "license_number": "ABC12345",
        }
        form = DriverCreationForm(data=form_date)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_date)

    def test_driver_licence_update(self):
        form_data = {
            "license_number": "TES12345",
        }
        form = DriverLicenseUpdateForm(data=form_data)
        self.assertTrue(form.is_valid())
