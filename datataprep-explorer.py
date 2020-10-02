
from flask import Flask, render_template,request,Markup
import create_dataprep_objects

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    recipe_url=''

    if request.method == 'POST':

        bucket=request.form['bucket']
        filepath=request.form['filepath']
        recipe_url=create_dataprep_objects.get_recipe_url(bucket,filepath)

    return render_template('home.html',recipe_url=recipe_url)