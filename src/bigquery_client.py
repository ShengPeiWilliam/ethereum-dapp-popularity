# BigQuery connection and query runner
from google.cloud import bigquery
from config import PROJECT_ID, ETHEREUM_DATASET, MAX_GB_PER_QUERY

_client = None


def get_client():
    global _client
    if _client is None:
        _client = bigquery.Client(project=PROJECT_ID)
    return _client


def load_sql(query_name):
    with open(f"sql/{query_name}.sql") as sql_file:
        return sql_file.read().format(ETHEREUM_DATASET=ETHEREUM_DATASET)


def run_query(query_name, parameters):
    job_config = bigquery.QueryJobConfig(
        query_parameters=parameters,
        maximum_bytes_billed=int(MAX_GB_PER_QUERY * 1e9))
    job = get_client().query(load_sql(query_name), job_config=job_config)
    result = job.to_dataframe()
    print(f"{query_name}: {job.total_bytes_processed / 1e9:.2f} GB")
    return result
