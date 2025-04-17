from django.urls import reverse
from django.test import TestCase
from forms_app.simple_form.forms import SimpleForm


class SimpleFormTest(TestCase):
    @staticmethod
    def get_valid_form_data():
        return {
            "first_name": "FirstName",
            "last_name": "LastName",
        }

    def test_valid_form(self):
        valid_form_data = SimpleFormTest.get_valid_form_data()
        form = SimpleForm(data=valid_form_data)
        self.assertTrue(form.is_valid(), msg=form.errors)

    def test_invalid_form(self):
        invalid_form_data = {"first_name": "firstName", "last_name": 5}
        form = SimpleForm(data=invalid_form_data)
        self.assertFalse(form.is_valid())

    def test_template_contents(self):
        # form = SimpleForm()
        response = self.client.get(reverse("simple-form"))
        self.assertContains(response, "<form")
        self.assertContains(response, 'name="csrfmiddlewaretoken"')
        # self.assertContains(response, form.as_p())

    def test_successful_form_submission(self):
        valid_form_data = SimpleFormTest.get_valid_form_data()
        response = self.client.post(reverse("simple-form"), valid_form_data)

        # Test that the page redirects on success.
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("success"))
        response = self.client.get(reverse("success"))
        self.assertContains(response, "Success!")
