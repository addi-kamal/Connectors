from google.cloud import bigquery
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
 
from connector.big_query_connector import BigQueryConnector  

bqc = BigQueryConnector()

# Creating a Table with Schema
schema = [
            bigquery.SchemaField("last_updated_time", "TIMESTAMP", mode="REQUIRED"),
            bigquery.SchemaField("si_number", "INTEGER", mode="REQUIRED"),
            bigquery.SchemaField("domain_name", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("cost_value", "NUMERIC", mode="REQUIRED"),
            bigquery.SchemaField("cost_date", "STRING", mode="REQUIRED"),
            ]
bqc.create_table(table_id="secure-proxy-ske.my_first_dataset_ske_project.my_first_ske_table1",project_id="secure-proxy-ske", schema=schema)
