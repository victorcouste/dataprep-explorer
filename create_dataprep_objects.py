
import requests, json
from datetime import datetime


# --- Token for Dataprep Authentication - Can be generated in Dataprep interface for project's owner
DATAPREP_AUTH_TOKEN='XXXXXXXXXXXX'
# --- Dataprep folder ID to create new flows
DATAPREP_FOLDERID=yyyyyyy

def get_dataprep_urls(file_uri):

    now = datetime.now() # current date and time
    timestamp = now.strftime("%d/%m/%y %H:%M")

    #print("Today :", timestamp)
    #timestamp=`date +"%d/%m/%y %H:%M"`
    #echo $timestamp

    flow_name="Flow - "+timestamp
    flow_description="Flow description - "+timestamp
    dataset_name="Dataset - "+timestamp
    recipe_name="Recipe - "+timestamp

    new_flow_id = create_dataprep_flow(flow_name,flow_description)
    new_dataset_id = create_dataprep_dataset(file_uri,dataset_name)
    add_dataset_to_flow(new_flow_id,new_dataset_id)
    new_recipe_id = add_recipe_to_dataset(new_flow_id,new_dataset_id,recipe_name)

    recipe_url = 'https://clouddataprep.com/data/{}/{}'.format(new_flow_id,new_recipe_id)
    dataset_url = 'https://clouddataprep.com/datasets/{}'.format(new_dataset_id)
    flow_url = 'https://clouddataprep.com/flows/{}'.format(new_flow_id)

    dataprep_urls={'recipe_url': recipe_url, 'dataset_url': dataset_url, 'flow_url': flow_url}

    return dataprep_urls


# --------------------------------------------------------------------------------------------
# -------------- CREATE FLOW ---------------
# --------------------------------------------------------------------------------------------

def create_dataprep_flow(flow_name, flow_description):

    endpoint="/v4/flows"

    parameters = {
        "name": flow_name,
        "description": flow_description,
        "folderId": DATAPREP_FOLDERID
    }      
    #print('Parameter: {}'.format(parameters))
            
    resp = requests.post(
        url="https://api.clouddataprep.com"+endpoint,
        headers={"Content-Type":"application/json","Authorization": "Bearer "+DATAPREP_AUTH_TOKEN},
        data=json.dumps(parameters)
    )
    result=resp.json()
    new_flow_id=result['id']

    #print('Status Code : {}'.format(resp.status_code))
    #print('Result : {}'.format(result))
    #print('New Flow ID : {}'.format(new_flow_id))

    return new_flow_id

# --------------------------------------------------------------------------------------------
# ------------------------------ CREATE DATASET ----------------------------------------------
# --------------------------------------------------------------------------------------------

def create_dataprep_dataset(file_uri,dataset_name):

    endpoint="/v4/importedDatasets"

    parameters = {
        "uri": file_uri,
        "name": dataset_name
    }      
    #print('Parameter: {}'.format(parameters))
            
    resp = requests.post(
        url="https://api.clouddataprep.com"+endpoint,
        headers={"Content-Type":"application/json","Authorization": "Bearer "+DATAPREP_AUTH_TOKEN},
        data=json.dumps(parameters)
    )
    result=resp.json()
    new_dataset_id=result['id']

    #print('Status Code : {}'.format(resp.status_code))
    #print('Result : {}'.format(result))
    #print('New Dataset ID : {}'.format(new_dataset_id))

    return new_dataset_id

# --------------------------------------------------------------------------------------------
# -------------- ADD DATASET TO FLOW ---------------
# --------------------------------------------------------------------------------------------

def add_dataset_to_flow(flow_id,dataset_id):


    endpoint="/v4/importedDatasets/"+str(dataset_id)+"/addToFlow"

    parameters = {
        "flow": {"id": flow_id}
    }      
    #print('Parameter: {}'.format(parameters))
            
    resp = requests.post(
        url="https://api.clouddataprep.com"+endpoint,
        headers={"Content-Type":"application/json","Authorization": "Bearer "+DATAPREP_AUTH_TOKEN},
        data=json.dumps(parameters)
    )
    result=resp.json()

    #print('Status Code : {}'.format(resp.status_code))
    #print('Result : {}'.format(result))

    return

# --------------------------------------------------------------------------------------------
# -------------- ADD RECIPE TO DATASET ---------------
# --------------------------------------------------------------------------------------------

def add_recipe_to_dataset(flow_id,dataset_id,recipe_name):


    endpoint="/v4/wrangledDatasets"

    parameters = {
        "importedDataset":{"id": dataset_id},
        "flow": {"id": flow_id},
        "name": recipe_name
    }      
    #print('Parameter: {}'.format(parameters))
            
    resp = requests.post(
        url="https://api.clouddataprep.com"+endpoint,
        headers={"Content-Type":"application/json","Authorization": "Bearer "+DATAPREP_AUTH_TOKEN},
        data=json.dumps(parameters)
    )

    result=resp.json()
    new_recipe_id=result['id']

    #print('Status Code : {}'.format(resp.status_code))
    #print('Result : {}'.format(result))
    #print('New Recipe ID : {}'.format(new_recipe_id))

    return new_recipe_id
