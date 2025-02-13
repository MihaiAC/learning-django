from django import forms

from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=100, error_messages= {
#         "max_length": "Please enter a shorter name.",
#         "required": "Your name should not be empty"
#     })

#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=250)
#     rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        # Model you want a form for.
        model = Review

        # Model fields that will be part of the form.
        # fields = ['user_name', 'review_text', 'rating']
        fields = '__all__'

        labels = {
            "user_name": "Your Name",
            "review_text": "Your feedback",
            "rating": "Your rating"
        }

        error_messages = {
            "user_name": {
                "required": "Your name must not me empty",
                "max_length": "Max char limit exceeded"
            }
        }