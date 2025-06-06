from flask import Flask, jsonify
from pymongo import MongoClient
import os
from flask_cors import CORS
app = Flask(__name__)
client = MongoClient('mongodb+srv://apkoundinya:v3VVVZ1Fj3vOFf5g@cluster0.s4d3zix.mongodb.net/')
db = client["STARS"]
collection = db["april_2025"]

@app.route('/get_stock_data', methods=['GET'])
def get_stock_data():
    data = list(collection.find({}, {'_id': 0}))  # remove _id for cleaner output
    return jsonify(data)
if __name__=="__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
    
