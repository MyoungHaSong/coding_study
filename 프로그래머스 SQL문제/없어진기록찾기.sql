-- �ڵ带 �Է��ϼ���
SELECT a.ANIMAL_ID, a.name
from animal_outs as a left join animal_ins as b 
on a.ANIMAL_ID= b.ANIMAL_ID
where b.animal_id is null
order by a.animal_id

