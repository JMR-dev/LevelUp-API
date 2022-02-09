from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event, Game
from levelupapi.models.gamer import Gamer

class EventView(ViewSet):
    """Level up event types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single event type
        

        Returns:
            Response -- JSON serialized event type
        """
        try:
            game_type =  Event.objects.get(pk=pk)
            serializer =  EventSerializer(game_type)
            return Response(serializer.data)
        except  Event.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        

    def list(self, request):
        """Handle GET requests to get all event types

        Returns:
            Response -- JSON serialized list of event types
        """
        events = Event.objects.all()

# Add in the next 3 lines
        game = request.query_params.get('game_id', None)
        if game is not None:
            events = events.filter(game_id=game)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    # confused as to why I'm getting a 500 error on this. An article seems to indicate that I may need to nest more of my data inside another JSON object, if for example, it has foreign keys with additional data. https://stackoverflow.com/questions/60279456/django-postman-error-this-field-is-required
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        organizer = Gamer.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.data["game_id"])

        event = Event.objects.create(
            description=request.data["description"],
            date=request.data["date"],
            time=request.data["time"],
            game_id=game.id,
            organizer_id= organizer.id
        )
        serializer = EventSerializer(event)
        return Response(serializer.data)
    
class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for event types
    """
    class Meta:
        model = Event
        fields = ('id', 'description', 'date', 'time', 'game_id', 'organizer_id')
        depth = 2