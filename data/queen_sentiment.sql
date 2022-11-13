USE project_4;
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/queen_cleaned.csv'
	INTO TABLE queen
		FIELDS TERMINATED BY ','
        OPTIONALLY ENCLOSED BY '"'
        LINES TERMINATED BY '\r\n'
        IGNORE 1 ROWS;
SELECT *
FROM queen;

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

    