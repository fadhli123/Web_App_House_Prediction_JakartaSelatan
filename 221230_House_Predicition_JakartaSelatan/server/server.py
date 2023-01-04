from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_garasi_status', methods=['GET'])
def get_garasi_status():
    response = jsonify({
        'garasi': util.get_garasi_status()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    LT = int(request.form['LT'])
    LB = int(request.form['LB'])
    KT = int(request.form['KT'])
    KM = int(request.form['KM'])
    garasi = request.form['garasi']

    response = jsonify({
        'estimated_price': util.get_estimated_price(LT,LB,KT,KM,garasi)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()