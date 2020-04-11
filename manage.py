from flask import Flask, Blueprint, request, jsonify, g
from flask_restplus import Resource, Api, Namespace, fields, reqparse
from dicttoxml import dicttoxml
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import time
from datetime import datetime, timezone


# Local imports
from src.estimator import estimator

app = Flask(__name__)

api_v1 = Blueprint('api', __name__)

api = Api(app)
# api = Api(
#     api_v1, title='Covid-19 API :: v1', doc='/', version='1.0', 
#     # path='/api/v1/on-covid-19',
#     description='Covid-19 is a online tool to estimate the impact and severity of Covid-19.',)

# del api.namespaces[0]
# api.add_namespace(new_ns, path='/api/v1/auth')

@app.before_request
def before_req():
    g.start = time.time() * 1000


@app.after_request
def after_req(resp):
    f = open('logs.txt', 'a+')
    # time_stamp = datetime.utcnow().replace(tzinfo=timezone.utc)
    time_stamp = time.time()
    req_method = request.method
    req_path = request.path
    res_time = round(time.time() * 1000 - g.start)
    res_status_code = resp.status_code

    f.write("{} \t\t {} \t\t {} \t\t {} \t\t {} ms \n".format(time_stamp, req_method, req_path, res_status_code, res_time))
    f.close()
    return resp

@api.route('/api/v1/on-covid-19/json')
class InJson(Resource):
    def get(self):
        return {'hello': 'json'}

    def post(self):
        # def get_estimation_default():
        req_data = request.get_json()
        res = estimator(req_data)

        return jsonify(res)
        # return {}

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
        # xml = ET.fromstring(xml)
        # xml = BeautifulSoup(xml)
        xml = xml.decode('utf8')

        return xml

        # return {}


@api.route('/api/v1/on-covid-19/logs')
class Logs(Resource):
    def get(self):
        f = open('logs.txt', 'r')
        resp = f.read()
        f.close()

        return resp    
        # return {'hello': 'logs'}

    def post(self):

        return {}

if __name__ == '__main__':
    app.run(debug=True)