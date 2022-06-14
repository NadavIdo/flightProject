from django.shortcuts import render
from django.db import models

from flight.eli.models import Flights


# Create your models here.
def index(request):
    context = {
        'flights': Flights.objects.all()
    }
    return render(request, "index.html", context)


