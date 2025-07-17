-- commment
SELECT tv_genres.name, COUNT(genre_id)
FROM tv_show_genres
LEFT JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id;