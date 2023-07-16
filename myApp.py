from flask import Flask
import joblib
app = Flask(__name__)

@app.route('/',methods=['GET'])
def hello_world():
    model = joblib.load('rf_heartForecastModel')
    return 'Model Loaded Success!'

if __name__ == '__main__':
	app.run()
