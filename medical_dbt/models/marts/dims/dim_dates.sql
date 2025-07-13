-- models/marts/dims/dim_dates.sql

with dates as (
    select distinct sent_at::date as date
    from {{ ref('stg_telegram_messages') }}
)

select
    date,
    extract(day from date)   as day,
    extract(week from date)  as week,
    extract(month from date) as month,
    extract(year from date)  as year,
    to_char(date, 'Day')     as weekday
from dates
