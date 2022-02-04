from django.db import models
from levelupapi.models.gamer import Gamer
from models import Game


class Game(models.Model):

    game= models.ForeignKey(Game)
    description = models.CharField(max_length=256)
    date = models.DateField()
    time = models.TimeField(_(""), auto_now=False, auto_now_add=False)
    organizer = models.ForeignKey(Gamer)