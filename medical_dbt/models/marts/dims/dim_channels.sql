-- models/marts/dims/dim_channels.sql

select
    channel_id,
    min(sent_at) as first_message_time,
    max(sent_at) as last_message_time,
    count(*)     as total_messages
from {{ ref('stg_telegram_messages') }}
group by channel_id
