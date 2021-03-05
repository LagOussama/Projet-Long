from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'NetworkTraffic'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/NetworkTraffic'

mongo = PyMongo(app)

@app.route('/host', methods=['GET'])
def get_all_hosts():
  host = mongo.db.Hosts
  output = []
  for s in host.find():
    output.append({'name' : s['hostname'], 'ip_address' : s['ip_address']})
  return jsonify({'result' : output})

@app.route('/network', methods=['GET'])
def get_all_Networks():
  net = mongo.db.Networks
  output = []
  for s in net.find():
    output.append({'ip_address' : s['network'], 'mask' : s['mask'],})
  return jsonify({'result' : output})

@app.route('/host/interfaces', methods=['GET'])
def get_Interfaces_By_Hostname():
  nodeName = request.args.get('nodeName')
  output = []
  coll = mongo.db.Interfaces
  myquery = { "Hostname": nodeName }
  state=" "
  HWaddr=" "
  inet4=" "
  inet6=" "
  Hostname=" "
  HostInterfaceName=" "
  #for doc in coll.find(myquery):
  output.append({'nodename' : nodeName}) 
  return jsonify({'result' : output})


