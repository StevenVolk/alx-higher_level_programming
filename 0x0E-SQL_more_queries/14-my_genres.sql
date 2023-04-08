-- a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tv_genres.name
FROM tv_genres, tv_shows, tv_show_genres
WHERE tv_shows.title = 'DEXTER' AND tv_shows.id = tv_show_genres.show_id AND tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_genres.name ASC;
