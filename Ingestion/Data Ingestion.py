import pandas as pd
import requests as req
import google.cloud.bigquery as bq
import prefect as pf
import os
from prefect import flow, task
from dotenv import load_dotenv
load_dotenv()


    #Fetching data from API
@task
def ingest_data(api_url):
    response = req.get(api_url)

    if response.status_code ==200:
        data = response.json()
        df = pd.DataFrame(data)
        print("Data fetched successfully from API")
        return df
    else:
        print("Failed to fetch data from API")
        return None

    #Loading data to BigQuery
@task
def load_to_bigquery(df, table_id):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    client = bq.Client(project=os.getenv("BIGQUERY_PROJECT"))
    dataset_id = os.getenv("BIGQUERY_DATASET")
    table_ref = client.dataset(dataset_id).table(table_id)
    job_config = bq.LoadJobConfig(
        write_disposition=bq.WriteDisposition.WRITE_TRUNCATE
    )
    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
    job.result()
    print("Data loaded successfully to BigQuery")
@flow
def main():
    df = ingest_data(os.getenv("USERS_URL"))     
    if df is not None:
        load_to_bigquery(df, "ecommercerawusers")

    df = ingest_data(os.getenv("PRODUCTS_URL"))  
    if df is not None:                                   
        load_to_bigquery(df, "ecommercerawproducts")       

    df = ingest_data(os.getenv("CARTS_URL"))      
    if df is not None:                                     
        load_to_bigquery(df, "ecommercerawcarts")           


if __name__ == "__main__":
    main.serve(
        name="ecommerce-pipeline",
        cron="0 * * * *"  
    )

