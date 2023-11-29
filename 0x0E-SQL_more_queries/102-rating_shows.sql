-- List all shows from the hbtn_0d_tvshows_rate database by their rating sum.
-- Each record displays: tv_shows.title - rating sum.
-- Results are sorted in descending order by the rating sum.

SELECT tv_shows.title, SUM(tv_show_ratings.rating) AS rating_sum
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
