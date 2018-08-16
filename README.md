Author: Lai Man Tang
github: https://github.com/littlecloud1
date: 2018-8-16

This project aims to analysis the 'news' database
and get the results of :
1.the most popular three articles of all time
2.the most popular article authors of all time
3.the day that has more than 1% of requests lead to errors

--------------------------------------------------------------
include two codes file: news-report.py, newsdb.py
and output file: newsreport.txt

news-report.py: the main function to call the database and output the result into newsreort file.

newsdb.py: it connects to the 'news' database and get the result from the queries.

newsreport.txt: it contains three result reports
--------------------------------------------------------------
Before running this project you have to create a view inside the datebase:

create view articlesLog as 
select au.name as author, a.title, l.id as logID, l.status as logStatus
from log as l, articles as a, authors as au 
where l.path like concat('%/', a.slug) and au.id = a.author;



To run this project:
python news-report.py