{{ config(materialized='view') }}

SELECT
    CAST(id.message_id AS INTEGER) AS message_id,
    id.detected_object_class,
    id.confidence_score
FROM {{ source('raw', 'image_detections') }} AS id
JOIN {{ ref('fct_messages') }} AS fm
  ON CAST(id.message_id AS INTEGER) = fm.id
