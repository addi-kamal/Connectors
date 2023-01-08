import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
 
from connector.big_query_connector import BigQueryConnector  

bqc = BigQueryConnector()


# Insert rows into our table
rows_to_insert=[( 554354542, 1, 'Finance', 4000, "10/04/2022")]
bqc.create_table_from_query(rows_to_insert=rows_to_insert, dataset_id="my_first_dataset_ske_project", table_id="my_first_ske_table")
