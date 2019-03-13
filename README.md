# Log Analysis

It is a simple python script that connect to a database and query specific data from some tables to generate a nice simple report.

Created by **Ahmed Kamel** for _**FSND**_.

## Installation
It require the following software to be up and runing on you OS ( Ubuntu on my case):
* Python3 and python3-psycopg2 packages.
* postgresql server.

## Database requirements:
* Full Stack Nano Degree provide you with the `.sql` file that contain our database, you can download it from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
* Create database called news `create database news;`
* Import the data into database from the file `psql -d news -f newsdata.sql`
* Create following SQL views is required in our code:

`create view top3 as
select replace((select replace(path,'/article/','') as t),'-',' ') as name, count(*) as num from log where path like '%article%' group by path order by num desc limit 3;`

`create view viewsum as
select replace((select replace(path,'/article/','') as t),'-',' ') as name, count(*) as num from log group by path order by num desc;`

`create view author_views as
select author , sum(num) as s from viewsum join articles on position(name in lower(title))>0 group by author order by s desc;`

`create view allviews as
select count(status) as all, time::date as d from log group by d;`

`create view fail as
select count(status) as failed, time::date as d from log where status != '200 OK' group by d order by d;`

## How to use :
From shell run: `python3 loganalysis.py`

#### Thanks
