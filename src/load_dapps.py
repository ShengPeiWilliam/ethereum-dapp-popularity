# DApp list and deploy date (day 0)
import pandas as pd
from google.cloud import bigquery
from config import PILOT_DAPPS
from src.bigquery_client import run_query


def load_dapps():
    contracts = pd.DataFrame(
        [(dapp_id, category, address.lower())
         for dapp_id, category, addresses in PILOT_DAPPS
         for address in addresses],
        columns=["dapp_id", "category", "contract_address"])

    deployed = run_query("deploy_date", [
        bigquery.ArrayQueryParameter("addresses", "STRING", contracts.contract_address.tolist())])

    missing = set(contracts.contract_address) - set(deployed.contract_address)
    if missing:
        print(f"not found as contracts, dropped: {sorted(missing)}")

    dapps = (contracts.merge(deployed, on="contract_address")
             .groupby("dapp_id")
             .agg(category=("category", "first"),
                  contract_address=("contract_address", lambda addresses: ";".join(addresses)),
                  deploy_date=("deployed_at", "min"))
             .reset_index())
    dapps["deploy_date"] = pd.to_datetime(dapps["deploy_date"], utc=True).dt.floor("D")
    return dapps
