from flask import Flask
import joblib
app = Flask(__name__)

@app.route('/',methods=['GET'])
def hello_world():
    model = joblib.load('rf_churn')
    pred = model.predict([[619,42,2,0.0,0,0,0,101348.88,0,0,0]])
    return f"Prediction is : {pred[0]}";

if __name__ == '__main__':
	app.run()
