from django.urls import path
from .views import generic_success
from .views import PersonCreateView

urlpatterns = [
    path("success/", generic_success, name="success"),
    path("person-create-form/", PersonCreateView.as_view(), name="person_create"),
]
