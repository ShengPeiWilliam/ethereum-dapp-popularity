# Feature definitions, computed from the activity of one DApp
import numpy as np
import pandas as pd
from config import WINDOW_DAYS
from src.daily_active_wallets import keep_successful, count_daily_active_wallets


def how_many_came(successful_activity):
    wallet_count = successful_activity.wallet.nunique()
    return {
        "active_wallets_total": wallet_count,
        "tx_per_wallet": successful_activity.successful_transactions.sum() / wallet_count,
    }


def how_fast_did_it_grow(successful_activity):
    daily_wallets = count_daily_active_wallets(successful_activity)
    wallet_count = successful_activity.wallet.nunique()
    return {
        "dau_slope": np.polyfit(np.arange(WINDOW_DAYS), daily_wallets.values, 1)[0],
        "max_milestone_reached": max(milestone for milestone in (0, 100, 1_000, 10_000)
                                     if wallet_count >= milestone),
        "peak_day": int(daily_wallets.idxmax()),
    }


def did_they_stay(successful_activity):
    first_day = successful_activity.groupby("wallet").day_index.min()
    cohort = first_day[first_day <= WINDOW_DAYS - 8]       # day 7 inside the window
    active_days = set(zip(successful_activity.wallet, successful_activity.day_index))
    retained = sum((wallet, day + 7) in active_days for wallet, day in cohort.items())
    days_per_wallet = successful_activity.groupby("wallet").day_index.nunique()
    return {
        "retention_d7": retained / len(cohort) if len(cohort) else np.nan,
        "returning_wallet_share": (days_per_wallet >= 2).mean(),
    }


def few_users_or_many(successful_activity):
    transactions_per_wallet = successful_activity.groupby("wallet").successful_transactions.sum()
    return {"top10_wallet_tx_share":
            transactions_per_wallet.nlargest(10).sum() / transactions_per_wallet.sum()}


def quality_flag(activity):
    return {"failed_tx_share":
            1 - activity.successful_transactions.sum() / activity.all_transactions.sum()}


def compute_features(activity):
    successful_activity = keep_successful(activity)
    if successful_activity.empty:
        return {}
    return {**how_many_came(successful_activity),
            **how_fast_did_it_grow(successful_activity),
            **did_they_stay(successful_activity),
            **few_users_or_many(successful_activity),
            **quality_flag(activity)}


def build_feature_table(dapps, activity):
    return pd.DataFrame([
        {"dapp_id": dapp.dapp_id, "category": dapp.category, "deploy_date": dapp.deploy_date,
         **compute_features(activity[activity.dapp_id == dapp.dapp_id])}
        for dapp in dapps.itertuples()])
