from django.forms import ModelForm
from .models import Person
from django.forms import ValidationError


class SimpleForm(ModelForm):
    class Meta:
        model = Person
        fields = ["first_name", "last_name"]

    def clean_last_name(self):
        """
        Checks that last_name is not empty and only contains letters.
        """
        last_name = self.cleaned_data.get("last_name")

        if last_name is None or last_name == "":
            raise ValidationError("Last name must not be empty")
        else:
            for letter in last_name:
                if not letter.isalpha():
                    raise ValidationError("Last names should only contain letters")
        return last_name
