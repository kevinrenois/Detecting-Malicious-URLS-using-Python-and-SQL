# imports
from flask import Flask, request, render_template, jsonify
import numpy as np
import pickle

import pandas as pd
from sqlalchemy import create_engine

# Set up the engine to access SQL data.

# 'driver://username:password@host:port/database'
engine = create_engine('postgres://postgres:kor@localhost:5432/capstone_urls')


# initialize the flask app
app = Flask('CapstoneApp')


#create home page
@app.route('/')
def home():
    return render_template('form.html')


# route 5: accept the form submission and do something fancy with it
# manipulate data into a format that we pass to our model
@app.route("/check")
def make_predictions():
    # load in the form data from the incoming request
    user_input = request.args.getlist('url')

    X_test = user_input[0]

    pipe = pickle.load(open('model.p', 'rb'))
    
    
    try:
        sql = """
        SELECT u.url, u.label
        FROM all_data.urls as u
        WHERE u.url ILIKE '%s'
        """ % X_test

        sql_df = pd.read_sql(sql, engine)#, params = {'thing': X_test})
        
        if sql_df.iloc[0][1] == 1:
            result = 'found in the database. Careful, it is malicious! 🚫'
        elif sql_df.iloc[0][1] == 0:
            result = 'found in the database. Congrats, it is benign! ✅'
        elif sql_df.empty == True:
            raise ValueError('not in database')
    except:
        pred = pipe.predict([X_test])[0]
        if pred == 1:
            result = 'not in the database. The model predicts it is malicious! 🚫'
        else:
            result = 'not in the database. The model predicts it is benign! ✅'
   
    return render_template('results.html', prediction=result)


# Call app.run(debug=True) when python script is called
if __name__ == '__main__':
    app.run(debug=True)