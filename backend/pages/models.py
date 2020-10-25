from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Floor(models.Model):
    level = models.IntegerField()


class Room(models.Model):
    DESTINATION_CHOICES = [
        ('ASSEMBLY_HALL', 'Assembly Hall'),
        ('LECTURE', 'Lecture'),
        ('PRACTICALS', 'Practicals')
    ]
    floor = models.ForeignKey(Floor, on_delete=models.DO_NOTHING)
    sign = models.CharField(max_length=100)
    projector = models.BooleanField()
    places = models.IntegerField()
    destination = models.CharField(max_length=20, choices=DESTINATION_CHOICES)


class Reservation(models.Model):
    TIME_CHOICES = [
        ('1', '8:00-10:00'),
        ('2', '10:00-12:00'),
        ('3', '12:00-14:00'),
        ('4', '14:00-16:00'),
        ('5', '16:00-18:00'),
        ('6', '18:00-20:00')
    ]
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#   date_begin = models.DateTimeField()
#   date_end = models.DateTimeField()
    date = models.DateField()
    time = models.CharField(max_length=12, choices=TIME_CHOICES)


class Message(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    content = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
