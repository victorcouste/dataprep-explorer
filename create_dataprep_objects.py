
import requests, json
from datetime import datetime


def get_recipe_url(bucket_name,file_path):


    host='https://api.clouddataprep.com'
    datataprep_auth_token='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbklkIjoiZjE1MWI5ZGItMmEyMy00OWUzLTlhYmQtNWU4NmVjYjM1YWI2IiwiaWF0IjoxNTg3OTI3NjkxLCJhdWQiOiJ0cmlmYWN0YSIsImlzcyI6ImRhdGFwcmVwLWFwaS1hY2Nlc3MtdG9rZW5AdHJpZmFjdGEtZ2Nsb3VkLXByb2QuaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLCJzdWIiOiJkYXRhcHJlcC1hcGktYWNjZXNzLXRva2VuQHRyaWZhY3RhLWdjbG91ZC1wcm9kLmlhbS5nc2VydmljZWFjY291bnQuY29tIn0.JcjPJFyhm13LFUjdnceToTU989kCNqowESm8q2Hrq680aMxQHdut3RFk2MVrFKdDIvkctXtwcgOEheSaHHjibKt1SsEsvmciesekltTQrs8Vdl5shXcD7ZcvtWJYarlKnKYaQhF-Bd04ReewsjQizLCwwW1cO2VmFF58iNQpyfNbcy4_xNNMrM00wjjiHazLGmsHR-ZKV7U57MkYpk0YidaUNirz_BEDYljfQumd4n4HvVfF9o5Lxd1lDU_gnaystPHuDn_B6TOzNHvxtUcorNn6B_tJSb9rkHsQVKrMhTDaB_o75Qy5C0C_gVtz0PBkL-2pEWMUakdPhC4lYNyBfw'
    folderId=3128

    file_uri="gs://"+bucket_name+"/"+file_path

    now = datetime.now() # current date and time
    timestamp = now.strftime("%m/%d/%Y, %H:%M")

    #print("Today :", timestamp)

    #timestamp=`date +"%d/%m/%y %H:%M"`
    #echo $timestamp

    flow_name="New Flow - "+timestamp
    flow_description="New Flow description - "+timestamp
    file_name="File - "+timestamp
    recipe_name="Recipe - "+timestamp

    # --------------------------------------------------------------------------------------------
    # -------------- CREATE FLOW ---------------
    # --------------------------------------------------------------------------------------------

    endpoint="/v4/flows"

    parameters = {
        "name": flow_name,
        "description": flow_description,
        "folderId": folderId
    }      
    #print('Parameter: {}'.format(parameters))
            
    resp = requests.post(
        url=host+endpoint,
        headers={"Content-Type":"application/json","Authorization": "Bearer "+datataprep_auth_token},
        data=json.dumps(parameters)
    )
    result=resp.json()
    new_flow_id=result['id']

    #print('Status Code : {}'.format(resp.status_code))
    #print('Result : {}'.format(result))
    #print('New Flow ID : {}'.format(new_flow_id))

    # --------------------------------------------------------------------------------------------
    # ------------------------------ CREATE DATASET ----------------------------------------------
    # --------------------------------------------------------------------------------------------

    endpoint="/v4/importedDatasets"
    detectStructure="false"

    parameters = {
        "uri": file_uri,
        "name": file_name,
        "detectStructure": detectStructure
    }      
    #print('Parameter: {}'.format(parameters))
            
    resp = requests.post(
        url=host+endpoint,
        headers={"Content-Type":"application/json","Authorization": "Bearer "+datataprep_auth_token},
        data=json.dumps(parameters)
    )
    result=resp.json()
    new_dataset_id=result['id']

    #print('Status Code : {}'.format(resp.status_code))
    #print('Result : {}'.format(result))
    #print('New Dataset ID : {}'.format(new_dataset_id))

    # --------------------------------------------------------------------------------------------
    # -------------- ADD DATASET TO FLOW ---------------
    # --------------------------------------------------------------------------------------------

    endpoint="/v4/importedDatasets/"+str(new_dataset_id)+"/addToFlow"

    parameters = {
        "flow": {"id": new_flow_id}
    }      
    #print('Parameter: {}'.format(parameters))
            
    resp = requests.post(
        url=host+endpoint,
        headers={"Content-Type":"application/json","Authorization": "Bearer "+datataprep_auth_token},
        data=json.dumps(parameters)
    )
    result=resp.json()

    #print('Status Code : {}'.format(resp.status_code))
    #print('Result : {}'.format(result))

    # --------------------------------------------------------------------------------------------
    # -------------- ADD RECIPE TO DATASET ---------------
    # --------------------------------------------------------------------------------------------

    endpoint="/v4/wrangledDatasets"

    parameters = {
        "importedDataset":{"id": new_dataset_id},
        "flow": {"id": new_flow_id},
        "name": recipe_name
    }      
    #print('Parameter: {}'.format(parameters))
            
    resp = requests.post(
        url=host+endpoint,
        headers={"Content-Type":"application/json","Authorization": "Bearer "+datataprep_auth_token},
        data=json.dumps(parameters)
    )

    result=resp.json()
    new_recipe_id=result['id']

    #print('Status Code : {}'.format(resp.status_code))
    #print('Result : {}'.format(result))
    #print('New Recipe ID : {}'.format(new_recipe_id))


# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------

#print('Flow URL : https://clouddataprep.com/flows/{}'.format(new_flow_id))

#print('Dataset URL : https://clouddataprep.com/data/{}/{}'.format(new_flow_id,new_recipe_id))
    recipe_url = 'https://clouddataprep.com/data/{}/{}'.format(new_flow_id,new_recipe_id)

    return recipe_url
