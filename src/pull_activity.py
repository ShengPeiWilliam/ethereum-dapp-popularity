# Activity: one row per wallet per day, first WINDOW_DAYS after day 0
import pandas as pd
from google.cloud import bigquery
from config import WINDOW_DAYS
from src.bigquery_client import run_query


def pull_activity(dapp):
    start = dapp.deploy_date
    end = start + pd.Timedelta(days=WINDOW_DAYS)
    activity = run_query("activity", [
        bigquery.ScalarQueryParameter("start", "TIMESTAMP", start.to_pydatetime()),
        bigquery.ScalarQueryParameter("end", "TIMESTAMP", end.to_pydatetime()),
        bigquery.ArrayQueryParameter("addresses", "STRING", dapp.contract_address.split(";"))])
    activity["dapp_id"] = dapp.dapp_id
    activity["day_index"] = (pd.to_datetime(activity["day"]) - start.tz_localize(None)).dt.days   # 0 = launch day
    return activity


def pull_all_activity(dapps):
    return pd.concat([pull_activity(dapp) for dapp in dapps.itertuples()], ignore_index=True)
