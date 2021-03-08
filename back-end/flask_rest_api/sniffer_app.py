from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import datetime
from dateutil import parser

from flask_cors import CORS, cross_origin

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'NetworkTraffic'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/NetworkTraffic'

#app.config['MONGO_DBNAME'] = 'NetworkTraffic'
#app.config['MONGO_URI'] = 'mongodb://localhost:27017/NetworkTraffic'

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
  allInterfacesInfo = get_intefaces_info(host_name)
  output = []
  nb_packet = get_Nbpackets_By_Host(host_name)
  for s in host.find():
    if s['hostname'] == host_name:
      output.append({'name' : s['hostname'], 'ip_address' : s['ip_address'], 'interfaces' : allInterfacesInfo, 'nb_packet': nb_packet})
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
def get_Nbpackets():
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


def get_Nbpackets_By_Host(host_name):
    coll = mongo.db.packetIP
    IpAdresses = getip4interfaces(host_name)
    res = coll.count_documents( { "$or" :[{"ipDestination" : { "$in": IpAdresses }},{"ipSource" : { "$in": IpAdresses }}]})
    return res


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


def get_intefaces_info(host_name):
    coll = mongo.db.Interfaces
    query = {"Hostname":host_name}
    interfaceInfo = coll.find(query)
    output = []
    for doc in interfaceInfo:
      del doc['_id']
      if 'inet6' in doc:
         del doc['inet6']
      if 'inet4' in doc:
        doc['nb_packet_i'] = get_Nbpackets_Interface(doc['inet4'].split("/")[0])
      else:
        doc['nb_packet_i'] = 0
      output.append(doc)
    #return list(interfaceInfo)
    return output

def get_Nbpackets_Interface(ipAdrr):
  res = mongo.db.packetIP.count_documents({"ipDestination" : str(ipAdrr) })
  res2 = mongo.db.packetIP.count_documents({"ipSource" : str(ipAdrr) })
  return res+res2



#if __name__ == "__main__":
#   app.run(host='0.0.0.0')


#print(get_Nbpackets_By_day_last30Day())
