from django.urls import path
from .views import generic_success
from .views import SimpleFormView

urlpatterns = [
    path("success/", generic_success, name="success"),
    path("simple-form/", SimpleFormView.as_view(), name="simple-form"),
]
