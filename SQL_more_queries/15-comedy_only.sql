-- commment
SELECT tv_shows.title FROM tv_show_genres
LEFT JOIN tv_shows
    ON tv_shows.id = tv_show_genres.show_id 
LEFT JOIN tv_genres 
    ON tv_genres.id = tv_show_genres.genre_id
    WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title;