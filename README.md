# dataprep-explorer

A simple Web application to explore **Google Cloud Storage files(https://cloud.google.com/storage)** with **Google Cloud Dataprep by Trifata(https://cloud.google.com/dataprep")**.
The application create all necessary Dataprep objects (Dataset, Flow and Recipe) and generate URLs to Dataprep interfaces.

This Web application use Python Flask Web framework and Dataprep REST API (https://api.trifacta.com/)

## Installation

* Install the Python Flask framework

  Full instructions with virtual environment here https://flask.palletsprojects.com/en/1.1.x/installation/
  
* Install Python requests module https://requests.readthedocs.io/en/master/user/install/

      pip install requests

* Install the Dataprep Explorer Web app

  Clone this repo

      git clone https://github.com/victorcouste/dataprep-explorer.git

## Running

1/ Update 

2/ Start the Flask Web app

  In the Dataprep Explorer directory run:
    
    export FLASK_APP=datataprep-explorer.py
    flask run
  
Now you must be able to go to http://127.0.0.1:5000/ and play with the application:

  
  ![alt tag](https://github.com/victorcouste/dataprep-explorer/blob/master/Explore_a_Google_GCS_file_with_Cloud_Dataprep.png)
