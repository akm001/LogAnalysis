#!/usr/bin/python3
import psycopg2


def db_connect():
    """
    Create and return a database connection and cursor.

    The functions creates and returns a database connection and cursor to the
    database defined by DBNAME.
    Returns:
        db, c - a tuple. The first element is a connection to the database.
                The second element is a cursor for the database.
    """
    # Your code here
    db = psycopg2.connect("dbname=news")

    c = db.cursor()

    return db, c


def execute_query(query):
    """
    execute_query returns the results of an SQL query.

    execute_query takes an SQL query as a parameter,
    executes the query and returns the results as a list of tuples.
    args:
    query - an SQL query statement to be executed.

    returns:
    A list of tuples containing the results of the query.
    """
    # Your code here
    c.execute(query)
    r = c.fetchall()
    return r


def print_top_articles():
    """Print out the top 3 articles of all time."""
    query = """
            select title , num from top3 join articles
            on position(slug in path)>0 order by num desc;
            """
    results = execute_query(query)

    # add code to print results
    print("The most popular three articles of all time:")

    for x in results:
        print(f'\"  {x[0]}  \" -- {str(x[1])} views')

    print()


def print_top_authors():
    """Print a list of authors ranked by article views."""
    query = """
            select name, s from authors join author_views
            on author = id order by s desc;
            """
    results = execute_query(query)

    # add code to print results
    print("The most popular article authors of all time:")
    for x in results:
        print(f'\"{x[0]:22s} \" -- {str(x[1]):>6s} views')

    print()


def print_errors_over_one():
    """Print out the error report.

    This function prints out the days and that day's error percentage where
    more than 1% of logged access requests were errors.
    """
    query = """
            select allviews.d ,
            (fail.failed::float / allviews.all::float) * 100 as perc
             from allviews join fail on allviews.d = fail.d
            where (fail.failed::float / allviews.all::float) * 100 > 1;
            """
    results = execute_query(query)

    # add code to print results
    print("When more than 1% of requests lead to errors:")
    for x in results:
        print(f'{x[0]:%B %d, %Y} -- {x[1]:.2f}% errors')
    print()


if __name__ == '__main__':
    db, c = db_connect()
    print_top_articles()
    print_top_authors()
    print_errors_over_one()
    db.close()
