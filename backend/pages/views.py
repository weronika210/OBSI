from django.shortcuts import render
from pages.tasks import update_reservation_status

# Create your views here.


def home(request):
    update_reservation_status()
    return render(request, 'pages/index.html')
