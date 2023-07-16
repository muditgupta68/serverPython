from flask import Flask, request,jsonify 
import joblib
app = Flask(__name__)

@app.route('/churn',methods=['POST'])
def churn():
    if request.method == 'POST':
        res = request.form
        model = joblib.load('rf_churn')
        pred = model.predict([[619,42,2,0.0,0,0,0,101348.88,0,0,0]])
        # return jsonify(
        #     data=res,
        #     pred=int(pred[0]))
        if(res):
            return f'The data recieved is {res}'
        else:
            return 'data not recieved'        
        
@app.route('/',methods=['GET'])
def start():
    return 'Hello Mudit'

if __name__ == '__main__':
	app.run()
