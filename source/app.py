from flask import Flask, request, render_template
import pickle
import numpy as np
@app.route('/')
def test():
        return render_template('home.html')
@app.route('/predict')
def get_delay():
        sen = ["date1","29000","date2","30000"]
        inr = ["68","69"]
        go = ["28000","29000"]
        result = {}
        result['INR'] = float(sen[1])
        result['GOLD'] = float(inr[0])
        result['SENSEX'] = float(go[0])
        result1 = {}
        result1['INR'] = float(sen[3])
        result1['GOLD'] = float(inr[1])
        result1['SENSEX'] = float(go[1])
        pkl_file = open('model.pkl', 'rb')
        logmodel = pickle.load(pkl_file)
        prediction = logmodel.predict(np.array([[float(result['INR']),float(result['SENSEX']),float(result['GOLD'])]]))
        pre = logmodel.predict(np.array([[float(result1['INR']),float(result1['SENSEX']),float(result1['GOLD'])]]))
        return render_template('result.html',date_now = sen[0],prediction=prediction,date_back = sen[2],pre = pre,correct = sen[1])
if __name__ == '__main__':
	app.run()
