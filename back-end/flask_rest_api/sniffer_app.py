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
  for doc in coll.find(myquery):
    del doc['_id']
    output.append(doc)
  return jsonify({'result' : output})

@app.route('/interfaces/packet', methods=['GET'])
def get_Nbpackets_By_Interface():
  output = []
  coll = mongo.db.packetIP
  agg_result= coll.aggregate( 
    [{ 
    "$group" :  
        {"_id" : "$interface",
         "nb_packet" : {"$sum" : 1}
         }}
    ]) 
  for doc in agg_result:
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

"""
to complete 
@app.route('/host/packetPerDay', methods=['GET'])
def get_Nbpackets_By_day_curr_month():
    nodeName = request.args.get('nodeName')
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

"""
