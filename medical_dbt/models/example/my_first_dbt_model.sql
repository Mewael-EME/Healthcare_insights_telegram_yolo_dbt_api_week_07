select 1 as id
union all
select null as id
where false  -- effectively removes the null row
