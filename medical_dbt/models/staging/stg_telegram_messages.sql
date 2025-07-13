-- models/staging/stg_telegram_messages.sql

with source as (
    select
        id,
        data ->> 'message' as message,
        data ->> 'channel_id' as channel_id,
        (data ->> 'date')::timestamp as sent_at,
        length(data ->> 'message') as message_length,
        case when data ? 'photo' then true else false end as has_image
    from {{ source('raw', 'telegram_messages') }}
    where data ->> 'message' is not null
      and trim(data ->> 'message') <> ''
      and data ->> 'channel_id' is not null
)

select * from source

