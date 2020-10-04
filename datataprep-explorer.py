
from flask import Flask, render_template,request,Markup
import create_dataprep_objects

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    recipe_url=''
    dataset_url=''
    flow_url=''
    file_uri=''

    if request.method == 'POST':

        bucket=request.form['bucket']
        filepath=request.form['filepath']

        file_uri="gs://"+bucket+"/"+filepath
        
        dataprep_urls=create_dataprep_objects.get_dataprep_urls(file_uri)

        recipe_url=dataprep_urls['recipe_url']
        dataset_url=dataprep_urls['dataset_url']
        flow_url=dataprep_urls['flow_url']

    return render_template('home.html',file_uri=file_uri,recipe_url=recipe_url,dataset_url=dataset_url,flow_url=flow_url)