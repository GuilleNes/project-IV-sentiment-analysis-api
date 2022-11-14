USE project_4;
	LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/queen_cleaned.csv'
		INTO TABLE queen
			FIELDS TERMINATED BY ','
			OPTIONALLY ENCLOSED BY '"'
			LINES TERMINATED BY '\r\n'
			IGNORE 1 ROWS;
SELECT *
FROM project_4;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/queen_sentiment.csv'
	INTO TABLE queen_sentiment
		FIELDS TERMINATED BY ','
        OPTIONALLY ENCLOSED BY '"'
        LINES TERMINATED BY '\r\n'
        IGNORE 1 ROWS;
        
SELECT * 
    FROM queen_sentiment
    WHERE neu > 0.900;
    
SELECT ROUND(AVG(compound), 3) FROM queen_sentiment
	WHERE tweet LIKE '%Harry%';
    
SELECT * FROM queen_sentiment;

SELECT tweet, name, replies_count FROM queen_sentiment
	order by replies_count DESC
    limit 5;
    
SELECT tweet, pos, username 
    FROM queen_sentiment
    WHERE pos >=  0.900
    AND pos < 1
    ORDER BY pos DESC;
    
SELECT tweet, replies_count FROM queen_sentiment
	ORDER BY replies_count DESC
    LIMIT 10;

SELECT * FROM queen_sentiment
	ORDER BY id ASC
    LIMIT 1;
