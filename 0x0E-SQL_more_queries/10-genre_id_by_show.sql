-- List all shows that have at least one genre linked
SELECT ts.title AS title, tsg.genre_id as genre_id
FROM tv_shows AS ts
JOIN tv_show_genres AS tsg
ON ts.id = tsg.show_id
ORDER BY title;
