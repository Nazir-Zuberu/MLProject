from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__) # Creating a flask app

app = application # Assigning the app to a short name app

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') # Creating the index page

## Routing for prediction page
@app.route('/predictdata', methods = ['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity= request.form.get('ethnicity'),
            parental_level_of_education= request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course= request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score')),
        ) #Initializing the CustomData class
        pred_df = data.get_data_as_data_frame() # Creating a data frame with the collected data from the rendered form with the get_data_as_data_frame method
        print(pred_df)

        predict_pipeline = PredictPipeline() # Initializing the PredictPipeline class
        results = predict_pipeline.predict(pred_df) # Making prediction with the predict method in PredictPipeline
        return render_template('home.html', results = results[0]) # Rendering the results to the home page
    
if __name__ == '__main__':
    app.run(host= "0.0.0.0", debug = True)

"""
Run this python file in the terminal. Go to a browser and type http://127.0.0.1:5000. This will send
you to the local host where the flask app will be runing. You can navigate to any page by adding the 
name of the function related to the page eg http://127.0.0.1:5000/predictdata with send you to the prediction page
"""