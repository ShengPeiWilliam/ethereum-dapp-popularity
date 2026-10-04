# ethereum-dapp-popularity

Early-activity features for Ethereum DApps, computed from the public BigQuery Ethereum dataset.
For each DApp: contract addresses → first 30 days of transactions → one row of features.

## Run

```bash
conda activate dapp
pip install -r requirements.txt
gcloud auth application-default login
python main.py
```

Writes `data/pilot_features.csv` (one row per DApp) and `data/pilot_daily_active_wallets.csv`.
One run scans about 12 GB in BigQuery.

## Layout

- `config.py`: DApp list (`PILOT_DAPPS`), window length (`WINDOW_DAYS`), BigQuery project
- `sql/`: the two queries (deploy date, wallet activity)
- `src/`: one file per pipeline step, called in order by `main.py`
