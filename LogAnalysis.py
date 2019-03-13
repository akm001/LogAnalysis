import psycopg2

conn = psycopg2.connect("dbname=news")

cr = conn.cursor()

# Q1 solution require 1 sql view (top3)
cr.execute("select title , num from top3 join articles "
           "on position(name in lower(title))>0 order by num desc ")

r = cr.fetchall()

print("The most popular three articles of all time:")

for x in r:
    print('"' + x[0] + '"' + ' -- ' + str(x[1]) + ' views')

print()
print("The most popular article authors of all time:")

# Q2 Solution require 2 sql views ( viewsum, author_views )
cr.execute("select name, s from authors join author_views "
           "on author = id order by s desc")

q2 = cr.fetchall()
for x in q2:
    print('"' + "%-22s" % x[0] + '"' + ' -- '+"%6s" % str(x[1]) + ' views')

print()
print("When more than 1% of requests lead to errors:")

# Q3 solution require 2 sql views (allviews, fail)
cr.execute("select allviews.d , "
           "(fail.failed::float / allviews.all::float) * 100 as perc"
           " from allviews join fail on allviews.d = fail.d "
           "where (fail.failed::float / allviews.all::float) * 100 > 1")
q3 = cr.fetchall()
for x in q3:
    print(x[0].strftime("%B %d, %Y") + ' -- ' + "%2.2f" % x[1] + '% errors')

conn.close()
