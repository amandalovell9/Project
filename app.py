from flask import Flask, render_template, request
import numpy as np
import pickle
import joblib
app = Flask(__name__)
filename = 'file_housing.pkl'
#model = pickle.load(open(filename, 'rb'))
linear2 = joblib.load(filename)
#model = joblib.load(filename)
@app.route('/')
def index(): 
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    housing_median_age = request.form['housing_median_age']
    total_rooms = request.form['total_rooms']
    median_income = request.form['median_income']
    population = request.form['population']

    
      
    pred = model.predict(np.array([[housing_median_age, total_rooms, median_income, population]]))
    print(pred)
    return render_template('index.html', predict=str(pred))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)