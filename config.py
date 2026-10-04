PROJECT_ID = "project-984bff5f-3deb-47ef-973"
ETHEREUM_DATASET = "bigquery-public-data.crypto_ethereum"

WINDOW_DAYS = 30        # days after launch
MAX_GB_PER_QUERY = 30   # cost limit per query
OUTPUT_DIR = "data"

# dapp_id, category, contract addresses (check on Etherscan)
PILOT_DAPPS = [
    ("uniswap_v2", "DEX",     ["0xf164fC0Ec4E93095b804a4795bBe1e041497b92a",    # Router01
                               "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"]),  # Router02
    ("aave_v2",    "Lending", ["0x7d2768dE32b0b80b7a3454c06BdAc94A69DDc7A9"]),
]
