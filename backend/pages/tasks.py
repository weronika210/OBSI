from pages.models import Reservation
import threading
from datetime import datetime


def update_reservation_status():
    res = Reservation.objects.all().filter(is_upcoming=True)
    for reservation in res:
        if reservation.datetime_begin < datetime.now():
            reservation.is_upcoming = False
            reservation.save()
    threading.Timer(60, update_reservation_status).start()
