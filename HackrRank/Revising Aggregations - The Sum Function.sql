select sum(population)
from city
group by DISTRICT
having district = 'California'