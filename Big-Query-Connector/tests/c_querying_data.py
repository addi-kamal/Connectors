import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
 
from connector.big_query_connector import BigQueryConnector  

bqc = BigQueryConnector()


# Querying the data
query = """
        SELECT *
        FROM `secure-proxy-ske.my_first_dataset_ske_project.my_first_ske_table`
    """
bqc.client_query(query=query)