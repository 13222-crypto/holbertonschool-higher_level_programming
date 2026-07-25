# SQL - More Queries

This project covers advanced SQL concepts in MySQL 8.0 including user privilege management, primary/foreign key constraints, JOIN operations (INNER, LEFT, RIGHT), subqueries, aggregation functions, and UNIONs.

## Requirements

* **Environment:** Ubuntu 20.04 LTS
* **Database System:** MySQL 8.0 (version 8.0.25)
* **Syntax Rules:** All SQL keywords MUST be in UPPERCASE. Every query must be preceded by a comment.

## Tasks Summary

| Task | File | Description |
| --- | --- | --- |
| **0. My privileges!** | `0-privileges.sql` | Lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on localhost. |
| **1. Root user** | `1-create_user.sql` | Creates user_0d_1 with full privileges and password user_0d_1_pwd. |
| **2. Read user** | `2-create_read_user.sql` | Creates database hbtn_0d_2 and user_0d_2 with SELECT privilege only. |
| **3. Always a name** | `3-force_name.sql` | Creates the table force_name with non-null name attribute. |
| **4. ID can't be null** | `4-never_empty.sql` | Creates the table id_not_null with default value 1 for id. |
| **5. Unique ID** | `5-unique_id.sql` | Creates the table unique_id with unique id constraint and default value 1. |
| **6. States table** | `6-states.sql` | Creates database hbtn_0d_usa and table states with auto-increment primary key. |
| **7. Cities table** | `7-cities.sql` | Creates table cities with foreign key constraint referencing states table. |
| **8. Cities of California** | `8-cities_of_california_subquery.sql` | Lists all cities of California without using JOIN. |
| **9. Cities by States** | `9-cities_by_state_join.sql` | Lists all cities in database with state names using JOIN. |
| **10. Genre ID by show** | `10-genre_id_by_show.sql` | Lists all TV shows that have at least one genre linked. |
| **11. Genre ID for all shows** | `11-genre_id_all_shows.sql` | Lists all TV shows displaying NULL for shows without genres. |
| **12. No genre** | `12-no_genre.sql` | Lists all TV shows contained in hbtn_0d_tvshows without a genre linked. |
| **13. Number of shows by genre** | `13-count_shows_by_genre.sql` | Lists all genres and the number of shows linked to each. |
| **14. My genres** | `14-my_genres.sql` | Lists all genres of the show Dexter. |
| **15. Only Comedy** | `15-comedy_only.sql` | Lists all Comedy shows in the database hbtn_0d_tvshows. |
| **16. List shows and genres** | `16-shows_by_genre.sql` | Lists all shows and all genres linked to each show. |
| **17. Not my genre** | `100-not_my_genres.sql` | Lists all genres not linked to the show Dexter. |
| **18. No Comedy tonight!** | `101-not_a_comedy.sql` | Lists all shows without the genre Comedy. |
| **19. Rotten tomatoes** | `102-rating_shows.sql` | Lists all shows by their total sum of ratings. |
| **20. Best genre** | `103-rating_genres.sql` | Lists all genres by their total sum of ratings. |
