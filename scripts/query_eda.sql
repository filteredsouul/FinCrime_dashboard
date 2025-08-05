WITH base AS (
	SELECT 
		t.ID as transaction_id,
		t.USER_ID as user_id,
		t.CREATED_DATE as created_date,
		DATE(t.CREATED_DATE) AS day_date,
		DATE(DATE(t.CREATED_DATE), '-' || ((CAST(STRFTIME('%w', DATE(t.CREATED_DATE)) AS INTEGER) + 6) % 7) || ' days') AS week_date,
		STRFTIME('%Y-W%W', DATE(t.CREATED_DATE)) AS iso_week,
		t.TYPE as transaction_type,
		t.STATE as state,
		t.AMOUNT_GBP as amnt_gbp,
		u.COUNTRY as country,
		CASE WHEN f.USER_ID IS NOT NULL THEN 1 ELSE 0 END AS is_fraudster	
	FROM transactions t 
	JOIN users u ON t.USER_ID = u.ID
	LEFT JOIN fraudsters f ON t.USER_ID = f.USER_ID 
),

base_2 AS (
	SELECT
		iso_week,
		week_date,
		day_date,
		country,
		transaction_type,
		COUNT(DISTINCT user_id) AS nb_users,
		COUNT(DISTINCT CASE WHEN is_fraudster = 1 THEN user_id END) AS nb_fraudsters,
		COUNT(transaction_id) AS nb_transaction,
		COUNT(CASE WHEN is_fraudster = 1 THEN transaction_id END) AS nb_transaction_fraud,
		ROUND(SUM(CASE WHEN is_fraudster = 1 THEN amnt_gbp ELSE 0 END), 2) AS total_amount_fraud,
		ROUND(SUM(amnt_gbp), 2) AS total_amount_transactions,

		-- Nouveaux indicateurs d’état
		ROUND(100.0 * COUNT(CASE WHEN state = 'completed' THEN 1 END) / COUNT(transaction_id), 2) AS pct_completed,
		ROUND(100.0 * COUNT(CASE WHEN state = 'failed' THEN 1 END) / COUNT(transaction_id), 2) AS pct_failed,
		ROUND(100.0 * COUNT(CASE WHEN state = 'cancelled' THEN 1 END) / COUNT(transaction_id), 2) AS pct_cancelled,
		ROUND(100.0 * COUNT(CASE WHEN state = 'refunded' THEN 1 END) / COUNT(transaction_id), 2) AS pct_refunded
	FROM base
	GROUP BY iso_week, week_date, country, transaction_type
) 
SELECT * 
FROM base_2
ORDER BY iso_week DESC, country, transaction_type;