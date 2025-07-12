with source as (
    select *
    from "telegram_medical"."public"."telegram_messages"
)

select
    id,
    data ->> 'message' as message,
    data ->> 'channel_id' as channel_id,
    (data ->> 'sent_at')::timestamp as sent_at,
    length(data ->> 'message') as message_length,
    case when data ? 'photo' then true else false end as has_image
from source