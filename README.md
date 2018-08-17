**Author**: Lai Man Tang

**Github**: https://github.com/littlecloud1

**Date**: 2018-8-16

## Project
This project aims to analysis the 'news' database
and get the results of :
  1. the most popular three articles of all time
  2. the most popular article authors of all time
  3. the day that has more than 1% of requests lead to errors


## Requirements
To Run this program, you have to install following softwares:

  * Python3
  * PostgreSQL
  * psycopg2


## Files
This project includes two codes file: **news-report.py, newsdb.py** 
and a output file: **newsreport.txt**

**news-report.py**: the main function to call the database and output the result into newsreort file.

**newsdb.py**: it connects to the 'news' database and get the result from the queries.

**newsreport.txt**: it is a example report that contains three analysis results 

Also, you need to download **newsdata.sql** and import it into database
[newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)


#### To import it into database:

psql -d news -f newsdata.sql


## How to Run
Before running this project you have to create a view inside the datebase:

CREATE VIEW articlesLog AS
SELECT au.name AS author,
       a.title,
       l.id AS logID,
       l.status AS logStatus
FROM log AS l,
      articles AS a,
      authors AS au
WHERE l.path LIKE CONCAT('%/', a.slug) 
      AND au.id = a.author;


#### To run this project:

python news-report.py
