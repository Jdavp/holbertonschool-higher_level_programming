-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genre.name AS genre, count(tv_show_genres.show_id) AS number_of_shows
       FROM tv_shows
       LEFT JOIN tv_show_genres
       	     ON tv_show_genres.show_id = tv_shows.id
	     ORDER BY tv_show_genres.show_id DESC;
