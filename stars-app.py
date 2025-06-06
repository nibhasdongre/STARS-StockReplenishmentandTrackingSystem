from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb+srv://apkoundinya:v3VVVZ1Fj3vOFf5g@cluster0.s4d3zix.mongodb.net/')
db = client["STARS"]
collection = db["april_2025"]

@app.route('/get_stock_data', methods=['GET'])
def get_stock_data():
    data = list(collection.find({}, {'_id': 0}))  # remove _id for cleaner output
    return jsonify(data)
