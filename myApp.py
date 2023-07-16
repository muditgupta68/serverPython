from flask import Flask, request,jsonify 
import joblib
app = Flask(__name__)

@app.route('/',methods=['POST'])
def basic():
    if request.method == 'POST':
        res = request.form
        model = joblib.load('rf_churn')
        pred = model.predict([[619,42,2,0.0,0,0,0,101348.88,0,0,0]])
        return jsonify(
            data=res,
            pred=int(pred[0]))


if __name__ == '__main__':
	app.run()
