from flask import Flask, Blueprint, request, jsonify, g
from flask_restplus import Resource, Api, Namespace, fields, reqparse
from dicttoxml import dicttoxml
import time
from datetime import datetime
import pytz


# Local imports
from src.estimator import estimator

app = Flask(__name__)

api = Api(app)

@app.before_request
def before_req():
    g.start = time.time() * 1000


@app.after_request
def after_req(res):
    f = open('logs.txt', 'a+')
    # time_stamp = int(time.time() * 1000)
    time_stamp = int(datetime.now(tz=pytz.utc).timestamp() * 1000) 
    req_method = request.method
    req_path = request.path[8:]
    res_time = round(time.time() * 1000 - g.start)
    res_status_code = res.status_code

    # f.write("{} \t\t {} \t\t {} \t\t {} \t\t done in {} ms \n".format(time_stamp, req_method, req_path, res_status_code, res_time))
    f.write("{} \t\t {} \t\t done in {:.2f} seconds \n".format(time_stamp,  req_path, res_time/10))

    f.close()
    return res

@api.route('/api/v1/on-covid-19/json')
class InJson(Resource):
    def get(self):
        return {'hello': 'json'}

    def post(self):
        req_data = request.get_json()
        res = estimator(req_data)

        return jsonify(res)

@api.route('/api/v1/on-covid-19/xml')
class InXml(Resource):
    def get(self):
        return {'hello': 'xml'}

    def post(self):
        # arr = []
        req_data = request.get_json()
        res = estimator(req_data)
        dic = {'response': res}
        # arr.append(dic)
        # xml = dicttoxml(res)
        xml = dicttoxml(dic)
        # xml = dicttoxml(dic, custom_root='test', attr_type=False)
        # xml = dicttoxml(arr, custom_root='test', attr_type=False)
        # xml = xml.decode('utf8').replace("'", '"')
        xml = xml.decode('utf8')

        return xml
        

@api.route('/api/v1/on-covid-19/logs')
class Logs(Resource):
    def get(self):
        f = open('logs.txt', 'r')
        res = f.read()
        f.close()

        return res    

    def post(self):

        return {'hello': 'logs'}

if __name__ == '__main__':
    app.run(debug=True)