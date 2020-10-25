from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from backend.utils import reservation_slug_generator

# Create your models here.


class Floor(models.Model):
    level = models.IntegerField()

    def __str__(self):
        return str(self.level)


class Room(models.Model):
    DESTINATION_CHOICES = [
        ('ASSEMBLY_HALL', 'Assembly Hall'),
        ('LECTURE', 'Lecture'),
        ('PRACTICALS', 'Practicals')
    ]
    floor = models.ForeignKey(Floor, on_delete=models.DO_NOTHING)
    sign = models.CharField(max_length=100)
    availability_level = models.PositiveIntegerField()
    projector = models.BooleanField()
    number_of_places = models.PositiveIntegerField()
    destination = models.CharField(max_length=20, choices=DESTINATION_CHOICES)

    def __str__(self):
        return self.sign


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
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)
    slug = models.SlugField(max_length=100, null=True, blank=True, default=None)
#   date_begin = models.DateTimeField()
#   date_end = models.DateTimeField()
    date = models.DateField()
    time = models.CharField(max_length=12, choices=TIME_CHOICES)
    is_upcoming = models.BooleanField()

    def __str__(self):
        return self.slug


class Message(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    content = models.CharField(max_length=1000)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[0:10]


pre_save.connect(reservation_slug_generator, sender=Reservation)
