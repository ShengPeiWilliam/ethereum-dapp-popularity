# Daily active wallets
import pandas as pd
from config import WINDOW_DAYS


def keep_successful(activity):
    return activity[activity.successful_transactions > 0]


def count_daily_active_wallets(successful_activity):
    return (successful_activity.groupby("day_index").wallet.nunique()
            .reindex(range(WINDOW_DAYS), fill_value=0))


def build_daily_table(activity):
    return pd.DataFrame({
        dapp_id: count_daily_active_wallets(keep_successful(dapp_activity))
        for dapp_id, dapp_activity in activity.groupby("dapp_id")})
