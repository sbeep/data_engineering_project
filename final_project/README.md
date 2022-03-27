# DE Zoomcamp Final Project Plan

1. Select a dataset that you're interested in (see datasets.md)
	- http://ergast.com/mrd/
2. Create a pipeline for processing this dataset and putting it to a datalake
	- Experiment with Jupyter Notebook, then use python file to put data into Google Cloud Storage (data lake). This will serve as a data lake (staging layer) for us to put our files. 
	- Divide the 1.8GB file into sub files so that spark can process it quicker
	- Parquetize the file?
 3. Create a pipeline for moving the data from the lake to a data warehouse
	- Using Spark to create tables and move data from data lake (staging layer) into BigQuery data warehouse (persistent layer)
4. Transform the data in the data warehouse: prepare it for the dashboard
	- Use dbt/spark 
5. Create a dashboard
	Use Data Studio (create 2 tiles) 

- Data Lake and BigQuery to be provisioned using Terraform 
- Steps 2 & 3 to be orchestrated using Airflow 

### Project reproducability
1. `cd` to the final project root directory (final_project/) and run `docker-compose up`
2. To create the cloud resources (gcs buckets, folders, bigquery datasets & tables) Run `terraform init` -> `terraform plan` -> `terraform apply` -> `terraform kill`. Adjust the region of the resources to your preferred location.
3. Google Data Studio Dashboard link (refreshes on a weekly basis): https://datastudio.google.com/s/vQKs-qblqXI
