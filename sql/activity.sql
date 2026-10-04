-- one row per wallet per day
-- params: @start, @end, @addresses
SELECT from_address AS wallet,
       DATE(block_timestamp) AS day,
       COUNT(*) AS all_transactions,
       COUNTIF(receipt_status = 1 OR receipt_status IS NULL) AS successful_transactions
FROM `{ETHEREUM_DATASET}.transactions`
WHERE block_timestamp >= @start AND block_timestamp < @end
  AND to_address IN UNNEST(@addresses)
GROUP BY wallet, day
