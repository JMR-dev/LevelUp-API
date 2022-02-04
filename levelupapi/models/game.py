from django.db import models
from django.contrib.auth.models import User
from django.db import models
from models import Gamer
from models import Game_Type


class Game(models.Model):

    game_type = models.ForeignKey(Game_Type)
    title = models.CharField(max_length=256)
    maker = models.CharField(max_length=256)
    gamer = models.ForeignKey(Gamer)
    number_of_players = models.IntegerField(max_value = 1, max_value = 128)
    skill_level = models.IntegerField(max_value = 1, max_value = 100)