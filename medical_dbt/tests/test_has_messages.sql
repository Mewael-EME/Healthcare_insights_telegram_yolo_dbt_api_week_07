SELECT * FROM {{ ref('fct_messages') }} WHERE message IS NULL;
