select
    id,
    channel_id::integer as channel_id,
    sent_at,
    message,
    message_length,
    has_image
from {{ ref('stg_telegram_messages') }}
