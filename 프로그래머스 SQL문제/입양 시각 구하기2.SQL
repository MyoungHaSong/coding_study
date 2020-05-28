-- 코드를 입력하세요
set @time := -1;
SELECT (@time := @time+1) as HOUR, (select count(*) from animal_outs where HOUR(DATETIME) = @time) as COUNT
FROM ANIMAL_OUTS
WHERE @time < 23
