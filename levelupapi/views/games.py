from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game

class GameView(ViewSet):
    """Level up game s view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game 
        

        Returns:
            Response -- JSON serialized game 
        """
        

# Add in the next 3 lines
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game)
            return Response(serializer.data)
        except Game.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        

    def list(self, request):
        """Handle GET requests to get all game s

        Returns:
            Response -- JSON serialized list of game s
        """
        game_ = request.query_params.get('type', None)
        games = Game.objects.all()
        if game_ is not None:
                games = games.filter(game_type_id=game_)
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
    
class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for game s
    """
    class Meta:
        model = Game
        fields = ('id', 'title', 'maker', 'number_of_players', 'skill_level', 'game_type_id', 'gamer_id')
        depth = 1