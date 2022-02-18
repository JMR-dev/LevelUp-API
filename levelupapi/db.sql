UPDATE levelupapi_game SET game_type_id = 3
WHERE title = 'World of Warcraft';

SELECT * FROM levelupapi_gamer
WHERE levelupapi_gamer.id = auth_user.id;

INSERT INTO levelupapi_event ('description', 'date', 'time', 'game_id', 'organizer_id')
VALUES 