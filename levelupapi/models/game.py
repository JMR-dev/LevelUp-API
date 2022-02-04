from django.db import models
from levelupapi.models.game_type import Game_Type
from levelupapi.models.gamer import Gamer


class Game(models.Model):

    game_type = models.ForeignKey(Game_Type, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=256)
    maker = models.CharField(max_length=256)
    gamer = models.ForeignKey(Gamer, on_delete=models.DO_NOTHING)
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()