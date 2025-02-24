from django.test import TestCase
from forms_app.simple_form.forms import SimpleForm


class SimpleFormTest(TestCase):
    def test_valid_form(self):
        valid_form_data = {
            "first_name": "FirstName",
            "last_name": "LastName",
        }

        form = SimpleForm(data=valid_form_data)
        self.assertTrue(form.is_valid(), msg=form.errors)

    def test_invalid_form(self):
        invalid_form_data = {"first_name": "firstName", "last_name": 5}
        form = SimpleForm(data=invalid_form_data)
        self.assertFalse(form.is_valid())
