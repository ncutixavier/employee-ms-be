import os
from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
from sqlalchemy import create_engine

app = Flask(__name__)

load_dotenv()

DATABASE_URI = os.environ.get('DEVELOPMENT_DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)

engine = create_engine(DATABASE_URI)

@app.route("/")
def hello():
    try:
        engine.connect()
        print('DB Connected')
        return jsonify({'message': 'App is running!'})
    except Exception as e:
        return jsonify({'message': 'Error connecting to database'}), 500


@app.route("/employees")
def getAllEmployees():
    return jsonify({'message':'Data fetched successfully!'})

if __name__ == "__main__":
    app.run(debug=True)
