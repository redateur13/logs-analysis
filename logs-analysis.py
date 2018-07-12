#!/usr/bin/env python3
import psycopg2


# Questions
ques1 = "\n1.What are the most popular three articles of all time?"
ques2 = "\n2.Who are the most popular article authors of all time?"
ques3 = "\n3.On which days did more than 1% of requests lead to errors?"

# The most popular three articles of all time
query1 = """SELECT articles.title, COUNT(*) as num
            FROM articles, log
            WHERE log.path = CONCAT('/article/', articles.slug)
               AND log.status = '200 OK'
            GROUP BY articles.title
            ORDER BY num DESC
            LIMIT 3"""

# The most popular article authors of all time
query2 = """SELECT name, COUNT(*) as num
            FROM articles, authors, log
            WHERE log.path = CONCAT('/article/', articles.slug)
               AND authors.id = articles.author
            GROUP BY name
            ORDER BY num DESC"""

# On which days did more than 1% of requests lead to errors?
query3 = """SELECT *
            FROM ( SELECT TO_CHAR(time, 'FMMonth DD, YYYY') AS day,
                   ROUND( AVG((status != '200 OK')::int * 100), 2)
                   AS errors_rate FROM log
                   GROUP BY day )
                   AS errors_rate
            WHERE  errors_rate > 1"""


# Get results from database for top article and top authors
def top_articles_and_authors(question, query):
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    print(question)
    for result in results:
        article_or_author = result[0]
        view_num = result[1]
        print("*", article_or_author, "-", view_num, "views")


# Get results from database for days whth high errors rates
def days_with_high_errors_rates(question, query):
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    print(question)
    day = results[0][0]
    perc = str(results[0][1]) + "%"
    print("*", day, "-", perc, "errors\n")

# print query results
top_articles_and_authors(ques1, query1)
top_articles_and_authors(ques2, query2)
days_with_high_errors_rates(ques3, query3)
