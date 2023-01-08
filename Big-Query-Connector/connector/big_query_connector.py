from google.cloud import bigquery


class BigQueryConnector():
    def __init__(self):
        self.connection = bigquery.Client()

    def list_datasets(self,project_id):
        client = bigquery.Client(project=project_id)
        for dataset in client.list_datasets():
            print(dataset.dataset_id)

    # Creating a Dataset
    def create_dataset(self,dataset_id, location, project_id):
        client = bigquery.Client(project=project_id)
        dataset = client.dataset(dataset_id)
        dataset.location = location
        dataset = client.create_dataset(bigquery.Dataset(dataset))

    # Creating a Table with Schema
    def create_table(self,table_id,project_id, schema):
        client = bigquery.Client(project=project_id)
        table = bigquery.Table(table_id, schema=schema)
        table = client.create_table(table)
        print(
            "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
            )

    # Adding Rows to a Table
    def create_table_from_query(self,rows_to_insert,dataset_id, table_id):
        client = bigquery.Client()
        
        dataset_ref = client.dataset(dataset_id)
        table_ref = dataset_ref.table(table_id)
        table = client.get_table(table_ref)
        
        errors = client.insert_rows(table, rows_to_insert)
        # insert_rows return an empty list if no errors 
        print(errors)

    # Querying the data using SQL queries
    def client_query(self,query):

            client = bigquery.Client()
            query_job = client.query(query)

            print("The query data:")
            for row in query_job:
                print(row)
