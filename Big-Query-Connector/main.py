from google.cloud import bigquery
from connector.big_query_connector import BigQueryConnector

bqc = BigQueryConnector()


# Print all the available datasets in the secure-proxy-ske project
print(bqc.list_datasets(project_id="secure-proxy-ske"))


# Creating a new dataset
bqc.create_dataset(dataset_id="my_first_dataset_ske_project", location="us-central1", project_id="secure-proxy-ske")
print("after creating our ske dataset :")
print(bqc.list_datasets(project_id="secure-proxy-ske"))


# Creating a Table with Schema
schema = [
            bigquery.SchemaField("last_updated_time", "TIMESTAMP", mode="REQUIRED"),
            bigquery.SchemaField("si_number", "INTEGER", mode="REQUIRED"),
            bigquery.SchemaField("domain_name", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("cost_value", "NUMERIC", mode="REQUIRED"),
            bigquery.SchemaField("cost_date", "STRING", mode="REQUIRED"),
            ]
bqc.create_table(table_id="secure-proxy-ske.my_first_dataset_ske_project.my_first_ske_table",project_id="secure-proxy-ske", schema=schema)


# Insert rows into our table
rows_to_insert=[( 554354542, 1, 'Finance', 4000, "10/04/2022")]
bqc.create_table_from_query(rows_to_insert=rows_to_insert, dataset_id="my_first_dataset_ske_project", table_id="my_first_ske_table")


# Querying the data
query = """
        SELECT *
        FROM `secure-proxy-ske.my_first_dataset_ske_project.my_first_ske_table`
    """
bqc.client_query(query=query)