-- SELECT * FROM subscriptions
-- LIMIT 4;

-- SELECT MIN(subscription_start) as min_start, 
--        MAX(subscription_end) as max_end 
-- FROM subscriptions;

-- WITH months AS 
-- (SELECT '2017-01-01' AS 'first_day',
--     '2017-01-31' AS 'last_day'
--   UNION
--   SELECT '2017-02-01' AS 'first_day',
--     '2017-02-28' AS 'last_day'
--   UNION
--   SELECT '2017-03-01' AS 'first_day',
--     '2017-03-31' AS 'last_day'
-- ),
-- cross_join AS 
-- (SELECT * 
--  FROM subscriptions 
--  CROSS JOIN months
-- ),
-- status AS 
-- (SELECT id, first_day as month,
--    CASE 
--      WHEN segment = 30 
--        AND subscription_start < first_day 
--        AND (subscription_end > first_day OR subscription_end IS NULL) THEN 1
--      ELSE 0
--    END as is_active_30, 
--    CASE
--      WHEN segment = 87 
--        AND subscription_start < first_day 
--        AND (subscription_end > first_day OR subscription_end IS NULL) THEN 1
--      ELSE 0
--    END as is_active_87,
--    CASE
--      WHEN segment = 30
--        AND (subscription_end BETWEEN first_day AND last_day)
--      THEN 1
--      ELSE 0
--    END as is_canceled_30,
--    CASE
--      WHEN segment = 87 
--        AND (subscription_end BETWEEN first_day AND last_day)
--      THEN 1
--      ELSE 0
--    END as is_canceled_87
--  FROM cross_join
-- ),
-- status_aggregate AS 
-- (SELECT month, 
--    SUM(is_active_30) as sum_active_30,    
--    SUM(is_canceled_30) as sum_canceled_30,
--    SUM(is_active_87) as sum_active_87,  
--    SUM(is_canceled_87) as sum_canceled_87
--  FROM status
--  GROUP BY month
-- )
-- SELECT month, 
--   ROUND(1.0 * sum_canceled_30 / sum_active_30, 4) as churn_30, 
--   ROUND(1.0 * sum_canceled_87 / sum_active_87, 4) as churn_87 
-- FROM status_aggregate;

-- BONUS (actually shorter)
WITH months AS 
(SELECT '2017-01-01' AS 'first_day',
    '2017-01-31' AS 'last_day'
  UNION
  SELECT '2017-02-01' AS 'first_day',
    '2017-02-28' AS 'last_day'
  UNION
  SELECT '2017-03-01' AS 'first_day',
    '2017-03-31' AS 'last_day'
),
cross_join AS 
(SELECT * 
 FROM subscriptions 
 CROSS JOIN months
),
status AS 
(SELECT first_day as month,
   segment,
   CASE
    WHEN subscription_start < first_day 
      AND (subscription_end > first_day OR subscription_end IS NULL) THEN 1
     ELSE 0
   END as is_active, 
   CASE
       WHEN subscription_end BETWEEN first_day AND last_day THEN 1
       ELSE 0
     END as is_canceled
 FROM cross_join
),
status_aggregate AS 
(SELECT month, segment, 
   SUM(is_active) as total_active,
   SUM(is_canceled) as total_canceled
 FROM status
 GROUP BY segment, month
)
SELECT month, segment, 
  ROUND(1.0 * total_canceled / total_active, 4) as churn 
FROM status_aggregate;