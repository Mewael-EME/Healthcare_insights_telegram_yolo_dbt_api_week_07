-- models/tests/no_empty_messages.sql
select *
from {{ ref('stg_telegram_messages') }}
where message is null or trim(message) = ''
