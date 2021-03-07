from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import datetime
from dateutil import parser

from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'NetworkSniffing'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/NetworkTraffic'

cors = CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})


mongo = PyMongo(app)

@app.route('/host', methods=['GET'])
def get_all_hosts():
  host = mongo.db.Hosts
  output = []
  for s in host.find():
    output.append({'name' : s['hostname'], 'ip_address' : s['ip_address']})
  return jsonify({'result' : output})

@app.route('/host/<host_name>', methods=['GET'])
def get_host_by_id(host_name):
  host = mongo.db.Hosts
  output = []
  for s in host.find():
    if s['hostname'] == host_name:
      output.append({'name' : s['hostname'], 'ip_address' : s['ip_address'], 'interfaces' : s['interfaces']})
  return jsonify({'result' : output})



@app.route('/network', methods=['GET'])
@cross_origin()
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
  for doc in coll.find(myquery):
    del doc['_id']
    output.append(doc)
  return jsonify({'result' : output})

def getip4interfaces(hostname):
    coll = mongo.db.Interfaces
    query = {'inet4': { "$exists": True}, "Hostname":hostname}
    host_interfaces = coll.find(query)
    ip4addreses = []
    for interface in host_interfaces:
            ip4addreses.append(interface['inet4'].split("/")[0])
    return ip4addreses

@app.route('/host/packet', methods=['GET'])
def get_Nbpackets_By_Host():
    output = []
    coll = mongo.db.packetIP
    for host in mongo.db.Hosts.find():
        d = {}
        d["hostname"] = host["hostname"]
        IpAdresses = getip4interfaces(host["hostname"])
        print(IpAdresses)
        res = coll.count_documents( { "$or" :[{"ipDestination" : { "$in": IpAdresses }},{"ipSource" : { "$in": IpAdresses }}]})
        d["nb_packet"] = res
        output.append(d)
    return jsonify({'result' : output})

@app.route('/host', methods=['GET'])
def get_Nbpackets_By_day_last30Day():
    #nodeName = request.args.get("nodeName")
    IpAdresses = getip4interfaces("nodeName")
    now = datetime.datetime.utcnow()
    last_30d = (now - datetime.timedelta(days=30))
    output  = mongo.db.packetIP.aggregate([
    {"$match" : {"$and": [
                      {"time" : {"$gt" : last_30d}},
                      { "$or" : [{"ipDestination" : { "$in": IpAdresses }},{"ipSource" : {"$in": IpAdresses }}]}
                        ]
                }
    },
    {"$project":{"year":{"$year":"$time"}, "month":{"$month":"$time"},"day": {"$dayOfMonth":"$time"}}},
    {"$group":{"_id" :{ "year" :"$year", "month" :"$month", "day" :"$day"}, "nb_packet":{"$sum" :1}}}
    ])
    return jsonify({'result' : output})
    #return list(output)

@app.route('/host/interface', methods=['GET'])
def get_inteface_info():
    nodeName = request.args.get("nodeName")
    interface = request.args.get("interface")
    coll = mongo.db.Interfaces
    query = {"HostInterfaceName":interface, "Hostname":nodeName}
    interfaceInfo = coll.find(query)
    output = []
    for doc in interfaceInfo:
      del doc['_id']
      output.append(doc)
    #return list(interfaceInfo)
    return jsonify({'result' :output})

#print(get_Nbpackets_By_day_last30Day())
