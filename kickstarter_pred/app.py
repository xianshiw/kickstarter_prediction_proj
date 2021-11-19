from flask import Flask, render_template, request
from .model import predictor
import pandas as pd


def create_app():

    app = Flask(__name__)
    @app.route('/', methods=["GET", "POST"])
    def root():
        return render_template('home.html')


    @app.route('/predict', methods=["GET", "POST"])
    def predict():

        if request.method == 'POST':
            
            # cols = ['main_category','launched','country','usd_pledged_real']

            df = pd.DataFrame({
                "main_category": [request.values['main_category']], 
                "launched": [request.values['launched']], 
                "country": [request.values['country']], 
                "usd_pledged_real": [request.values['usd_pledged_real']]
            })
            
            # Create prediction from model
            prediction, proba = predictor(df)
            if prediction == 1:
                flag = 'SUCCESSFUL'
            else:
                flag = 'FAIL'

            # Covert array to string response
            results = "Your project is predicted to be {0} with probability {1}".format(flag, proba)

        else:
            results = 'No data has been posted to page.'
        return render_template('results.html', results=results)

    return app