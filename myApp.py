from flask import Flask, request
import joblib
app = Flask(__name__)

@app.route('/churn',methods=['GET','POST'])
def basic():
    if request.method == 'POST':
        res = request.form
        print(res)
    model = joblib.load('rf_churn')
    pred = model.predict([[619,42,2,0.0,0,0,0,101348.88,0,0,0]])
    return f"Prediction is : {pred[0]}";


if __name__ == '__main__':
	app.run()
