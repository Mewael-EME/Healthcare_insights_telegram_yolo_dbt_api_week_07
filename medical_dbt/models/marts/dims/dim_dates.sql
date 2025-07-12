select distinct
    sent_at::date as date,
    extract(year from sent_at) as year,
    extract(month from sent_at) as month,
    extract(day from sent_at) as day,
    extract(dow from sent_at) as weekday
from {{ ref('stg_telegram_messages') }}
