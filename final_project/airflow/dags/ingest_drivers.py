import requests 
import json
import pandas as pd 
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
from google.cloud import storage

def main():

    url = "http://ergast.com/api/f1/drivers.json?limit=1000"
    response = requests.get(url)

    try:
        data = response.json()
        drivers_list = []

        for i in range(len(data['MRData']['DriverTable']['Drivers'])):
            drivers_list.append(data['MRData']['DriverTable']['Drivers'][i])

        drivers_df = pd.json_normalize(drivers_list)
        
        #path = '/Users/souravsaha/Desktop/data_engineering_project/final_project/f1_csv_files/drivers.csv'
        path = '/opt/airflow/f1_csv_files/drivers.csv'
        drivers_csv = drivers_df.to_csv(path)

        credentials = GoogleCredentials.get_application_default()
        client = storage.Client(project='dtc-de', credentials=credentials)
        bucket = client.get_bucket('de_project_f1')
        blob = bucket.blob("stg_drivers/drivers.csv")

        blob.upload_from_filename(path)
        print("Successfully uploaded!")

    except Exception as e: 
        print(e)

if __name__ == '__main__':
    main() 