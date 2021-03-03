from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'NetworkTraffic'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/NetworkTraffic'

mongo = PyMongo(app)

@app.route('/star', methods=['GET'])
def get_all_hosts():
  host = mongo.db.Hosts
  output = []
  for s in host.find():
    output.append({'name' : s['hostname'], 'distance' : s['ip_address']})
  return jsonify({'result' : output})
