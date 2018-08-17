#!/usr/bin/env python3
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
    """ return articles have been accessed the most.
    default return 3 articles."""
    db = psycopg2.connect(dbname='news')
    c = db.cursor()
    c.execute("""
        SELECT title,
               count(title) AS views
        FROM articlesLog
        GROUP BY title
        ORDER BY count(title) DESC
        LIMIT (%s);
        """, (nums,))
    msg = c. fetchall()
    db.close()
    return msg


def popular_authors():
    """ return the pages views each authors have recieved."""
    db = psycopg2.connect(dbname='news')
    c = db.cursor()
    c.execute('''
        SELECT author,
               count(author) AS views
        FROM articlesLog
        GROUP BY author
        ORDER BY count(author) desc;
        ''')
    msg = c. fetchall()
    db.close()
    return msg


def request_error():
    """ return the pages views each authors have recieved."""
    db = psycopg2.connect(dbname='news')
    c = db.cursor()
    c.execute("""
        SELECT  date(TIME) AS date,
                count(*) AS total,
                count(CASE
                         WHEN status LIKE '4%' THEN 1
                         ELSE NULL
                      END)::float AS error
        FROM log
        GROUP BY date(TIME)
        ORDER BY date(TIME);
        """)
    msg = c. fetchall()
    db.close()
    return msg
