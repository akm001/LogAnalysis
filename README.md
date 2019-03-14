# Log Analysis
It is python script uses psycopg2 to query a mock PostgreSQL database for a fictional news website and generate a report.
The database consist of three tables (authors which contains authors' name and info,
articles which contains articles info like title,slug,author,.. ,
log which is web server logs data ),
The report will answer the following questions:

* The most popular three articles of all time ?
* The most popular article authors of all time ?
* When more than 1% of requests lead to errors ?

## Installation
It require the following software to be up and running on you OS ( Ubuntu on my case):
* Python3 and python3-psycopg2 packages: `apt nstall python3 python3-psycopg2`
* postgresql server: `apt install postgresql`

## Database preparation:
* Create database called **news** `create database news;`
* FSND provides you with the `.sql` file that contain our database, you can download it from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip),
import it: `psql -d news -f newsdata.sql`
* Import the SQL views which is required in our code: `psql -d news -f views.sql`

## How to use :
From shell or cmd run: `python3 LogAnalysis.py`
Or make sure you have execute permission on the script: `chmod u+x LogAnalysis.py`
then run `./LogAnalysis.py`

#### Thanks
Created by **Ahmed Kamel** for _**FSND**_.
