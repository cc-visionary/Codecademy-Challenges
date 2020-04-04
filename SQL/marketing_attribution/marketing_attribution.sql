SELECT DISTINCT utm_campaign FROM page_visits;
SELECT DISTINCT utm_source FROM page_visits;

SELECT utm_campaign, utm_source FROM page_visits
GROUP BY utm_source, utm_campaign;

SELECT DISTINCT page_name FROM page_visits;
WITH first_touch AS (
  SELECT *, MIN(timestamp) as first_touch_at
  FROM page_visits
  GROUP BY user_id
)
SELECT utm_campaign, 
  COUNT(user_id) as num_first_touch
FROM first_touch
GROUP BY utm_campaign;

WITH last_touch AS (
  SELECT *, MAX(timestamp) as last_touch_at
  FROM page_visits
  GROUP BY user_id
)
SELECT utm_campaign, COUNT(user_id) as num_last_touch FROM last_touch
GROUP BY utm_campaign;

SELECT COUNT(*) as num_purchase FROM page_visits
WHERE page_name ='4 - purchase';

WITH last_touch AS (
  SELECT *, MAX(timestamp) as last_touch_at
  FROM page_visits
  GROUP BY user_id
)
SELECT utm_campaign, COUNT(user_id) as num_last_touch FROM last_touch
WHERE page_name = '4 - purchase'
GROUP BY utm_campaign;