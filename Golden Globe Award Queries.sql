-- I created this project to track the number of times a certain actor, director, or film has won/been nominated for 
-- the Golden Globes in the past year (2019-2020). I collected the dataset from Kaggle and created tables and 
-- forward engineered the dataset to be able to write and execute queries to answer questions about the dataset.

-- Who were the nominees for Best Director -  Motion Picture and how many people were nominated?
USE golden_globes;
CREATE OR REPLACE VIEW directors AS
SELECT nominee_name AS 'Director', category_name AS 'Category'
FROM nominees n
JOIN nominees_for_category nc 
ON n.nominee_id = nc.nfc_nominee_id

JOIN categories c
ON c.category_id = nc.nfc_category_id

WHERE category_name = "Best Director - Motion Picture"

UNION 
SELECT "Total Number of Nominees", COUNT(nominee_name)
FROM nominees n
JOIN nominees_for_category nc 
ON n.nominee_id = nc.nfc_nominee_id

JOIN categories c
ON c.category_id = nc.nfc_category_id

WHERE category_name = "Best Director - Motion Picture";

-- Who won a golden globe in 2020 and had previously won one before
USE golden_globes;

CREATE OR REPLACE VIEW previous_winners AS

SELECT nominee_name AS 'Nominee'
FROM nominees JOIN golden_globes_results 
	USING (nominee_id)
WHERE previous_win = 1 AND win = 1
ORDER BY nominee_name; 

-- What category had the most nominees
USE golden_globes;

CREATE OR REPLACE VIEW most_nominated AS

SELECT nominee_name AS 'Nominee', category_name AS 'Category', win
FROM nominees JOIN nominees_for_category
	ON nominee_id =  nfc_nominee_id
    JOIN categories 
    ON category_id = nfc_category_id
    JOIN golden_globes_results
    USING(category_id)
WHERE win = 1
ORDER BY nominee_name;

-- What film won in multiple categories
CREATE OR REPLACE VIEW multiple_categories AS

SELECT f.film_name AS 'Winning Film', c.category_name AS 'Winning Category', n.nominee_name AS 'Winner', f.film_rating AS 'Film Rating'

FROM nominees_for_category JOIN nominees n
	ON nfc_nominee_id = nominee_id
    JOIN categories c ON nfc_category_id = category_id
	JOIN golden_globes_results gg USING(nominee_id)
    JOIN films f USING(film_id)
    JOIN (SELECT SUM(win) AS total_wins, film_id,film_name
			FROM golden_globes_results JOIN films
			USING(film_id)
			GROUP BY film_id) t1
		USING(film_id)
    
WHERE total_wins > 1 AND win = 1;

-- Which film that has a rating above 5.0 stars and has made a gross over $1 million
USE golden_globes;

CREATE OR REPLACE VIEW film_view AS


SELECT film_name AS 'Film', film_rating AS 'Rating', CONCAT('$',(film_gross)) AS 'Film Gross'
FROM films

WHERE film_rating > 5.0 AND film_gross > 1000000;

-- What is the average rating for films that won a golden globe
USE golden_globes;

CREATE OR REPLACE VIEW average_rating AS
SELECT film_name AS 'Film', FORMAT(AVG(film_rating),2) AS 'Rating'
FROM films join golden_globes_results
	USING(film_id)
GROUP BY film_name, win
HAVING win = 1;

-- Who was nominated for golden globes and never won
USE golden_globes;
CREATE OR REPLACE VIEW no_wins AS
SELECT nominee_name AS 'Nominee', previous_win, category_name AS 'Category' 
FROM nominees 
JOIN nominees_for_category 
      ON nominees.nominee_id = nominees_for_category.nfc_nominee_id
      
JOIN categories 
     ON categories.category_id = nominees_for_category.nfc_category_id
WHERE previous_win= 0; 

-- Which film's gross made more than average
CREATE OR REPLACE VIEW average_film_gross AS
SELECT film_name AS 'Film', CONCAT('$', film_gross) AS 'Film Gross'
FROM films
WHERE film_gross >
(SELECT AVG(avg_across) FROM 
(SELECT film_name, AVG(film_gross) AS avg_across
FROM films WHERE 
film_gross IS NOT NULL
GROUP BY  film_name) a)
ORDER BY film_gross DESC;


