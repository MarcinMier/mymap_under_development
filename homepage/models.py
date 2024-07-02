from django.db import models

# Create your models here.
from django.db import models


class Route(models.Model):
    route_id = models.IntegerField(default=0) # jak nadać automatycznie nowe id?
    route_name = models.CharField(max_length=200)
    route_length = models.IntegerField(default=0) # tu wstawic funkcje do obliczania dlugosci drogi
    # do uzupelnienia jak dojda kolejne modele
    # route_start =
    # route_finish =
    # stops =
    def __str__(self):
        return self.route_name

class User(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=200)
    password = models.IntegerField(default=0)
    route = models.ForeignKey(Route, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user_name

