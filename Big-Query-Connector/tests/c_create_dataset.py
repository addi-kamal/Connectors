import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
 
from connector.big_query_connector import BigQueryConnector  

bqc = BigQueryConnector()


# Creating a new dataset
bqc.create_dataset(dataset_id="my_first_dataset_ske_project", location="us-central1", project_id="secure-proxy-ske")
print("after creating our ske dataset :")
print(bqc.list_datasets(project_id="secure-proxy-ske"))