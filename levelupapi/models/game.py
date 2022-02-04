from django.db import models
from models import Gamer


class Game(models.Model):

    game_type = models.ForeignKey(game_type)
    title = models.CharField(max_length=256)
    maker = models.CharField(max_length=256)
    gamer = models.ForeignKey(Gamer)
    number_of_players = models.IntegerField(max_value = 1, max_value = 128)
    skill_level = models.IntegerField(max_value = 1, max_value = 100)