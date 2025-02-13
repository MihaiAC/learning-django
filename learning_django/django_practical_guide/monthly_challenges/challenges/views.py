from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.utils.dates import MONTHS
from django.urls import reverse

MONTH_LOWERCASE_NAMES = [x.lower() for x in MONTHS.values()]

def index(request: HttpRequest) -> HttpResponse:
    # response_data = ['<ul>']
    # for month in MONTHS.values():
    #     month_path = reverse("monthly-challenge", args=[month])
    #     response_data.append(f'\n<li><a href="{month_path}">{month}</a></li>')
    # response_data.append('</ul>')

    return render(request, "challenges/index.html", {
        'months': MONTH_LOWERCASE_NAMES
    })

def monthly_challenge_by_number(request: HttpRequest, month_nr: int) -> HttpResponse:
    if 1 <= month_nr <= 12:
        redirect_path = reverse("monthly-challenge", args=[MONTHS[month_nr]]) # Builds the prefix to the path
        return HttpResponseRedirect(redirect_path)
    raise Http404()

def monthly_challenge(request: HttpRequest, month: str) -> HttpResponse:
    if month in MONTH_LOWERCASE_NAMES:
        challenge_text = f"Placeholder challenge for {month}"

        # HTML template.
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    return Http404()
