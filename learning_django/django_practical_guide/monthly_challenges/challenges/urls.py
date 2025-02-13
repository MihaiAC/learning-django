from django.urls import path, include
from . import views

# path(path, view function)
urlpatterns = [
    path("<int:month_nr>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="monthly-challenge"),
    path("", views.index, name="index"),
]