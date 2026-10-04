# Write results to OUTPUT_DIR
import os
from config import OUTPUT_DIR


def save_results(features, daily_table):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    features.to_csv(f"{OUTPUT_DIR}/pilot_features.csv", index=False)
    daily_table.to_csv(f"{OUTPUT_DIR}/pilot_daily_active_wallets.csv", index_label="day_index")
