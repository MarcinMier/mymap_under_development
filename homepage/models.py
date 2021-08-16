from django.db import models
from django.contrib.auth.models import User
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
    # tutaj dodaje klucz obcy do Użytkownika. Każda trasa jest przypisana do jakiegoś
    # użytkownika.
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.route_name

# Zakomentowałem model Usera, bo do logowania używasz model Usera wbudowany
# w Django (model User z modułu django.contrib.auth.models)
# class User(models.Model):
#     user_id = models.IntegerField()
#     user_name = models.CharField(max_length=200)
#     password = models.IntegerField(default=0)
#     # route = models.ForeignKey(Route, on_delete=models.DO_NOTHING)
#
#     def __str__(self):
#         return self.user_name
#
