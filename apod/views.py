import requests
from django.shortcuts import render
from django.conf import settings
from django.utils.dateparse import parse_date
from .models import Apod
from datetime import date, timedelta

# Create your views here.
def get_apod_data(date=None):
    api_key = settings.NASA_API_KEY
    base_url = "https://api.nasa.gov/planetary/apod"

    params = {
        "api_key": api_key,
    }
    if date:
        params["date"] = date

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        apod, created = Apod.objects.get_or_create(
            date=parse_date(data['date']),
            defaults={
                'title': data['title'],
                'explanation': data['explanation'],
                'url': data['url'],
                'media_type': data['media_type'],
            }
        )
        return apod
    return None

def home(request):
    apod = get_apod_data()
    return render(request, 'apod/home.html', {'apod': apod})

def timeline(request):
    end_date = date.today()
    start_date = end_date - timedelta(days=30)
    apods = Apod.objects.filter(date__range=[start_date, end_date]).order_by('-date')
    return render(request, 'apod/timeline.html', {'apods': apods})
