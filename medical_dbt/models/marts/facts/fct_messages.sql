-- models/marts/facts/fct_messages.sql

select
    m.id,
    m.channel_id,
    c.total_messages,
    d.date,
    m.sent_at,
    m.message,
    m.message_length,
    m.has_image
from {{ ref('stg_telegram_messages') }} m
left join {{ ref('dim_channels') }} c
    on m.channel_id = c.channel_id
left join {{ ref('dim_dates') }} d
    on m.sent_at::date = d.date

