from src.load_dapps import load_dapps
from src.pull_activity import pull_all_activity
from src.compute_features import build_feature_table
from src.daily_active_wallets import build_daily_table
from src.save_results import save_results


def main():
    dapps = load_dapps()                               # 1. DApp list and day 0
    activity = pull_all_activity(dapps)                # 2. one row per wallet per day
    features = build_feature_table(dapps, activity)    # 3. one row per DApp
    daily_table = build_daily_table(activity)          # 4. daily active wallets
    save_results(features, daily_table)                # 5. write CSV files
    print(features.T.to_string())


if __name__ == "__main__":
    main()
