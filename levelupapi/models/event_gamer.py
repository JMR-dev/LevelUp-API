from django.db import models
from levelupapi.models.gamer import Gamer
from levelupapi.models.events import Event
class Event_Gamer(models.Model):

    #Event won't change color for some reason. Reference this if something breaks later
    gamer= models.ForeignKey(Gamer)
    event = models.ForeignKey(Event)
    