''' Database code for 
    author: Lai Man Tang(Nancy) 
    email: cloudtang030@gmail.com
'''

import psycopg2 

'''
create view articlesLog as 
select au.name as author, a.title, l.id as logID, l.status as logStatus
from log as l, articles as a, authors as au 
where l.path like concat('%/', a.slug) and au.id = a.author;

'''

def popular_articles(nums=3):
	""" return articles have been accessed the most. default return 3 articles."""
	db = psycopg2.connect(dbname='news')
	c = db.cursor()
	c.execute("select title ,count(title) as views from articlesLog group by title order by count(title) desc limit (%s);",(nums,))
	msg = c. fetchall()
	db.close()
	return msg

def popular_authors():
	""" return the pages views each authors have recieved."""
	db = psycopg2.connect(dbname='news')
	c = db.cursor()
	c.execute("select author ,count(author) as views from articlesLog group by author order by count(author) desc;")
	msg = c. fetchall()
	db.close()
	return msg

def request_error():
	""" return the pages views each authors have recieved."""
	db = psycopg2.connect(dbname='news')
	c = db.cursor()
	c.execute(" select date(time) as date, count(*) as total ,count(case when status like '4%' then 1 else null end) as error from log group by date(time) order by date(time);")
	msg = c. fetchall()
	db.close()
	return msg
