from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Person
from .forms import SimpleForm


class PersonCreateView(CreateView):
    model = Person
    form_class = SimpleForm
    template_name = "simple_form.html"
    success_url = reverse_lazy("success")
    success_message = "Book successfully added!"


def generic_success(request):
    return render(request, "success.html")
