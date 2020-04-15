import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__) #Initialize the flask App
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')



# prediction function updated
def predict(to_predict_list): 
    to_predict = np.array(to_predict_list).reshape(1, 13) 
    model = pickle.load(open("model.pkl", "rb")) 
    result = model.predict(to_predict) 
    return result[0] 
  
@app.route('/predict', methods = ['POST']) 
def result(): 
    if request.method == 'POST': 
        to_predict_list = request.form.to_dict() 
        to_predict_list = list(to_predict_list.values()) 
        to_predict_list = list(map(int, to_predict_list)) 
        result = ValuePredictor(to_predict_list)         
        if int(result)== 1: 
            prediction ='Income more than 50K'
        else: 
            prediction ='Income less that 50K'            
        return render_template('result.html', prediction = prediction)

if __name__ == "__main__":
    app.run()