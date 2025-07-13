-- models/staging/stg_telegram_messages.sql

with source as (
    select *
    from {{ source('raw', 'telegram_messages') }}
),

flattened as (
    select
        (data->>'id')::bigint               as id,
        (data->>'message')                  as message,
        (data->>'channel_id')::bigint       as channel_id,
        (data->>'date')::timestamp          as sent_at,
        (data->>'photo')                    as photo
    from source
)

select
    id,
    message,
    channel_id,
    sent_at,
    length(message) as message_length,
    photo is not null as has_image
from flattened
