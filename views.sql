create view top3 as
select path, count(*) as num from log join articles
on position(articles.slug in log.path)>0
group by path order by num desc limit 3;

create view viewsum as
select path , count(*) as num from log
group by path order by num desc;

create view author_views as
select author , sum(num) as s from viewsum join articles
on position(slug in path)>0 group by author order by s desc;

create view allviews as
select count(status) as all, time::date as d from log group by d;

create view fail as
select count(status) as failed, time::date as d
from log where status != '200 OK' group by d order by d;
