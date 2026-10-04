-- params: @addresses
SELECT address AS contract_address, MIN(block_timestamp) AS deployed_at
FROM `{ETHEREUM_DATASET}.contracts`
WHERE address IN UNNEST(@addresses)
GROUP BY address
