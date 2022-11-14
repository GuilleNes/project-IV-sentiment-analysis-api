![](https://github.com/GuilleNes/project-IV-sentiment-analysis-api/blob/main/data/Portada.png)


 ## PROJECT IV SENTIMENT ANALYSIS API
***Guillermo Nespral***


**1. Introduction**

- **Goal of the Project**

> The main goal of this project is create our own API using MySQL to store our data allowing others to post new rows on it, querying to obtain the information we need and applying Sentiment Analysis over the diferent data that we have.


>In order to get and clean all the data, I have created a [main](https://github.com/GuilleNes/project-IV-sentiment-analysis-api/blob/main/main.ipynb) document, where the results of querying and post and several code [files](https://github.com/GuilleNes/project-IV-sentiment-analysis-api/tree/main/src) for the diferent functions for cleaning or connecting/querying to sql.


**1. Cleaning Process**

First of all, I started with a database from [kaggle](https://www.kaggle.com/) with more than 190.000 different tweets regarding the death of Elizabeth II.  The biggest challenge on the cleaning process was applying regex to delete the emojis, as they can not be uploaded to MySQL.



![](https://github.com/GuilleNes/project-IV-sentiment-analysis-api/blob/main/data/Regex.jpg)


**2. Sentiment Analysis**

Once I had the dataframe cleaned, added some columns for the sentiment analysis using some functions created for this.
![](https://github.com/GuilleNes/project-IV-sentiment-analysis-api/blob/main/data/Sentiment_analysis.jpg)

![Alt text](https://github.com/GuilleNes/project-IV-sentiment-analysis-api/blob/main/data/Sentiment_df.jpg)

**3. Upload to MySQL**

Once cleaned and with the new columns added, I used a query to upload it to SQL

![Alt text](https://github.com/GuilleNes/project-IV-sentiment-analysis-api/blob/main/data/Mysql_query.jpg)


**4. Querying MySQL and uploading to the API**

After creating the connection with MySQL and the API, I constructed the different query functions for the data analysis:

![Alt text](https://github.com/GuilleNes/project-IV-sentiment-analysis-api/blob/main/data/Querying_functions.jpg)

*****Despite I already did it before, I queried in the function below using the Sentiment Analysis on the function*****
![Alt text](https://github.com/GuilleNes/project-IV-sentiment-analysis-api/blob/main/data/API_functions.jpg)

I tried all the different functions using the web browser and checking the results.

**5. Making the request to the API from a Jupyter Notebook**

Once I had the connection with the API and the queries worked, I started to include them in the jupyter notebook:


![Alt text](https://github.com/GuilleNes/project-IV-sentiment-analysis-api/blob/main/data/Jupyter_query_1.jpg)


![Alt text](https://github.com/GuilleNes/project-IV-sentiment-analysis-api/blob/main/data/Jupyter_query_2.jpg)


![Alt text](https://github.com/GuilleNes/project-IV-sentiment-analysis-api/blob/main/data/Jupyter_query_3.jpg)


Using the average compound of the name query I could make a sentiment analysis of the tweets mentioning each member of the Royal Family. And here is the plot... 

![Alt text](https://github.com/GuilleNes/project-IV-sentiment-analysis-api/blob/main/data/Jupyter_query_5.jpg)


Finally, I post a new row in the df using the Post method:

![Alt text](https://github.com/GuilleNes/project-IV-sentiment-analysis-api/blob/main/data/Jupyter_query_4.jpg)


![](https://user-images.githubusercontent.com/112824189/201768507-33d4929b-f60d-4850-a4c1-96098ac0a8f8.gif)





  



