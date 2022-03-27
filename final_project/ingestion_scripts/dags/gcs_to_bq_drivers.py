import six
from google.cloud import bigquery

def main():

    client = bigquery.Client(project='top-vial-340214')
    table_id = "top-vial-340214.f1_dataset.per_drivers"

    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
    )
    uri = "gs://de_project_f1/stg_drivers/drivers.csv"

    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )  # Make an API request.

    load_job.result()  

    destination_table = client.get_table(table_id)  
    print("Successfully loaded {} rows!".format(destination_table.num_rows))

if __name__ == '__main__':
    main() 