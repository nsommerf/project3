# import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
#from sqlalchemy.orm import Session
#from sqlalchemy import create_engine, func

from flask import Flask, jsonify, Response
import pandas as pd
#from flask_cors import CORS

# Flask set up
app = Flask(__name__)
#CORS(app)

# Routes
@app.route("/")
def index():

	return jsonify({
		"key1": "value1",
		"key2": 2
	})

@app.route("/crimes")
def crimes():

    return jsonify({
		"key1": "crime1",
		"key2": 3
	})
#if __name__ == '__main__':
#    app.run(debug=True)