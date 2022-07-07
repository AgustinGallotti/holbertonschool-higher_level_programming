-- sql
SELECT tv_shows.title, tv_show_genres.genre_id
RIGHT JOIN tv_shows_display ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
