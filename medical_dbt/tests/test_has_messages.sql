select *
from {{ ref('fct_messages') }}
where message is null or trim(message) = ''
